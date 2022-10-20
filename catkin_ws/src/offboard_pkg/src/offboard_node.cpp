/**
 * @file offb_node.cpp
 * @brief Offboard control example node, written with MAVROS version 0.19.x, PX4 Pro Flight
 * Stack and tested in Gazebo SITL
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include "std_msgs/String.h"
#include "std_msgs/Bool.h"

bool takeoff_cmd=false;
bool land_cmd = false;

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

void takeoffCallback(const std_msgs::String::ConstPtr& msg)
  {
     ROS_INFO("I heard: [%s]", msg->data.c_str());
     takeoff_cmd=true;
     ROS_INFO("Takeoff Status: %d \n ",takeoff_cmd);
  }

void landCallback(const std_msgs::String::ConstPtr& msg)
  {
     ROS_INFO("I heard: [%s]", msg->data.c_str());
     land_cmd=true;
     ROS_INFO("Landing Status: %d \n ",takeoff_cmd);
  }

int main(int argc, char **argv)
{
    ros::init(argc, argv, "offb_node");
    ros::NodeHandle nh;

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);
    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");

    //management server
    ros::Subscriber takeoffSub = nh.subscribe("takeoff", 10, takeoffCallback);
    ros::Subscriber landSub    = nh.subscribe("land", 10, landCallback);

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    // wait for FCU connection and for takeoff command from the server
    while(ros::ok()){
        ros::spinOnce();
        rate.sleep();
        //ROS_INFO("Takeoff Status: %d \n ",takeoff_cmd);
        if(takeoff_cmd==true && current_state.connected){
            geometry_msgs::PoseStamped pose;
            pose.pose.position.x = 0;
            pose.pose.position.y = 0;
            pose.pose.position.z = 2;

            //send a few setpoints before starting
            for(int i = 100; ros::ok() && i > 0; --i){
                local_pos_pub.publish(pose);
                ros::spinOnce();
                rate.sleep();
            }

            mavros_msgs::SetMode offb_set_mode;
            offb_set_mode.request.custom_mode = "OFFBOARD";

            mavros_msgs::CommandBool arm_cmd;
            arm_cmd.request.value = true;

            ros::Time last_request = ros::Time::now();

            while(ros::ok()){
                if( current_state.mode != "OFFBOARD" &&
                    (ros::Time::now() - last_request > ros::Duration(5.0))){
                    if( set_mode_client.call(offb_set_mode) &&
                        offb_set_mode.response.mode_sent){
                        ROS_INFO("Offboard enabled");
                    }
                    last_request = ros::Time::now();
                } else {
                    if( !current_state.armed &&
                        (ros::Time::now() - last_request > ros::Duration(5.0))){
                        if( arming_client.call(arm_cmd) &&
                            arm_cmd.response.success){
                            ROS_INFO("Vehicle armed");
                        }
                        last_request = ros::Time::now();
                    }
                }

                local_pos_pub.publish(pose);

                if(land_cmd == true){
                        geometry_msgs::PoseStamped pose;
                        pose.pose.position.x = 0;
                        pose.pose.position.y = 0;
                        pose.pose.position.z = 0;
                        local_pos_pub.publish(pose);
                }

                ros::spinOnce();
                rate.sleep();
            }

        }
    }

    return 0;
}