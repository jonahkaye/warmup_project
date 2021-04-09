#!/usr/bin/env python3
""" This script publishes ROS messages containing the 3D coordinates of a single point """
import rospy
import math
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class PersonFollower(object):
    def __init__(self):
        # Start rospy node.
        rospy.init_node("follow_person")
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

        closest = math.inf
        deg = 0
        for i in range(len(msg.ranges)):
            if msg.ranges[i] < closest:
                deg = i
                closest =  msg.ranges[i]

        #turn to the farthest degree 

        #angular_speed = 5*2*math.pi/360  
        current_angle = 0 
        if deg not in [359,0,1]: #  The turtlebot turns left
            if deg < 180:
                self.my_twist.angular.z = deg/360 * 5
            if deg >= 180:
                self.my_twist.angular.z = -deg/360 * 5
        else:
            self.my_twist.angular.z = 0

        if closest > 0.5 and closest < 3.5:
            self.my_twist.linear.x = 0.5
        elif closest < 0.5:
            self.my_twist.linear.x = 0
            
        self.twist_pub.publish(self.my_twist)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    # Declare a node and run it.
    node = PersonFollower()
    node.run()