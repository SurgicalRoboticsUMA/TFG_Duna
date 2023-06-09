import M2_processing_module.Utilities
import numpy as np

class ReferenceSystem:

    """ Initialise coordinate systems parameters """
    def __init__(self):
        # DH1 parameters for UR3 robots
        self.a = [0, -24.365, -21.325, 0, 0, 0] # cm
        self.d = [15.19, 0, 0, 11.235, 8.535, 8.19] # cm
        self.alfa = [np.pi/2, 0, 0, np.pi/2, -np.pi/2, 0] # rad
        self.theta = [0, 0, 0, 0, 0, 0] # rad

    """ From Ti (image) to Tc (camera in cm) """
    def Tim2Tcam(self, utils, stitches, center, px_scale):
        T = utils.desp([-center[0], -center[1], 0])
        Pcam_homog = np.hstack((stitches, np.ones((len(stitches), 1))))
        PB1_homog = np.dot(T, Pcam_homog.T)
        Ptos = PB1_homog[:3, :].T
        Ptos_cm = []
        for p in Ptos:
            aux = []
            aux.append(p[0]*px_scale)
            aux.append(p[1]*px_scale)
            aux.append(p[2])
            Ptos_cm.append(aux)
        return Ptos_cm
        
    """ Reference systems from R1 to R2 """
    def TB1B2(self, utils):
        # Matching the end-effectors of both robots
        #TR1R2 = TR1E1 * TE1E2 * inv(TR2E2)
        theta_r1 = np.deg2rad([-213.17, -96.74, -55.54, -28.07, 91.08, 359.14])
        theta_r2 = np.deg2rad([66.40, -146.36, -15.63, -17.57, 80.53, 0.86])

        TE2E1 = utils.rotY(np.pi)
        TB1E1 = utils.transformation(self.a, self.d, self.alfa, theta_r1)
        TB2E2 = utils.transformation(self.a, self.d, self.alfa, theta_r2)

        TB1B2 = TB1E1 @ TE2E1 @ np.linalg.inv(TB2E2)
        return TB1B2

    """ Camera position relative to robot 2 """
    def TB2C(self, utils, dy, dz):
        theta_cam = np.deg2rad([61.81, -166.95, -57.27, -55.81, 66.27, 18.10])
        TB2E2_c = utils.transformation(self.a, self.d, self.alfa, theta_cam)
        TB2C = TB2E2_c @ utils.desp([dy, 0, dz])@ utils.rotZ(-np.pi/2)
        return TB2C


    """ Conversion of the stitches from the camera to the robot 1 """
    def Pcam2B1(self, Pcam, TB2C, TB1B2):
        TB1C = TB1B2 @ TB2C 

        Pcam_homog = np.hstack((Pcam, np.ones((len(Pcam), 1))))
        PB1_homog = np.dot(TB1C, Pcam_homog.T)
        PB1 = PB1_homog[:3, :].T
        return PB1
    
    """ Calibration matrix """
    def calib(self, utils, S):
        Tcalib = utils.rotZ(np.pi) @ utils.desp([0.035, 0.009, -0.0162])

        Pcam_homog = np.hstack((S, np.ones((len(S), 1))))
        PB1_homog = np.dot(Tcalib, Pcam_homog.T)
        stitches = PB1_homog[:3, :].T
        return stitches

    
