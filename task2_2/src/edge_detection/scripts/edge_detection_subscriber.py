#!/usr/bin/env python3
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Fix for GUI issues
os.environ['QT_QPA_PLATFORM'] = 'xcb'

class EdgeDetectionSubscriber:
    def __init__(self):
        rospy.init_node('edge_detection_subscriber')
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('edge_detection', Image, self.image_callback)
        rospy.loginfo("Subscriber node ready")

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            cv2.imshow("Edge Detection", cv_image)
            cv2.waitKey(1)
        except CvBridgeError as e:
            rospy.logerr(f"Conversion error: {e}")
        except Exception as e:
            rospy.logerr(f"Display error: {e}")

if __name__ == '__main__':
    try:
        EdgeDetectionSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()
