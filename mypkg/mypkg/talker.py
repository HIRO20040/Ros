import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

rclpy.init()
node = Node("battery")
pub = node.create_publisher(Int16, "battery", 10)
n = 0



def cb():
    global n
    msg = Int16()
    msg.data = int(random.uniform(10.0, 100.0))
    pub.publish(msg)
    

def main():
        node.create_timer(2.0, cb)
        rclpy.spin(node)
