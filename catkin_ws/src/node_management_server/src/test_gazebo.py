#!/usr/bin/python3
import os
import rospy
import threading
import random
import math
import subprocess
import time
import boto3
from flask import Flask, jsonify, request

from std_msgs.msg import String

essentialNodes = False

#Run Essential ROS Nodes & Simulator
def run_essentialNodes():
        print("Running Essenstial Nodes Gazebo, MAVROS and OFFBOARD Node")
        os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
        directory= os.getcwd()
        #print(directory)
        px4GazeboSimulator = subprocess.Popen(['sh', '1_gazebo.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mavrosScript = subprocess.Popen(['sh', 'mavros.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        offboardScript = subprocess.Popen(['sh', 'offboard.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        global essentialNodes
        essentialNodes = True

# Run Manager Node
rospy.init_node('manager_node')

# Run Essential Nodes: Mavros & Offboard
EssentialNodesThread = threading.Thread(target=run_essentialNodes).start()
time.sleep(5)
#Drone Command Publishers
pubTakeoff = rospy.Publisher('takeoff', String,queue_size=1)
pubLand = rospy.Publisher('land', String,queue_size=1)

def takeoff():
    print("Checking to see if Drone can Takeoff...")
    pubTakeoff.publish("ON")

def land():
    print("Drone Land Activated")
    pubLand.publish("ON")

 #Connect to AWS Here
 #Deserialize incoming Command and call functions Written Above
cmd = True


while not rospy.is_shutdown():

    print("manager node is running")

    time. sleep(20)

    print("TAKING OFF")
    takeoff()
    print("FINISHED TAKING OFF")

    time. sleep(30)

    print("LANDING")
    land()
    print("FINISHED LANDING")

