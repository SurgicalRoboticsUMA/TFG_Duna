## Class Utilities ##

# Libraries #
#import pyrealsense2 as rs
import math
import numpy as np
import pyrealsense2  as rs
import cv2
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits import mplot3d
import random
from matplotlib import cm, colors


class Utilities:
    
    """ From pixel to point 3D """
    def pixel2point (self, aligned_depth_frame, intr, pixel):
        # Inicialice the 3D point
        pto1 = []

        # Obtain the depth of the pixels with the function get_distance
        z1 = aligned_depth_frame.get_distance(pixel[0] , pixel[1])

        # Deproject from pixel to point in 3D
        pto1 = rs.rs2_deproject_pixel_to_point(intr, pixel, z1)

        return pto1
    
    """ From point 3D to pixel """
    def point2pixel (self, intr, point):

        # Project the point to obtain the pixel
        pixel = rs.rs2_project_point_to_pixel(intr, point) 

        return pixel

    """ Distance between 2 pixels """
    def distance_px (self, aligned_depth_frame, intr, pixel1, pixel2):
        
        # Inicialice the 3D points
        pto1 = []
        pto2 = []

        # Obtain the depth of the pixels with the function get_distance
        z1 = aligned_depth_frame.get_distance(pixel1[0] , pixel1[1])
        z2 = aligned_depth_frame.get_distance(pixel2[0] , pixel2[1])

        # Deproject from pixel to point in 3D
        pto1 = rs.rs2_deproject_pixel_to_point(intr, pixel1, z1)
        pto2 = rs.rs2_deproject_pixel_to_point(intr, pixel2, z2)

        dist = math.sqrt((math.pow(pto1[0]-pto2[0],2)) + (math.pow(pto1[1]-pto2[1],2)) + (math.pow(pto1[2]- pto2[2],2)))
        return dist, pto1, pto2
    
    """ Obtain the px_scale factor """
    def px_scale_calculator(self, aligned, intr, w, h):
        pixels_x = random.sample(range(w - 30), 20) 
        pixels_y = random.sample(range(h), 20)
        distances = []
        for i in range(0, 10):
            # Calculates the distance between each pair of selected pixels
            p1 = [pixels_x[i], pixels_y[i]]
            p2 = [(pixels_x[i] + 30), pixels_y[i]]
            distance = self.distance_px(aligned, intr, p1, p2)[0]
            if distance != 0:
                distances.append(distance)
                
        # Calculate the median of the distances   
        px_scale = np.median(distances) * 100 / 30  
        return px_scale
    
    """ Representing the 3D surface """
    def grid(self, title, image, unit):
        ax = plt.axes(projection="3d")

        z = np.array(image)
        y = np.arange(len(z))
        x = np.arange(len(z[0]))

        (x, y) = np.meshgrid(x, y)

        X = 'X' + unit
        Y = 'Y' + unit
        Z = 'Z' + ' [cm]'

        ax.plot_surface(x, y, z/100)
        ax.set_xlabel(X, labelpad=15)
        ax.set_ylabel(Y, labelpad=15)
        ax.set_zlabel(Z, labelpad=15)

        plt.title(title, fontdict = {'fontsize' : 30})
        plt.show()

    """ Representing the gradient surface """
    def grid_gradient(self, title, image, unit):
        ax = plt.axes(projection="3d")

        z = np.array(image)
        y = np.arange(len(z))
        x = np.arange(len(z[0]))

        (x, y) = np.meshgrid(x, y)

        X = 'X' + unit
        Y = 'Y' + unit
        Z = 'Z' + ' [1/cm]'

        ax.plot_surface(x, y, z)
        ax.set_xlabel(X, labelpad=15)
        ax.set_ylabel(Y, labelpad=15)
        ax.set_zlabel(Z, labelpad=15)
        plt.title(title, fontdict = {'fontsize' : 30})
        plt.show()
        
    """ Representation of 2D images """
    def surf(self, title, image, unit):
        plt.imshow(image, cmap = matplotlib.colors.ListedColormap(['black', 'white']))

        X = 'X' + unit
        Y = 'Y' + unit

        plt.xlabel(X, fontdict = {'fontsize' : 25})
        plt.ylabel(Y, fontdict = {'fontsize' : 25})
        plt.title(title, fontdict = {'fontsize' : 30})
        plt.show()
        
    """ Representing stitches """
    def print_stitches(self, injury, stitches, title, c, unit):
        
        plt.imshow(injury, cmap = colors.ListedColormap(['black', 'white']))
        for p in stitches:
            plt.scatter(p[0], p[1], color=c, s=20)

        X = 'X' + unit
        Y = 'Y' + unit

        plt.xlabel(X, fontdict = {'fontsize' : 25})
        plt.ylabel(Y, fontdict = {'fontsize' : 25})
        plt.title(title, fontdict = {'fontsize' : 30})
        plt.show()

    """ Representing 2D image """
    """ def surface(self, title, image):
        img = np.asarray(image)
        img = img.astype(np.uint8)
        cv2.imshow(title, img)
        cv2.waitKey(0) """

    def surface(self, title, image, unit):
        img = np.asarray(image)
        img = img.astype(np.uint8)

        X = 'X' + unit
        Y = 'Y' + unit
        plt.imshow(img)
        plt.xlabel(X, fontdict = {'fontsize' : 25})
        plt.ylabel(Y, fontdict = {'fontsize' : 25})
        plt.title(title, fontdict = {'fontsize' : 30})
        plt.show()

    """ Generating the colorbar for colormaps """
    def colorbar(self, lista_colores = ["#fe3400", "#ff6000", "#ff6d00", "#FF9D00" ,
                                        "#ffd100", "#fff400", "#e0ff1d", "#a6ff57" ,
                                        "#83FF7A" , "#65ff98","#22ffdb", "#00f4ff",
                                        "#00B7FF", "#0092ff", "#0026ff", "#0000CD",
                                        "#000081", "#000057"]):
        colores_nuevos = []
        
        for i in range(len(lista_colores) - 1):
            color_inicio = lista_colores[i]
            color_final = lista_colores[i + 1]
            
            r_inicio, g_inicio, b_inicio = int(color_inicio[1:3], 16), int(color_inicio[3:5], 16), int(color_inicio[5:7], 16)
            r_final, g_final, b_final = int(color_final[1:3], 16), int(color_final[3:5], 16), int(color_final[5:7], 16)
            
            r = math.floor((r_final + r_inicio) / 2)
            g = math.floor((g_final + g_inicio) / 2)
            b = math.floor((b_final + b_inicio) / 2)
            
            color_intermedio = f"#{r:02X}{g:02X}{b:02X}"

            colores_nuevos.append(color_inicio)
            colores_nuevos.append(color_intermedio)
        colores_nuevos.append(lista_colores[len(lista_colores)-1])
        
        return colores_nuevos
    
    """ Make the color bar smooth """
    def gradient_colorbar(self, num=5):
        lista = self.colorbar()
        for i in range(num - 1):
            lista = self.colorbar(lista)
        return lista

    """ Rotation in X """
    def rotX(self, theta):
        s = np.sin(theta)
        c = np.cos(theta)
        if isinstance(theta, (int, float)):
            if abs(c) < 1e-10:
                c = 0
            if abs(s) < 1e-10:
                s = 0
        RX = [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]
        return np.array(RX)

    """ Rotation in Z """
    def rotZ(self, theta):
        s = np.sin(theta)
        c = np.cos(theta)
        if isinstance(theta, (int, float)):
            if abs(c) < 1e-10:
                c = 0
            if abs(s) < 1e-10:
                s = 0
        RZ = [[c,-s,0,0], [s,c,0,0], [0,0,1,0], [0, 0, 0, 1]]
        return np.array(RZ)

    """ Displacement """
    def desp(self, p):
        D = [[1, 0, 0, p[0]], [0, 1, 0, p[1]], [0, 0, 1, p[2]], [0, 0, 0, 1]]
        return np.array(D)

    """ From pixel to point without the aling """
    def image2camara(self, px, T):
        pto = np.array([[px[0]], [px[1]], [0], [1]])
        P = T @ pto
        return P.tolist()
    
    """ Transformation matrix """
    def transformation(self, a, d, alfa, theta):           
        T01 = self.desp([0, 0, d[0]]) @ self.rotZ(theta[0]) @ self.desp([a[0], 0, 0]) @ self.rotX(alfa[0])
        T12 = self.desp([0, 0, d[1]]) @ self.rotZ(theta[1]) @ self.desp([a[1], 0, 0]) @ self.rotX(alfa[1])
        T23 = self.desp([0, 0, d[2]]) @ self.rotZ(theta[2]) @ self.desp([a[2], 0, 0]) @ self.rotX(alfa[2])
        T34 = self.desp([0, 0, d[3]]) @ self.rotZ(theta[3]) @ self.desp([a[3], 0, 0]) @ self.rotX(alfa[3])
        T45 = self.desp([0, 0, d[4]]) @ self.rotZ(theta[4]) @ self.desp([a[4], 0, 0]) @ self.rotX(alfa[4])
        T56 = self.desp([0, 0, d[5]]) @ self.rotZ(theta[5]) @ self.desp([a[5], 0, 0]) @ self.rotX(alfa[5])
        T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
        
        return T06



    