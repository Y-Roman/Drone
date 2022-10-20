#!/bin/bash
rosrun mavros mavsafety arm
sleep 1
rosrun mavros mavcmd takeoffcur 0 0 2.5
