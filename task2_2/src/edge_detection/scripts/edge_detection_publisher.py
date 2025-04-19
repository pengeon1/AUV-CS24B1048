#!/usr/bin/env python3
import rospy
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class EdgeDetectionPublisher:
    def __init__(self):
        rospy.init_node('edge_detection_publisher')
        self.bridge = CvBridge()
        self.edge_pub = rospy.Publisher('edge_detection', Image, queue_size=10)
        self.camera_index = 0
        self.cap = None
        self.setup_camera()

    def setup_camera(self):
        """Initialize camera with retry logic"""
        max_attempts = 3
        for attempt in range(max_attempts):
            self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_V4L2)
            if self.cap.isOpened():
                # Configure camera
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
                rospy.loginfo(f"Camera initialized at index {self.camera_index}")
                return
            else:
                rospy.logwarn(f"Camera open attempt {attempt + 1} failed")
                time.sleep(1)
        
        rospy.logerr("Could not initialize camera!")
        exit(1)

    def reconnect_camera(self):
        """Re-establish camera connection"""
        rospy.logwarn("Attempting camera reconnection...")
        self.cap.release()
        time.sleep(1)
        self.setup_camera()

    def run(self):
        rate = rospy.Rate(30)  # 30Hz
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if not ret:
                rospy.logerr("Frame capture failed!")
                self.reconnect_camera()
                continue

            try:
                # Edge detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 100, 200)
                edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
                
                # Publish
                self.edge_pub.publish(self.bridge.cv2_to_imgmsg(edges_bgr, "bgr8"))
            except Exception as e:
                rospy.logerr(f"Processing error: {e}")
                continue

            rate.sleep()

if __name__ == '__main__':
    try:
        EdgeDetectionPublisher().run()
    except rospy.ROSInterruptException:
        if hasattr(EdgeDetectionPublisher, 'cap'):
            EdgeDetectionPublisher.cap.release()
