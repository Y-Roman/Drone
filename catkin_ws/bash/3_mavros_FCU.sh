#!/bin/bash
source ~/Drone/catkin_ws/devel/setup.bash
sleep 1
chmod 777 /dev/ttyACM0
sleep 2
roslaunch mavros px4.launch fcu_url:=/dev/ttyACM0:115200
