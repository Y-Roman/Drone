#!/bin/bash
source ~/Drone/catkin_ws/devel/setup.bash
sleep 1
roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"
