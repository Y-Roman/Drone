#!/bin/bash
rosrun mavros mavcmd landcur 0 0 
sleep 4
rosrun mavros mavsafety disarm
