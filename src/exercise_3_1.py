#! /usr/bin/env python

import rospy
import rospkg
rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + \
    "/config/get_food.txt"


rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service = rospy.ServiceProxy(
    '/execute_trajectory')

print execute_trajectory_service(traj)
