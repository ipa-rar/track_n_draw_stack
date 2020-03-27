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
        start_pos = Pose(position=Point(0.10, -0.78, 0.25))
        center_pos = Pose(position=Point(0, -0.68, 0.25))
        goal_pos = Pose(position=Point(-0.10, -0.78, 0.25))
        # planners starting here
        try:
            self.r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))
        except RobotMoveFailed:
            rospy.loginfo("The pose is not unreachable")

        try:
            self.r.move(Circ(goal=goal_pos, center=center_pos, acc_scale=0.4))
        except RobotMoveFailed:
            rospy.loginfo("The pose is unreachable")

    def move_robot(self):
        joint_goal = [1.1450463005300113, 1.3449728449134062, 0.3303570566119351, -
                      1.2896732177397627, -1.2425725076038912, -1.762039518051274]
        cartesian_goal = Pose(position=Point(0.540, -0.283, 0.682),
                              orientation=Quaternion(-0.000, 0.726, 0.000, 0.688))
        self.r.move(Ptp(goal=joint_goal, vel_scale=__ROBOT_VELOCITY__))
        self.r.move(Ptp(goal=cartesian_goal, vel_scale=__ROBOT_VELOCITY__))

    def pick_and_place(self):
        self.r.move(Lin(goal=Pose(position=Point(0, 0, 0.1)),
                        reference_frame="prbt_tcp", vel_scale=0.2))
        rospy.loginfo("Open/Close the gripper")  # log
        rospy.sleep(0.2)
        self.r.move(Lin(goal=Pose(position=Point(0, 0, -0.1)),
                        reference_frame="prbt_tcp", vel_scale=0.2))

    def start_program(self):
        # positions declared
        start_pose = [1.49, -0.54, 1.09, 0.05, 0.91, -1.67]
        pick_pos = Pose(position=Point(-0.0060056, -0.815452, 0.150537),
                        orientation=Quaternion(0.998554, 0.0525097, 0.00671931, 0.00937636))
        work_pos = Pose(position=Point(-0.018218, -0.90926, 0.343775),
                        orientation=Quaternion(0.998554, 0.0525097, 0.00671931, 0.00937636))
        place_pos = Pose(position=Point(-0.0458218, -0.890926, 0.223775),
                         orientation=Quaternion(0.998554, 0.0525097, 0.00671931, 0.00937636))
        # default start position
        self.r.move(Ptp(goal=start_pose, vel_scale=__ROBOT_VELOCITY__))
        # Logic loops here
        while(True):
            self.r.move(Ptp(goal=pick_pos, vel_scale=__ROBOT_VELOCITY__))
            self.pick_and_place()
            rospy.sleep(1)
            self.r.move(Ptp(goal=place_pos, vel_scale=__ROBOT_VELOCITY__))
            self.pick_and_place()
            rospy.sleep(1)


def main():
    rospy.init_node('track_n_draw_node')
    track_n_draw = TrackNDraw()
    track_n_draw.start_program()


if __name__ == "__main__":
    main()
