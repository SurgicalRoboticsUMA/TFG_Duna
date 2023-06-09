#!/usr/bin/env python

from __future__ import print_function

from camera_pkg.srv import CameraData, CameraDataResponse, UserReq, UserReqResponse
import rospy
from threading import Lock

mutex = Lock() #To avoid concurrecy issues
container = {
            "num": 0,
            "stitches": [],
            }

def handle_camera_data(req):
    mutex.acquire() # Ensures that the variable is only being written 
    global container
    container["num"] = req.num
    container["stitches"] = req.stitches
    mutex.release()
    
    print("Correctly received data")
    return CameraDataResponse()

def handle_user_req(req):
    print("Sending data...")
    mutex.acquire() # Ensures that the variable is only being read
    res = UserReqResponse(container["num"], container["stitches"])
    mutex.release()

    print('Sended!')
    return res

def camera_server():
    rospy.init_node('camera_server')

    rospy.Service('camera_data', CameraData, handle_camera_data)
    print("Ready to receive stitches")

    rospy.Service('user_req', UserReq, handle_user_req)
    print("Ready to send stitches")

    rospy.spin()

if __name__ == "__main__":
    camera_server()
