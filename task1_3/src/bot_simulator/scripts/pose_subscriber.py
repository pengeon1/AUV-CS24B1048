#!/usr/bin/env python3
import rospy
from bot_simulator.msg import bot_pose

class PoseTracker:
    def __init__(self):
        rospy.init_node('pose_tracker')
        rospy.Subscriber('bot_pose', bot_pose, self.pose_callback)
        self.current_pose = None
        
    def pose_callback(self, data):
        self.current_pose = data
        self.print_pose()
        
    def print_pose(self):
        if self.current_pose:
            print("\n--- BOT STATUS ---")
            print(f"Position: ({self.current_pose.x:.1f}, {self.current_pose.y:.1f})")
            print(f"Facing: {self.current_pose.facing.upper()}")
            print("-----------------")

if __name__ == '__main__':
    tracker = PoseTracker()
    print("Waiting for updates...")
    rospy.spin()
