#!/usr/bin/python3
import os
import rospy
import threading
import random
import math
import subprocess
import time

from flask import Flask, jsonify, request

from std_msgs.msg import String

app = Flask(__name__)

essentialNodes = False

#Run Essential ROS Nodes & Simulator
def run_essentialNodes():
        print("Running Essenstial Nodes Gazebo and MAVROS Node")
        os.chdir("/home/user/Drone/catkin_ws/src/node_management_server/src/commands")
        directory= os.getcwd()
        px4GazeboSimulator = subprocess.Popen(['sh', '1_gazebo.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mavrosScript = subprocess.Popen(['sh', 'mavros.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)

# Run Manager Node
rospy.init_node('manager_node')

# Run Essential Nodes: Mavros & Offboard
EssentialNodesThread = threading.Thread(target=run_essentialNodes).start()
time.sleep(5)

def takeoff():
    print("Checking to see if Drone can Takeoff...")
    os.chdir("/home/user/Drone/catkin_ws/src/node_management_server/src/commands")
    directory= os.getcwd()
    takeoffProcess = subprocess.Popen(['sh', 'takeoff.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def land():
    print("Drone Land Activated")
    os.chdir("/home/user/Drone/catkin_ws/src/node_management_server/src/commands")
    directory= os.getcwd()
    landProcess = subprocess.Popen(['sh', 'land.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def explore():
    print("Exploration Activated")
    os.chdir("/home/user/Drone/catkin_ws/src/node_management_server/src/commands")
    directory= os.getcwd()
    landProcess = subprocess.Popen(['sh', 'explore.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@app.route('/', methods=['POST', 'GET'])
def test_func():

    inpJSON = request.get_json()

    if "message" not in inpJSON:
        return "ERROR", 305
        
    message_content = inpJSON["message"]

    if 'taking off' in message_content:
        takeoff()
        print("TAKING OFF COMMAND EXECUTED")

    if 'landing' in message_content:
        land()
        print("LANDING COMMAND EXECUTED")
    
    if 'exploring' in message_content:
        explore()
        print("Explore COMMAND EXECUTED")

    retJSON = {
                "return_message": message_content
    }

    return jsonify(retJSON)

if __name__=="__main__":
    app.run(host="172.16.162.83", port="5494")
    app.run()




