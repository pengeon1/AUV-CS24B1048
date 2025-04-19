#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def camera_publisher():
    rospy.init_node('camera_publisher', anonymous=True)
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)
    
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Failed to capture frame")
            break
            
        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(msg)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        rate.sleep()
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass
