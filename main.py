#####################################################################################
#                                                                                   #
#    Detección de heridas en imágenes RGB-D integrado en un sistema ciberfísico     #
#    para la asistencia a la sutura laparoscópica.                                  #
#    Copyright (C) 2023. Duna de Luis Moura.                                        #
#                                                                                   #
#    This program is free software: you can redistribute it and/or modify           #
#    it under the terms of the GNU General Public License as published by           #
#    the Free Software Foundation, either version 3 of the License, or              #
#    (at your option) any later version.                                            #
#                                                                                   #
#    This program is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#    GNU General Public License for more details.                                   #
#                                                                                   #
#    You should have received a copy of the GNU General Public License              #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.         #
#                                                                                   #    
#####################################################################################
### MAIN ###

# Standard library imports
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import rcParams


# Local imports
import M1_acquisition_module
import M2_processing_module.Filters as filter
import M2_processing_module.Utilities
from M2_processing_module.nextNeighbour import next_neighbour
import M3_wound_detection_module.Wound as wound
import M4_stitches_module.Stitches
import M4_stitches_module.ReferenceSystem 
import M5_classifier_module.KmeanClassifier as kmean

# CHAGE THIS ADDRESS!!
dir = "/home/duna/Escritorio/CameraFeature/TFG_Duna/M5_classifier_module"

print("Environment Ready")

def main():

    ## 1. ADQUISITION OF THE IMAGE ##
    # Initiate the camera variable
    camera = M1_acquisition_module.Camera()
    camera.init_camera()

    # Stablish the resolution parameters
    resolution = {
        'width': 640,
        'height': 480
    }
    camera.set_resolution(resolution['height'], resolution['width'])
    
    # Obtaining the image from de camera
    [aligned_frames, color_frame] = camera.get_align()
    [depth_colormap, color_image, intr, depth_image] = camera.get_image(aligned_frames, color_frame)

    # Store the parameters of the image
    w = aligned_frames.get_width()
    h = aligned_frames.get_height()
    print(f"(W, H) = ({w}, {h})")
    
    utils = M2_processing_module.Utilities()

    # Get the distance to de center of the image and the pixel scale
    distance = camera.get_distance(aligned_frames, w, h)
    px_scale = utils.px_scale_calculator(aligned_frames, intr, w, h)
    
    print('The body is '+ str(round(distance, 3)) +' cm away')
    print(f"Pixel scale (x1):  {px_scale}")

    # Change the BGD image to RGB
    depth_colormap_rgb = depth_colormap[:,:,::-1]

    # Change the impression parameters globally
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 25
   
    # Show the color image and the depth color map
    image = np.hstack((color_image, depth_colormap_rgb))
    #cv2.circle(image, (w//2, h//2), 10, [255, 255, 0], -1)
   
    # Show the images
    fig, axes = plt.subplots(1,1)
    im = axes.imshow(image)
    #plt.axis('off')
    plt.xlabel('X [px]', fontdict = {'fontsize' : 25})
    plt.ylabel('Y [px]', fontdict = {'fontsize' : 25})
    plt.title("Depth colormap", fontdict = {'fontsize' : 30})

    # Legend color bar
    c = utils.gradient_colorbar()
    cmap = colors.ListedColormap(c)
    d_max = np.max([valor for fila in depth_image for valor in fila if valor/100 < distance+10])
    d_min = np.min([valor for fila in depth_image for valor in fila if valor/100 != 0])

    norm = colors.Normalize(d_min/1000, d_max/1000)
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(cm.ScalarMappable(norm, cmap), cax)
    cbar.set_label('cm', fontdict = {'fontsize' : 20})
    plt.show()

    # Representing the original image
    utils.grid('Depth image', depth_image, ' [px]')
    #print(len(depth_image))

    ## 2. PROCESSING THE IMAGE ##
    # Reshaped the death pixels
    death_px = camera.death_zones(distance, w)
    OFFSET = 100
    reshaped = filter.reshape(depth_image, death_px, OFFSET)
    utils.grid('Reshaped image', reshaped, ' [px]')

    # Validate the quality of the image
    null = filter.null_px(reshaped)
    total_px = w * h
    print(f"Null pixels (%): {round(null*100/total_px, 2)} %")
   
    # Interpolate the null pixels
    corrected = filter.interpolate(reshaped)
    #utils.grid('Corrected image', corrected, ' [px]')
    
    # Invert the matrix
    invert = filter.invert(corrected)
    #utils.grid('Invert image', invert, ' [px]')
    
    # Smooth the image
    smooth = filter.smoothing(invert)
    utils.grid('Smooth image', smooth, ' [px]')

    # Apply gradient to the image
    gradient = filter.gradient(smooth)
    utils.grid_gradient('Gradient 3D', gradient, ' [px]')

    ## 3. DETECTING THE WOUND ##
    # Binarize the injury and 2D representation
    binary = wound.binaritation(gradient)
    utils.surf('Binary gradient', binary, ' [px]')

    binary = wound.no_border(binary)
    #utils.surf('Binary gradient (no border)', binary, ' [px]')

    # Contours detected
    contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
    print("Number of contours found: " + str(len(contours)))
    #utils.surf('Binary image', binary, ' [px]')

    # Detect the region with the major area and it's centroid
    injury, cx, cy = wound.detect_wound(binary)
    #utils.surf('Wound detected', injury, ' [px]')

    # Fill the wound detected knowing the centroid
    injury = wound.fill_area(injury, cx, cy)
    utils.surf('Wound', injury, ' [px]')

    # Obtain propertires of the injury
    prop = wound.properties(injury)
    phi = prop[0].orientation

    # ROI image
    b1, b2, b3, b4 = wound.roi_coor(injury, prop[0])
    roi_image = []
    for x in range(b1, b3):
        roi_image.append(smooth[x][b2:b4])
    
    print(f"ROI coordinates: {b1, b2, b3, b4}")
    utils.grid("ROI image", roi_image, ' [px]')
    
    ### 6. ClASSIFICATION ###
    kmeansclass = kmean(dir)
    mean_curv, gauss_curv = wound.curvature(smooth)
    wound_curvature =  [np.mean(gauss_curv), np.mean(mean_curv)]
    data_test, label_test, centroides, labels_train = kmeansclass.fit_predict(wound_curvature)

    kmeansclass.dispersion(data_test, label_test, centroides, labels_train)

    print("Herida plana" if label_test==0 else "Herida tubular")

    ## 4. CALCULATION OF STITCHES ##
    # Straighten up the wound
    print(f"Wound inclination: {phi} º")

    (rows, cols) = injury.shape[:2]
    injury_center = (cols // 2, rows // 2)
    T = cv2.getRotationMatrix2D(injury_center, -phi, 1)
    v_injury = cv2.warpAffine(injury, T, (cols, rows))

    # Main diagonal of the wound
    top, bottom = wound.extremes(v_injury)
    print(f"top: {top}, bottom: {bottom}")

    # Depending on the result of the clasification, establish dist_stitches
    if label_test == 0: # flat wound
        dist_stitches = 1
    else:  # tubular wound
        dist_stitches = 0.5
    
    # Create the instance of the class stitches
    stitch = M4_stitches_module.Stitches(dist_stitches, px_scale)

    # Tool: endoestich -> 1 cm width
    tool_width = 1
    thin = stitch.is_thin(prop[0], tool_width)
    print("The wound is thin: " + str(thin))

    major_length = wound.major_len(top, bottom)
    separation = stitch.stitches_separation(major_length)

    # Coordinates of stitches in the diagonal of the wound
    stitches_point = stitch.thin_stitches(separation, major_length, top, bottom)
    print(f"Stitches in main diagonal in px: {stitches_point}")
    
    img_center = [w/2, h/2]
    reshape_center = np.shape(smooth)
    reshape_center = [reshape_center[1]/2, reshape_center[0]/2]

    # Represent thin stitches
    v_injury_line = cv2.cvtColor(v_injury, cv2.COLOR_GRAY2RGB)
    cv2.line(v_injury_line, top, bottom, (255, 0, 0), 2)
    utils.print_stitches(v_injury_line, stitches_point, injury_center, "Stitches in main diagonal in px", "blue", " [px]")

    # Calculation of gross stitches
    #print(f"injury paramenters: {np.shape(v_injury)}")
    #print(f"injury centroid: {prop[0].centroid}")
    if not thin:
        if label_test == 0: # flat wound
            suture_dist = 0.5
        else:  # tubular wound
            suture_dist = 1

        stitches_point = stitch.gross_stitches(v_injury, suture_dist, stitches_point)
        print(f"Stitches in suture line in px: {stitches_point}")

        # Represent gross stitches
        utils.print_stitches(v_injury_line, stitches_point, reshape_center, "Gross stitches in suture line", "red", " [px]")
    
    # Unroted the stitches coordinates
    T_inv = cv2.getRotationMatrix2D(injury_center, phi, 1)
    rot_stitches = cv2.transform(np.array([stitches_point]), T_inv)[0] 
    print(f"Rotated stitches: {rot_stitches}")

    # Representation of stitches well oriented
    utils.print_stitches(injury, rot_stitches, reshape_center, "Stitches original image", "blue", " [px]")

    ## Calculate the stitches in the original image
    stitches = []
    for s in rot_stitches:
        stitches.append([s[0] + OFFSET, s[1] + death_px + OFFSET])
    
    # Overlap the injury to the RGB image and the stitches
    img1 = color_image.astype(np.float32)
    img1 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    utils.print_stitches(img1, stitches, img_center, "RGB image with stitches", "red", " [px]")

    stitches_3D = []
    for s in stitches:
        aux = []
        aux.append(s[0])
        aux.append(s[1])
        aux.append(depth_image[s[1]][s[0]]/100)
        
        stitches_3D.append(aux)
    #print(stitches_3D)

    ## Change of reference system ##
    # Set the print options for homogeneous transformation matrix.
    np.set_printoptions(precision=4, suppress=True, floatmode='fixed')  

    refsys = M4_stitches_module.ReferenceSystem()

    # Change to the camera reference system
    Pcam = refsys.Tim2Tcam(utils, stitches_3D, img_center, px_scale)
    print(f"Pcam -> {Pcam}")    

    # Change the coordinates of the stitch points to the robot reference system R2.
    # Transformation from one robot to another
    TB1B2 = refsys.TB1B2(utils)
    #print(f"TB2B1 -> {TB2B1}")

    # Camera support parameters (cm)
    dz = 6-0.37
    dy = 4.1

    # Transform from R2 to camera
    TB2C = refsys.TB2C(utils, dy, dz)
    #print(f"TCE2 -> {TCE2}")

    # Stitches from the camera to R1
    PB1 = refsys.Pcam2B1(Pcam, TB2C, TB1B2)/100 # meters
    stitches_R1 = refsys.calib(utils, PB1)
    print("Puntos de sutura respecto de R1")
    print(f"PR1 -> {stitches_R1}") 

    # Adding the bias points to the final trayectory
    eta = 0.02 # 2 cm away from the surface to stretch the thread
    trayect = stitch.trayectory(stitches_R1, eta)

    final_trayectory = []
    for t in trayect:
        aux = []
        aux.append(float(t[0]))
        aux.append(float(t[1]))
        aux.append(float(t[2]))
        final_trayectory.append(aux)
    
    print("Complete trajectory with respect to R1")
    print(final_trayectory)

    ros_trayect = []
    for l in final_trayectory:
        ros_trayect.extend(l)
    """ print("Trayectory to send by ros")
    print(ros_trayect) """

    utils.grid_trayect(final_trayectory)

    utils.print_stitches(img1, stitches, img_center, "RGB image with stitches", "red", " [px]")

    # Quaternions calculation
    Q = stitch.quaternion(PB1, phi)
    #print(f"Quaternios: {Q}")

    # Store the depth_image in a file
    """ with open('Validación/V1_plana', 'w') as f:
        info = "pr = " + str(depth_image)
        f.write(info)
    f.close()  """ 
        

if __name__ == "__main__":
    #try:
    main()
    """ except:
        print('An error has ocurred')
    pass """
