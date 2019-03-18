#! /usr/bin/env python

import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj
import rospkg
rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + \
    "/config/init_pos.txt"
# change the filename above to either "/config/get_food.txt"
# or "/config/release_food.txt" to view the three different poses built in

rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service = rospy.ServiceProxy(
    '/execute_trajectory', ExecTraj)

print execute_trajectory_service(traj)
