#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    try:
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow("Camera View", cv_image)
        cv2.waitKey(1)
    except Exception as e:
        rospy.logerr(e)

def image_viewer():
    rospy.init_node('image_viewer', anonymous=True)
    rospy.Subscriber("camera/image_raw", Image, image_callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_viewer()
