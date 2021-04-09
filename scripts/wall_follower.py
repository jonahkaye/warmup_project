#!/usr/bin/env python3
""" This script publishes ROS messages containing the 3D coordinates of a single point """
import rospy
import math
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

straight_bool = 0 

class WallFollower(object):
    def __init__(self):
        # Start rospy node.
        rospy.init_node("follow_wall")
        # Declare our node as a subscriber to the scan topic and
        #   set self.process_scan as the function to be used for callback.
        rospy.Subscriber("/scan", LaserScan, self.distance)
        # Get a publisher to the cmd_vel topic.
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        # Create a default twist msg (all values 0).
        lin = Vector3()
        ang = Vector3()
        self.my_twist = Twist(linear=lin,angular=ang)

    def distance(self,msg):

        closest = msg.ranges[90]

        LorR = -1 
        if msg.ranges[90] < msg.ranges[270]:
            LorR = -1
        else:
            LorR = 1
        
        if msg.ranges[0] < 0.75 and msg.ranges[45] < 0.5:
            straight_bool = 0
        else:
            straight_bool = 1
        
        if straight_bool: # angular controls
            self.my_twist.angular.z = (closest - 0.5) * 0.1
        else:
            self.my_twist.angular.z = LorR * 0.1

        if straight_bool: # linear controls 
            self.my_twist.linear.x = 0.2
        else:
            self.my_twist.linear.x = 0
            
        self.twist_pub.publish(self.my_twist)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    # Declare a node
    node = WallFollower()
    node.run()