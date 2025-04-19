#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def number_publisher():
    rospy.init_node('number_publisher')
    pub = rospy.Publisher('/numbers', Int32, queue_size=10)
    rate = rospy.Rate(1)
    
    count = 0
    while not rospy.is_shutdown():
        number = count * 2
        rospy.loginfo("Publishing: %d", number)
        pub.publish(number)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        number_publisher()
    except rospy.ROSInterruptException:
        pass
