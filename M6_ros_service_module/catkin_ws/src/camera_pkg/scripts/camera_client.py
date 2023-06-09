#!/usr/bin/env python

from __future__ import print_function
import cv2
import numpy as np
from sys import path

path.insert(0, '/home/labrob2022/Escritorio/CameraFeature')
# Local imports
import M1_acquisition_module
import M2_processing_module.Filters as filter
import M2_processing_module.Utilities
from M2_processing_module.nextNeighbour import next_neighbour
import M3_wound_detection_module.Wound as wound
import M4_stitches_module.Stitches
import M4_stitches_module.ReferenceSystem 
import M5_classifier_module.KmeanClassifier as kmean
import M6_ros_service_module


import rospy
from camera_pkg.srv import CameraData

def camera_client(num, stitches):
    rospy.wait_for_service('camera_data')
    try:
        camera = rospy.ServiceProxy('camera_data', CameraData)
        camera(num, stitches)

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
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

    ## 2. PROCESSING THE IMAGE ##
    # Reshaped the death pixels
    death_px = camera.death_zones(distance, w)
    OFFSET = 100
    reshaped = filter.reshape(depth_image, death_px)

    # Interpolate the null pixels
    corrected = filter.interpolate(reshaped)
    
    # Invert the matrix
    invert = filter.invert(corrected)
    
    # Smooth the image
    smooth = filter.smoothing(invert)

    # Apply gradient to the image
    gradient = filter.gradient(smooth)

    ## 3. DETECTING THE WOUND ##
    # Binarize the injury and 2D representation
    binary = wound.binaritation(gradient)
    binary = wound.no_border(binary)

    # Contours detected
    contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 

    # Detect the region with the major area and it's centroid
    injury, cx, cy = wound.detect_wound(binary)

    # Fill the wound detected knowing the centroid
    injury = wound.fill_area(injury, cx, cy)

    # Obtain propertires of the injury
    prop = wound.properties(injury)
    phi = prop[0].orientation

    ### 6. ClASSIFICATION ###
    # Adress of the datatrain for the classiffier
    dir = "/home/labrob2022/Escritorio/CameraFeature/M5_classifier_module"

    kmeansclass = kmean(dir)
    mean_curv, gauss_curv = wound.curvature(smooth)
    wound_curvature =  [np.mean(mean_curv), np.mean(gauss_curv)]
    label_test = kmeansclass.fit_predict(wound_curvature)

    ## 4. CALCULATION OF STITCHES ##
    # Straighten up the wound
    (rows, cols) = injury.shape[:2]
    injury_center = (cols // 2, rows // 2)
    T = cv2.getRotationMatrix2D(injury_center, -phi, 1)
    v_injury = cv2.warpAffine(injury, T, (cols, rows))

    # Main diagonal of the wound
    top, bottom = wound.extremes(v_injury)

    # Depending on the result of the clasification, establish dist_stitches
    if label_test: # flat wound
        dist_stitches = 1
    else:  # tubular wound
        dist_stitches = 0.5
    
    # Create the instance of the class stitches
    stitch = M4_stitches_module.Stitches(dist_stitches, px_scale)

    # Tool: endoestich -> 1 cm width
    tool_width = 1
    thin = stitch.is_thin(prop[0], tool_width)

    major_length = wound.major_len(top, bottom)
    separation = stitch.stitches_separation(major_length)

    # Coordinates of stitches in the diagonal of the wound
    stitches_point = stitch.thin_stitches(separation, major_length, top, bottom)    

    img_center = [w/2, h/2]
    reshape_center = np.shape(smooth)
    reshape_center = [reshape_center[1]/2, reshape_center[0]/2]

    # Calculation of gross stitches
    if not thin:
        if label_test == 0: # flat wound
            suture_dist = 0.5
        else:  # tubular wound
            suture_dist = 1

        stitches_point = stitch.gross_stitches(v_injury, suture_dist, stitches_point)
    
    num = len(stitches_point)

    # Unroted the stitches coordinates
    T_inv = cv2.getRotationMatrix2D(injury_center, phi, 1)
    rot_stitches = cv2.transform(np.array([stitches_point]), T_inv)[0] 
    
    ## Calculate the stitches in the original image
    stitches = []
    for s in rot_stitches:
        stitches.append([s[0] + OFFSET, s[1] + death_px + OFFSET])
    
    ## Calculate the 3D stitches ##
    stitches_3D = []
    for s in stitches:
        aux = []
        aux.append(s[0])
        aux.append(s[1])
        aux.append(depth_image[s[1]][s[0]]/100)
        
        stitches_3D.append(aux)

    ## Change of reference system ##
    # Set the print options for homogeneous transformation matrix.
    #np.set_printoptions(precision=4, suppress=True, floatmode='fixed')  

    refsys = M4_stitches_module.ReferenceSystem()

    # Change to the camera reference system
    w_cm = w * px_scale
    h_cm = h * px_scale

    Pcam = refsys.Tim2Tcam(stitches_3D, img_center, px_scale)

    # Change the coordinates of the stitch points to the robot reference system R2.
    # Transformation from one robot to another
    TB1B2 = refsys.TB1B2(utils)

    # Camera support parameters
    dz = 6-0.37
    dy = 4.1

    # Transform from R2 to camera
    TB2C = refsys.TB2C(utils, dy, dz)

    # Stitches from the camera to R1
    PB1 = refsys.Pcam2B1(Pcam, TB2C, TB1B2)/100 # meters
    stitches_R1 = refsys.calib(utils, PB1)

    # Adding the bias points to the final trayectory
    eta = 0.02 # 2 cm away from the surface to stretch the thread
    trayect = stitch.trayectory(PB1, eta)

    # Calculating the trayectory
    final_trayectory = []
    for t in trayect:
        aux = []
        aux.append(float(t[0]))
        aux.append(float(t[1]))
        aux.append(float(t[2]))
        final_trayectory.append(aux)

    # Preparing stitches to send
    stitches = []
    for l in final_trayectory:
        stitches.extend(l)

    camera_client(num, stitches)
    print("Sended!")
