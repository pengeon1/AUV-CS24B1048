#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

pub = None

def callback(data):
    processed_number = data.data * 10
    rospy.loginfo("Processing: %d -> %d", data.data, processed_number)
    pub.publish(processed_number)

def number_processor():
    global pub
    rospy.init_node('number_processor')
    pub = rospy.Publisher('/processed_numbers', Int32, queue_size=10)
    rospy.Subscriber('/numbers', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    number_processor()
