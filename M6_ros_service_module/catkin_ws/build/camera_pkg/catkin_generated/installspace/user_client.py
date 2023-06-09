#!/usr/bin/env python3

from __future__ import print_function

import rospy
from camera_pkg.srv import UserReq

def user_client():
    rospy.wait_for_service('user_req')
    try:
        user_req = rospy.ServiceProxy('user_req', UserReq)
        resp = user_req()
        resp = {
            "num": resp.num,
            "stitches": resp.stitches,
            }
        return resp
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    print("Requesting stitches")
    resp = user_client()
    print(resp)
    print('hola')