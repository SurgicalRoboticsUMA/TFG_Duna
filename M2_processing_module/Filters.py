## Class Filters ##

# Libraries #
import re
import numpy as np
from M2_processing_module.nextNeighbour import next_neighbour
import cv2

class Filters:

    """ Reshape the matrix to eliminate depth pixels """
    def reshape(image, death_px):
        reshaped = []
        s = np.shape(image)
        # I add the 100 because of the set up conditions
        for i in range(death_px+100, s[0]):
            # To correctly detect tubular wounds I ajust this values to [i][280:s[1]-280]
            reshaped.append(image[i][280:s[1]-280])
        return reshaped

    
    """ Number of null pixels in the image """
    def null_px(matriz):
        contador = 0
        for fila in matriz:
            for pixel in fila:
                if pixel == 0:
                    contador += 1
        return contador

    """ Interpolate null pixel to the mean of the non nule neighborgs """
    def interpolate (matrix):
        corrected = matrix

        # First cell
        if matrix[0][0] == 0:
            v_bottom = next_neighbour(corrected, 0, 0, "bottom")
            v_right = next_neighbour(corrected, 0, 0, "right")

            m = np.mean([v_bottom, v_right])
            corrected[0][0] = m
        
        # First row
        j = 0
        colums = len(matrix)
        for i in range(1, colums):
            if matrix[i][j] == 0: 
                v_bottom = next_neighbour(corrected, i, j, "bottom")           
                v_right = next_neighbour(corrected, i, j, "right")
                v_left = corrected[i-1][j]

                m = np.mean([v_bottom, v_right, v_left])
                corrected[i][j] = m
        
        # First column
        i = 0
        rows = len(matrix[1])
        for j in range(1, rows):
            if matrix[i][j] == 0:
                v_top = corrected[i][j-1]
                v_bottom = next_neighbour(corrected, i, j, "bottom")
                v_right = next_neighbour(corrected, i, j, "right")

                m = np.mean([v_top, v_bottom, v_right])
                corrected[i][j] = m

        # Remainder of the matrix
        for j in range(1, rows):
            for i in range(1, colums):
                if matrix[i][j] == 0:
                    v_top = corrected[i][j-1]
                    v_bottom = next_neighbour(corrected, i, j, "bottom")
                    v_right = next_neighbour(corrected, i, j, "right")
                    v_left = corrected[i-1][j]

                    m = np. mean([v_top, v_bottom, v_right, v_left])
                    corrected[i][j] = m
        return corrected
    
    """ Invert the matrix in order to visualice z values the same as reality  """
    def invert (matrix):
        invert = np.max(matrix) - matrix
        return invert

    """ Apply gaussian filter for smoothing the image """
    def smoothing (matrix):
        smooth = cv2.GaussianBlur(matrix, (5,5), 5)
        return smooth

    """ Apply gradient filter to detect variations of depth """
    def gradient (matrix):
        sobelx = cv2.Sobel(matrix, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(matrix, cv2.CV_64F, 0, 1, ksize=5)

        # Calculate the gradient magnitude
        magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))

        # Re-scale between 0 and 1
        magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_8UC1)
        return magnitude
