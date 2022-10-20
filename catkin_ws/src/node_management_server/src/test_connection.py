#!/usr/bin/python3

## Importing relevant libraries

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

# Declaring the application start here
app = Flask(__name__)

# declaring variables to store drone status
essentialNodes = False

app.config['armed_status'] = False
app.config['armed_status_takeoff'] = False
app.config['current_location'] = "HomeLand"

#Run Essential ROS Nodes & Simulator
def run_essentialNodes():

        """
        This function will execute ROS nodes:- Gazebo and MAVROS

        Gazebo is the simulator that provides a virtual environment for the drone
        MAVROS is the brain that works for the drone

        :return: None
        """

        print("Running Essenstial Nodes Gazebo, MAVROS and OFFBOARD Node")
        os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
        directory= os.getcwd()
        #print(directory)
        px4GazeboSimulator = subprocess.Popen(['sh', '1_gazebo.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mavrosScript = subprocess.Popen(['sh', 'mavros.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        #offboardScript = subprocess.Popen(['sh', 'offboard.sh'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        global essentialNodes
        essentialNodes = True

# This is the manager node for the ROS
# Run Manager Node
rospy.init_node('manager_node')

# This runs the function which executes the nodes for operation
# Run Essential Nodes: Mavros & Offboard
EssentialNodesThread = threading.Thread(target=run_essentialNodes).start()

time.sleep(5)

# NOT NEEDED
#Drone Command Publishers
pubTakeoff = rospy.Publisher('takeoff', String,queue_size=1)
pubLand = rospy.Publisher('land', String,queue_size=1)

# function to execute take off command
def takeoff():
    print("Checking to see if Drone can Takeoff...")
    #pubTakeoff.publish("ON")
    os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
    directory= os.getcwd()
    takeoffProcess = subprocess.Popen(['sh', 'takeoff.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    return True

# function to execute landing command
def land():
    print("Drone Land Activated")
   # pubLand.publish("ON")
    os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
    directory= os.getcwd()
    landProcess = subprocess.Popen(['sh', 'land.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    return False

# function to execute arming command
def arm():
    print("Drone Arming Activated")
   # pubLand.publish("ON")
    os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
    directory= os.getcwd()
    landProcess = subprocess.Popen(['sh', 'arm.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    return False

# function to execute disarming command
def disarm():
    print("Drone Disarming Activated")
   # pubLand.publish("ON")
    os.chdir("/home/user/catkin_ws/src/nlp_ros/src/")
    directory= os.getcwd()
    landProcess = subprocess.Popen(['sh', 'disarm.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    return False

# function to ask the drone the battery level
# currently returns a random value between 5 to 100
def battery():
    print("Drone battery status Queried")
    battery_level = random.randint(5,100)
    return "The Battery Level is: {}%".format(battery_level)

# function to ask the drone the voltage level
# currently returns a random value between 1.0 to 5.0 with a step value of 0.1
def voltage():
    print("Drone voltage level Queried")
    voltage_level = round(random.uniform(1.0, 5.0), 1)
    return "The Voltage Level is: {}V".format(voltage_level)

# # function to ask the drone the location where it is
# # currently returns a random position
# def location():
#     print("Drone Location Queried")
#     location = random.choice(['kitchen', 'garage', 'bedroom', 'hall', 'living room'])
#     return "The Drone is located in the : {}".format(location)

cmd = True

## this is the function that gets executed when the
# flaks API gets the GET/POST command at the address '/'
# along with the IP address and port being executed with
@app.route('/', methods=['POST', 'GET'])
def test_func():

    try:

        # This gets the input request which is sent in json format
        inpJSON = request.get_json()

        # 'message' being a key in the json if not found, raise the error
        if "message" not in inpJSON:
            return "ERROR", 305

        # get the message content that is sent in the json package
        message_content = inpJSON["message"]

        # based on what the message content is, the functions defined above can be executed
        # the message content has to match with what is sent from the Lambda function associated with the Lex bot

        # following a common format:-
            # 1. Executing the function defined above
            # 2. Logging the function completion on terminal
            # 3. Changing armed_status and armed_status_takeoff based on which function is executed (if needed)
            # 4. Print if the drone is armed or not on the terminal (if needed)
            # 5. Changing the return message content (if needed)

        if 'taking off' in message_content:
            takeoff()
            print("TAKING OFF COMMAND EXECUTED")
            app.config["armed_status_takeoff"] = True
            app.config["armed_status"] = True
            app.config['current_location'] = "Air"
            print("ARMED_STATUS", app.config["armed_status"])

        if 'landing' in message_content:
            land()
            print("LANDING COMMAND EXECUTED")
            app.config["armed_status"] = False
            app.config['current_location'] = "HomeLand"
            print("ARMED_STATUS", app.config["armed_status"])

        if 'disArming' in message_content:
            disarm()
            print("DISARMING COMMAND EXECUTED")
            app.config["armed_status"] = False
            app.config['current_location'] = "HomeLand"
            print("ARMED_STATUS", app.config["armed_status"])

        if 'arming' in message_content:
            arm()
            print("ARMING COMMAND EXECUTED")
            if app.config["armed_status_takeoff"] == True:
                app.config["armed_status"] = True
            else:
                app.config["armed_status"] = False
            print("ARMED_STATUS", app.config["armed_status"])

        if "LOCATION_AND_ACTION" in message_content:
            message_content = message_content
            location_sent = message_content.split("\n")[1].split(',')[0].split()[1]
            app.config['current_location'] = location_sent
            print("SENDING TO LOCATION COMMAND EXECUTED")

        if 'Battery' in message_content:
            message_content = battery()
            print("BATTERY COMMAND EXECUTED")
            
        if 'Voltage' in message_content:
            message_content = voltage()
            print("VOLTAGE COMMAND EXECUTED")

        if 'Location' in message_content:
            message_content = "The Drone is currently at this location: {}".format(app.config['current_location'])
            print("LOCATION STATUS COMMAND EXECUTED")

        if 'Armed' in message_content:
            print("ARMED_STATUS", app.config["armed_status"])
            if app.config["armed_status"]==True:
                message_content = "The Drone is currently Armed"
            else:
                message_content = "The Drone is currently not Armed"

        # Return the message_content (can get modified in the above 4 functions)
        retJSON = {
                    "return_message": message_content
        }

    # if due to some reason, the above piece of code fails, finish the call with this return message
    except:

        retJSON = {
                    "return_message": "THIS IS NOT WORKING!!!"
        }

    # returning the message here
    return jsonify(retJSON)

if __name__=="__main__":

    # run the flask API with the below mentioned ip address and port hosting the API
    # The API would listen all messages incoming at this address
    # Check the IP address of the system from where the API would run to modify this
    # For the linux machine provided, the default port opened is 5494
    # Need to be connected to VPN to interact (if the Linux machine is in office)
    app.run(host="172.16.162.83", port="5494")
    #app.run()
    # 192.168.12.14

    # 172.16.162.83

