#!/usr/bin/env python3
import rospy
from chat_pkg.msg import ChatMessage

class ChatNode:
    def __init__(self, username):
        self.username = username
        rospy.init_node('chat_node', anonymous=True)
        self.pub = rospy.Publisher('chat_topic', ChatMessage, queue_size=10)
        rospy.Subscriber('chat_topic', ChatMessage, self.receive_message)
        rospy.loginfo(f"{self.username} joined the chat. Type 'exit' to quit.")

    def receive_message(self, msg):
        if msg.sender != self.username:
            print(f"[{msg.sender}] {msg.message}")

    def send_message(self, text):
        msg = ChatMessage()
        msg.sender = self.username
        msg.message = text
        self.pub.publish(msg)

    def run(self):
        while not rospy.is_shutdown():
            message = input("> ")
            if message.lower() == 'exit':
                break
            self.send_message(message)

if __name__ == '__main__':
    print("Enter your name: ",end='')
    name = input().strip()
    chat_node = ChatNode(name)
    chat_node.run()
