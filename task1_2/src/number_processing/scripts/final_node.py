#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    result = data.data + 5
    rospy.loginfo("Final result: %d + 5 = %d", data.data, result)

def final_node():
    rospy.init_node('final_node')
    rospy.Subscriber('/processed_numbers', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    final_node()
