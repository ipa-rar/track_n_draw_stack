#!/usr/bin/env python
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy
# Parameters
__REQUIRED_API_VERSION__ = "1"
__ROBOT_VELOCITY__ = 0.5

class TrackNDraw():
    def __init__(self):
        self.r = Robot(__REQUIRED_API_VERSION__)
        home_pos = [1.69, -0.07, 1.41, -0.14, 0.16, -0.63]
        self.r.move(Ptp(goal=home_pos, vel_scale=__ROBOT_VELOCITY__))
    
    def draw_circle(self):
        pass

    def move_to_center(self):
        pass

    def task(self):
        pass

def main():
    rospy.init_node('track_n_draw_node')
    track_n_draw = TrackNDraw()


if __name__ == "__main__":
    main()