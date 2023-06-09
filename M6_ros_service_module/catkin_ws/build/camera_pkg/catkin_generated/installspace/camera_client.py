#!/usr/bin/env python3

from __future__ import print_function
from sys import path

path.insert(0, '/home/labrob2022/Escritorio/CameraFeature')
from M6_ros_service_module import main_vbox

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
    num, stitches = main_vbox()
    camera_client(num, stitches)
