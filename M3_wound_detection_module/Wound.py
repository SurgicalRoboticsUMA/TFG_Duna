## Class Wound ##

import cv2
from skimage import measure
import numpy as np
import math
from scipy.signal import decimate

class Wound:

    """ Binaritation of the image """
    def binaritation(image):
        # Preprocessing the image
        kernel = np.ones((5,5), np.uint8)
        injury = cv2.dilate(image, kernel, iterations=10) 
        injury = cv2.erode(injury, kernel, iterations=10) 
        injury = cv2.dilate(injury, kernel, iterations=1) 

        _, binary = cv2.threshold(injury, 0.5, 255, cv2.THRESH_BINARY)
        return binary

    """ Delete border regions (useful for tubular wounds) """
    def no_border(binary):
        # Add 1 pixel white border all around
        pad = cv2.copyMakeBorder(binary, 1,1,1,1, cv2.BORDER_CONSTANT, value=255)
        h, w = pad.shape

        # Create zeros mask 2 pixels larger in each dimension
        mask = np.zeros([h + 2, w + 2], np.uint8)

        # Floodfill outer white border with black
        img_floodfill = cv2.floodFill(pad, mask, (0,0), 0, (5), (0), flags=8)[1]

        # Remove border
        binary_floodfill = img_floodfill[1:h-1, 1:w-1]
        
        return binary_floodfill
        
    """ Detect maximum area region """
    def detect_wound(binary):
        # Detect the region with more area to eliminate persistent noises
        label_img = measure.label(binary)
        regions = measure.regionprops(label_img)
        
        # Detect max area
        maxArea = 0
        for r in regions:
            if r.area > maxArea:
                maxArea = r.area
        
        # Obtain the index of the max area region
        finded = False
        i = 0
        while not(finded) and i < len(regions):
            if regions[i].area == maxArea:
                finded = True
            i = i + 1  
        
        # Select the region with the maxArea
        mask = np.zeros_like(binary, dtype=np.uint8)
        mask[label_img == i] = 255
        injury = cv2.bitwise_and(binary, binary, mask=mask)

        # Centroid of the injury
        [cx, cy] = regions[i-1].centroid

        return injury, cx, cy

    """ Fill the region detected """
    def fill_area (injury, cx, cy):
        # Fill the injury
        mask = np.zeros((injury.shape[0]+2, injury.shape[1]+2), dtype=np.uint8)
        cv2.floodFill(injury, mask, (round(cy), round(cx)), 255)  
        return injury

    """ Properties of the injury """
    def properties (injury):
        prop = measure.regionprops(injury)
        return prop

    """ Rotation matrix """
    def rotation(matrix, T):
        new = []
        for s in matrix:
            pto = np.array([[s[0]], [s[1]], [0], [1]])
            P = (T @ pto).tolist()            
            new.append([int(round(P[0][0], 0)), int(round(P[1][0], 0))])
        return new

    """ Straighten up the wound (vertical) """
    def vertical(injury, img_param, prop):
        # Calculate the matrix rotation
        center = (img_param['width'] // 2, img_param['height'] // 2)
        angle =  -prop[0].orientation *180/np.pi # Oposite angle to wound inclination
        scale = 1.0
        M = cv2.getRotationMatrix2D(center, angle, scale)

        # Apply the rotation to the image
        rotated = cv2.warpAffine(injury, M, (img_param['width'], img_param['height'])) 
       
        return rotated
    
    """ Un-straighten up the wound (original inclination) """
    def non_vertical(injury, img_param, original_ori):
        # Calculate the rotation matrix
        center = (img_param['width'] // 2, img_param['height'] // 2)
        angle =  original_ori *180/np.pi
        scale = 1.0
        M = cv2.getRotationMatrix2D(center, angle, scale)

        # Apply the rotation to the image
        rotated = cv2.warpAffine(injury, M, (img_param['width'], img_param['height'])) 
       
        return rotated

    """ Obtain the ROI of the image """
    def roi_coor (injury, prop):
        s = np.shape(injury)
        
        # Injury parameters
        aa = prop.major_axis_length
        bb = prop.minor_axis_length

        centroidx, centroidy = prop.centroid

        # up left x pixel
        if (centroidx - 3 * bb) > 0:
            b1 = centroidx - 3 * bb
        else:
            b1 = 1
        
        # up left y pixel
        if (centroidy - 2 *aa) > 0:
            b2 = centroidy - 2 * aa
        else:
            b2 = 1
        
        # bottom right x pixel
        if (centroidx + 3 * bb) < s[1]:
            b3 = centroidx + 3 * bb
        else:
            b3 = s[0]
        
        # bottom right y pixel
        if (centroidy + 2 * aa) < s[0]:
            b4 = centroidy + 2 * aa
        else:
            b4 = s[1]           
        return round(b1), round(b2), round(b3), round(b4)
    #cv2.rectangle(image, px_sup_izq, px_inf_der, color, thickness)

    """ Extremes of the wound """ 
    def extremes(injury):
        # Get the non-zero rows and columns
        rows, cols = np.nonzero(injury)
        
        # Find the top and bottom pixels
        top = (cols[rows.argmin()], rows.min())
        bottom = (cols[rows.argmax()], rows.max())
        return top, bottom

    """ Major diagonal lenght """
    def major_len(top, bottom):
        return math.sqrt((top[1] - bottom[1])**2 + (top[0] - bottom[0])**2)
    
    """ Curvature """
    def curvature(image):
        Zy, Zx  = np.gradient(image)
        Zxy, Zxx = np.gradient(Zx)
        Zyy, _ = np.gradient(Zy)

        # Mean curvature
        M = (Zx**2 + 1)*Zyy - 2*Zx*Zy*Zxy + (Zy**2 + 1)*Zxx
        M = -M/(2*(Zx**2 + Zy**2 + 1)**(1.5))

        # Gaussian curvature
        G = (Zxx * Zyy - (Zxy ** 2)) /  (1 + (Zx ** 2) + (Zy **2)) ** 2
        
        return M, G
    
    """ Colision mesh """
    def colision_mesh (roi_image, px_scale):
        s = np.shape(roi_image)  
        mesh = []
        for i in range(s[0]):
            for j in range(s[1]):
                z = roi_image[i][j]/10
                x = i * px_scale
                y = j * px_scale
                mesh.append([round(x, 3), round(y, 3), round(z, 3)])
        
        # Downsampling the mesh
        Xr = []
        Yr = []
        Zr = []
        for i in mesh:
            Xr.append(i[0])
            Yr.append(i[1])
            Zr.append(i[2])

        Xr = decimate(Xr, 12)
        Yr = decimate(Yr, 12)
        Zr = decimate(Zr, 12)
        
        return [Xr, Yr, Zr]
        


