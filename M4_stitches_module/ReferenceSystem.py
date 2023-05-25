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
    def Tim2Tcam(self, smooth, rot_stitches, w, h,px_scale):
        Tc = np.eye(4)
        Tc[:3,3] = np.array([w/2, h/2, 0])

        # Convert the Pi stitches to the reference system of the Pcam camera.
        Pcam = np.empty((0, 3))

        for i in range(len(rot_stitches)):
            Paux = np.append(rot_stitches[i]*px_scale, [smooth[rot_stitches[i][0]][rot_stitches[i][1]]/10, 1])
            Taux = np.dot(Tc, Paux)
            Taux = Taux[:3]
            Pcam = np.vstack([Pcam, Taux])
        return Pcam
        
    """ Reference systems from R1 to R2 """
    def TR1R2(self, utils):
        # Matching the end-effectors of both robots
        #TR1R2 = TR1E1 * TE1E2 * inv(TR2E2)
        theta_r1 = np.deg2rad([46.71, -134.1, -43.9, -3.11, 90.1, 105.64])
        theta_r2 = np.deg2rad([-44.88, -74.38, 52.18, -159.45, -87.43, 2.49])

        TE1E2 = utils.rotX(np.pi) @ utils.rotZ(-np.pi/2)
        TR1E1 = utils.transformation(self.a, self.d, self.alfa, theta_r1)
        TR2E2 = utils.transformation(self.a, self.d, self.alfa, theta_r2)

        TR1R2 = TR1E1 @ TE1E2 @ np.linalg.inv(TR2E2)
        return TR1R2

    """ Camera position relative to robot 2 """
    def TR2cam(self, utils, dy, dz):
        theta_cam = np.deg2rad([53.78, -171.82, -47.15, -51.88, 90.77, 3.47])
        TR2E2_c = utils.transformation(self.a, self.d, self.alfa, theta_cam)
        TR2C = TR2E2_c @ utils.desp([0, -dy, dz])@ utils.rotZ(np.pi/2)
        return TR2C

    """ Conversion of the stitches from the camera to the robot 1 """
    def Pcam2PR1(self, utils, Pcam, TR2C, TR1R2):
        # Coordinates of the stitch points in the reference frame of the base of R2
        Pcam_homog = np.hstack((Pcam, np.ones((len(Pcam), 1))))
        PR2_homog = np.dot(TR2C, Pcam_homog.T)
        PR2 = PR2_homog[:3, :].T

        # Coordinates of the stitch points in the R1 reference system
        T_calib1 = utils.rotZ(-np.pi/2)
        TR1R2_c = T_calib1 @ TR1R2
        PR2_homog = np.hstack((PR2, np.ones((len(PR2), 1))))
        PR1_homog = np.dot(TR1R2_c, PR2_homog.T)
        PR1 = PR1_homog[:3, :].T

        T_calib2 = utils.desp([-67.8, 0, 0])
        PR1_homog = np.hstack((PR1, np.ones((len(PR1), 1))))
        PR1_desp_homog = T_calib2 @ PR1_homog.T
        PR1_desp = PR1_desp_homog[:3, :].T
        return PR1_desp
