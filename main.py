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
    #plt.title("Depth colormap", fontdict = {'fontsize' : 30})

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

    ## 2. PROCESSING THE IMAGE ##
    # Reshaped the death pixels
    death_px = camera.death_zones(distance, w)
    reshaped = filter.reshape(depth_image, death_px)
    utils.grid('Reshaped image', reshaped, ' [px]')

    # Validate the quality of the image
    null = filter.null_px(reshaped)
    total_px = w * h
    print(f"Null pixels (%): {round(null*100/total_px, 2)} %")
   
    # Interpolate the null pixels
    corrected = filter.interpolate(reshaped)
    utils.grid('Corrected image', corrected, ' [px]')
    
    # Invert the matrix
    invert = filter.invert(corrected)
    utils.grid('Invert image', invert, ' [px]')
    
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
    original_ori = prop[0].orientation

    # ROI image
    b1, b2, b3, b4 = wound.roi_coor(injury, prop[0])
    roi_image = []
    for x in range(b1, b3):
        roi_image.append(smooth[x][b2:b4])
    
    print(f"ROI coordinates: {b1, b2, b3, b4}")
    utils.grid("ROI image", roi_image, ' [px]')

    #Colision mesh
    [Xr, Yr, Zr] = wound.colision_mesh(roi_image, px_scale)
    """ n = len(Xr)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for k in range(n):
        ax.scatter(Xr[k], Yr[k], Zr[k], c='b', marker='.')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show() """
    
    ### 6. ClASSIFICATION ###
    # Adress of the datatrain for the classiffier
    #dir = "/home/duna/Escritorio/TFG sutura quirurgica/UMA_MallaColisiones/PYTHON/CameraFeature/M5_classifier_module"
    dir = "/home/labrob2022/Desktop/UMA_MallaColisiones/PYTHON/CameraFeature/M5_classifier_module"

    kmeansclass = kmean(dir)
    mean_curv, gauss_curv = wound.curvature(smooth)
    wound_curvature =  [np.mean(mean_curv), np.mean(gauss_curv)]
    label_test = kmeansclass.fit_predict(wound_curvature)

    print("Herida plana" if label_test==0 else "Herida tubular")

    ## 4. CALCULATION OF STITCHES ##
    # Straighten up the wound
    phi = original_ori
    print(f"Wound inclination: {phi} º")

    (rows, cols) = injury.shape[:2]
    center = (cols // 2, rows // 2)
    T = cv2.getRotationMatrix2D(center, -phi, 1)
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
    
    # Represent thin stitches
    v_injury_line = cv2.cvtColor(v_injury, cv2.COLOR_GRAY2RGB)
    cv2.line(v_injury_line, top, bottom, (255, 0, 0), 2)
    utils.print_stitches(v_injury_line, stitches_point, "Stitches in main diagonal in px", "blue", " [px]")

    # Calculation of gross stitches
    print(f"injury paramenters: {np.shape(v_injury)}")
    print(f"injury centroid: {prop[0].centroid}")
    if not thin:
        if label_test == 0: # flat wound
            suture_dist = 0.5
        else:  # tubular wound
            suture_dist = 1

        stitches_point = stitch.gross_stitches(v_injury, suture_dist, stitches_point)
        print(f"Stitches in suture line in px: {stitches_point}")

        # Represent gross stitches
        utils.print_stitches(v_injury_line, stitches_point, "Gross stitches in suture line", "red", " [px]")
    
    # Unroted the stitches coordinates
    T_inv = cv2.getRotationMatrix2D(center, phi, 1)
    rot_stitches = cv2.transform(np.array([stitches_point]), T_inv)[0] 
    print(f"Rotated stitches: {rot_stitches}")

    # Representation of stitches well oriented
    utils.print_stitches(injury, rot_stitches, "Stitches original image", "blue", " [px]")

    # Overlap the injury to the RGB image and the stitches
    img1 = color_image.astype(np.float32)
    img1 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    img1 = filter.reshape(img1, death_px)

    utils.print_stitches(img1, rot_stitches, "RGB image with stitches", "red", " [px]")

    ## Change of reference system ##
    # Set the print options for homogeneous transformation matrix.
    np.set_printoptions(precision=4, suppress=True, floatmode='fixed')  

    refsys = M4_stitches_module.ReferenceSystem()

    # Change to the camera reference system
    w_cm = w * px_scale
    h_cm = h * px_scale

    Pcam = refsys.Tim2Tcam(depth_image, rot_stitches, w_cm, h_cm, px_scale)    

    # Change the coordinates of the stitch points to the robot reference system R2.
    # Transformation from one robot to another
    TR1R2 = refsys.TR1R2(utils)

    # Camera support parameters
    dz = 5.5-0.37
    dy = 3.6

    # Transform from R2 to camera
    TR2C = refsys.TR2cam(utils, dy, dz)

    # Stitches from the camera to R1
    PR1 = refsys.Pcam2PR1(utils, Pcam, TR2C, TR1R2)
    print("Puntos de sutura respecto de R1")
    print(PR1)

    # Adding the bias points to the final trayectory
    eta = 2 # 2 cm away from the surface to stretch the thread
    trayect = stitch.trayectory(PR1, eta)
    print("Trayectoria completa respecto de R1")
    print(trayect)

    # Quaternions calculation
    Q = stitch.quaternion(PR1, original_ori)
    print(f"Quaternios: {Q}")

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