#!/usr/bin/env python3
import rospy
from bot_simulator.msg import bot_pose

class BotCommander:
    def __init__(self):
        rospy.init_node('bot_commander')
        self.pose_pub = rospy.Publisher('bot_pose', bot_pose, queue_size=10)
        
        self.x = 0.0
        self.y = 0.0
        self.facing = "NORTH"
        self.state = "idle" 
        self.move_timer = None
        self.step_size = 1.0
        self.move_rate = rospy.Rate(1) 
        
        self.pub_timer = rospy.Timer(rospy.Duration(0.1), self.publish_pose)
        
    def publish_pose(self, event=None):
        pose = bot_pose()
        pose.x = self.x
        pose.y = self.y
        pose.facing = self.facing
        self.pose_pub.publish(pose)
        
    def move_forward(self):
        if self.facing == "NORTH":
            self.y += self.step_size
        elif self.facing == "SOUTH":
            self.y -= self.step_size
        elif self.facing == "EAST":
            self.x += self.step_size
        elif self.facing == "WEST":
            self.x -= self.step_size
            
    def auto_move(self, event):
        if self.state == "moving":
            self.move_forward()
            self.publish_pose()
            
    def process_command(self, command):
        command = command.lower().strip()
        
        if command == "start":
            if self.state != "moving":
                self.state = "moving"
                self.move_timer = rospy.Timer(rospy.Duration(1), self.auto_move)
                return True
                
        elif command == "stop":
            if self.state == "moving":
                if self.move_timer:
                    self.move_timer.shutdown()
                self.state = "idle"
                return True
                
        elif command == "l":
            if self.facing == "NORTH":
                self.facing = "WEST"
            elif self.facing == "WEST":
                self.facing = "SOUTH"
            elif self.facing == "SOUTH":
                self.facing = "EAST"
            elif self.facing == "EAST":
                self.facing = "NORTH"
            return True
            
        elif command == "r":
            if self.facing == "NORTH":
                self.facing = "EAST"
            elif self.facing == "EAST":
                self.facing = "SOUTH"
            elif self.facing == "SOUTH":
                self.facing = "WEST"
            elif self.facing == "WEST":
                self.facing = "NORTH"
            return True
            
        elif command == "exit":
            rospy.signal_shutdown("User requested exit")
            return True
            
        return False
        
    def run(self):
        print("Bot_Simulator")
        print("Commands: start, stop, l, r, exit")
        
        while not rospy.is_shutdown():
            try:
                command = input("Enter command: ")
                if not self.process_command(command):
                    print("Invalid command. Try again.")
            except (EOFError, KeyboardInterrupt):
                break
            except Exception as e:
                rospy.logerr(f"Error: {e}")

if __name__ == '__main__':
    try:
        commander = BotCommander()
        commander.run()
    except rospy.ROSInterruptException:
        pass
