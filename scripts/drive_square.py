#!/usr/bin/env python3
""" This script publishes ROS messages containing the 3D coordinates of a single point """
import rospy
from geometry_msgs.msg import Twist

PI = 3.1415926535897
right_angle = 90*2*PI/360
angular_speed = 10*2*PI/360

class DriveSquares(object):
    def __init__(self):
        rospy.init_node('drive_squares')
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def run(self):
        my_twist = Twist()

        r =rospy.Rate(2)
        while not rospy.is_shutdown():
            my_twist.linear.x = 0.5
            my_twist.angular.z = 0
            current_angle = 0
            self.velocity_publisher.publish(my_twist)

            t_end = rospy.Time.now().to_sec() + 2
            while rospy.Time.now().to_sec() < t_end:
                pass # wait and do nothing
            my_twist.angular.z = angular_speed
            my_twist.linear.x = 0
            self.velocity_publisher.publish(my_twist)

            t0 = rospy.Time.now().to_sec()    
            while (current_angle <= right_angle):
                self.velocity_publisher.publish(my_twist)
                t1 = rospy.Time.now().to_sec()
                current_angle = angular_speed * (t1-t0)

if __name__ == '__main__':
    node = DriveSquares()
    node.run()
            
        
