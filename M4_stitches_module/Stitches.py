## Class stitches ##

import math
import cv2
import numpy as np
from pyquaternion import Quaternion

class Stitches:        

    """ Set parameters """
    def __init__(self, dist_stitches, px_scale):
        self.dist_stitches = dist_stitches
        self.SCALE = px_scale

    """ Type of wound depending on the suture tool """
    def is_thin(self, prop, tool_dist):
        thin = False
        wound_width = prop.minor_axis_length
        if wound_width < tool_dist*self.SCALE:
            thin = True
        return thin

    """ Stitches separation"""
    def stitches_separation(self, major_length):
        separation = []
        num_stitches = math.floor((major_length * self.SCALE)/self.dist_stitches)
        
        margen = major_length - ((num_stitches - 1)) * self.dist_stitches/self.SCALE
        separation.append(margen / 2)

        for i in range(1, num_stitches):
            new = separation[i-1] + self.dist_stitches/self.SCALE
            separation.append(new)
        return separation
    
    """ Calculation of the coordinates for thin wounds """
    def thin_stitches(self, separation, major_length, top, bottom):
        w = (bottom[0] - top[0], bottom[1] - top[1])
        num_stitches = len(separation)
        coor_stitches = []
        for i in range(0, num_stitches):
            x = top[0] + (separation[i]/major_length) * w[0]
            y = top[1] + (separation[i]/major_length) * w[1]
            x = int(round(x, 0))
            y = int(round(y, 0))
            coor_stitches.append([x, y])
        return coor_stitches

    """ Calculation of the coordinates for gross wounds """
    def gross_stitches(self, injury, suture_dist, coor_stitches):
        a = math.ceil(suture_dist/self.SCALE)
    
        kernel = np.ones((2*a, 2*a), np.uint8)
        suture_wound = cv2.dilate(injury, kernel, iterations=1)
        suture_line, _ = cv2.findContours(suture_wound, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
        
        suture_line = list(suture_line[0].tolist())

        gross_stitches = []
        
        for pto in range(0, len(coor_stitches)):
            # Detecting the left point
            i = round(coor_stitches[pto][0], 0)
            j = round(coor_stitches[pto][1], 0)
            found = False
            while (not found) and i > 0:
                try:
                    suture_line.index([[i, j]])
                    gross_stitches.append([i, j])
                    found = True
                except ValueError:
                    i = i - 1
                
            # Detecting the right point
            i = round(coor_stitches[pto][0], 0)
            j = round(coor_stitches[pto][1], 0)
            found = False
            lim = np.shape(injury)
            while (not found) and i < lim[1]:
                try:
                    suture_line.index([[i, j]])
                    gross_stitches.append([i, j])
                    found = True
                except ValueError:
                    i = i + 1
        return gross_stitches
    
    """ Adding the bias points to the trayectory """
    def trayectory(self, stitches, eta):
        trayectory = []
        for i in range(0, len(stitches)-1):
            trayectory.append(stitches[i])
            bias = np.zeros(3)
            bias[0] = (stitches[i][0] + stitches[i+1][0])/2
            bias[1] = (stitches[i][1] + stitches[i+1][1])/2
            bias[2] = (stitches[i][2] + stitches[i+1][2])/2 + eta
            trayectory.append(bias)
        trayectory.append(stitches[-1])
        return trayectory

    """ From cm point to quaternion parameters"""
    def quaternion (self, stitches, ori):
        Q = []
        for s in stitches:
            q = Quaternion(axis=s, angle=ori)
            Q.append([q.x, q.y, q.z, q.w])
        return Q


