#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
# Parameters

class OmplTask():
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        group_name = "manipulator"
        self.move_group = moveit_commander.MoveGroupCommander(group_name)

    def display_details(self):
        planning_frame = self.move_group.get_planning_frame()
        print "============ Planning frame: %s" % planning_frame
        eef_link = self.move_group.get_end_effector_link()
        print "============ End effector link: %s" % eef_link
        group_names = self.robot.get_group_names()
        print "============ Available Planning Groups:", self.robot.get_group_names()
        print "============ Printing robot state"
        print(self.robot.get_current_state())
        print ""

    def target_pos(self):
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.position.x = -0.049
        pose_goal.position.y = -0.37
        pose_goal.position.z = 0.7
        self.move_group.set_pose_target(pose_goal)

        plan = self.move_group.go(wait=True)

    def cleanup(self):
        self.move_group.stop()
        self.move_group.clear_pose_targets()


def main():
    rospy.init_node('track_n_draw_node')
    planer = OmplTask()
    planer.display_details()
    planer.target_pos()
    planer.cleanup()


if __name__ == "__main__":
    main()
