#!/usr/bin/python3

import rospy
from turtlesim.msg import *
from turtlesim.srv import *
from geometry_msgs.msg import Twist
from std_srvs.srv import *
import random
from math import *


#initialization of victim pose
# victim position
victim_x = 0.0
victim_y = 0.0
victim_theta = 0.0

#initialization of turtle1 pose
# turtle position
turtle_x = 0.0
turtle_y = 0.0
turtle_theta = 0.0

#constants of proportional gains of PID controllers
tolerance_1 = 1.5
tolerance_2 = 5.5

#function to configure victim's position
def victim_position(victim_pose):
    global victim_x, victim_y, victim_theta
    victim_x = victim_pose.x
    victim_y = victim_pose.y
    victim_theta = victim_pose.theta

#function to configure turtle's position
def turtle_position(turtle_pose):
    global turtle_x, turtle_y, turtle_theta
    turtle_x = turtle_pose.x
    turtle_y = turtle_pose.y
    turtle_theta = turtle_pose.theta

#implementation of a PID controller algorithm
def chase_victim(vel_publisher):
    global turtle_x, turtle_y, turtle_theta

    vel_msg = Twist()

    while not rospy.is_shutdown():
   
        euclidean_distance = sqrt(pow((victim_x - turtle_x), 2) + pow((victim_y - turtle_y), 2))
        
        steering_angle = atan2(victim_y - turtle_y, victim_x - turtle_x) - turtle_theta
        linear_vel = tolerance_1 * euclidean_distance * cos(steering_angle)
        vel_msg.linear.x = linear_vel
        angular_vel = tolerance_2 * steering_angle
        vel_msg.angular.z = angular_vel

        vel_publisher.publish(vel_msg)


#spawning a second turtle called victim at a random position, we'll later be able to control it using teleop key
x = random.randint(1, 10)
y = random.randint(1, 10)
rospy.wait_for_service('/spawn')
spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
spawn_turtle(x, y, 0, 'victim')


#initializing our node and making sure that it is unique
rospy.init_node('give_chase', anonymous=True)

# create a publisher object
vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

# subscribe to turtles pose
rospy.Subscriber("/turtle1/pose", Pose, turtle_position)
rospy.Subscriber("/victim/pose", Pose, victim_position)

#publishing our message
victim_position(Pose())
chase_victim(vel_publisher)
