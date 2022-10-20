/**
 * @file offb_node.cpp
 * @brief Offboard control example node, written with MAVROS version 0.19.x, PX4 Pro Flight
 * Stack and tested in Gazebo SITL
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/CommandTOL.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include "std_msgs/String.h"
#include "std_msgs/Bool.h"

//Current position of the drone
double x_position;
double y_position;
double z_position;

void position_call_back(const geometry_msgs::PoseStamped::ConstPtr &msg){
    geometry_msgs::PoseStamped position = *msg;
    x_position = position.pose.position.x;
    y_position = position.pose.position.y;
    z_position = position.pose.position.z;
}

bool is_greater_then_threshold(geometry_msgs::PoseStamped destination){
	//Is drone close enough to the target
    double distance = sqrt(pow(destination.pose.position.x - x_position, 2) + pow(destination.pose.position.y - y_position, 2));
    return distance> 0.8; //0.8 is just a threshold
}

//function that make drone move by publishing destination.
void travel(geometry_msgs::PoseStamped destination, ros::Publisher local_pos_pub, ros::Publisher next_pos_pub  ){
    while(is_greater_then_threshold(destination)){
        next_pos_pub.publish(destination.pose.position);
        local_pos_pub.publish(destination);
        sleep(1);
    }
    return;
}

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
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
	
    //from square script
    ros::Publisher next_pos_pub = nh.advertise<geometry_msgs::Point>("/drone/next_waypoint", 1000);
    ros::Subscriber position_sub = nh.subscribe<geometry_msgs::PoseStamped>("/mavros/local_position/pose", 10, position_call_back);

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    while(ros::ok()){
        ros::spinOnce();
        rate.sleep();
        
        if(current_state.connected){
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
		
		//**** Enter the Square Script Here ****
		//Declare destination, change it when reached.
		    geometry_msgs::PoseStamped destination;
		    destination.pose.position.x = 3;
		    destination.pose.position.y = 0;
		    destination.pose.position.z = 10;
		    travel(destination, local_pos_pub, next_pos_pub);
			//second point of the square 
		    destination.pose.position.x = 3;
		    destination.pose.position.y = 3;
		    destination.pose.position.z = 10;
		    travel(destination, local_pos_pub, next_pos_pub);
		    //third point of the square
		    destination.pose.position.x = 0;
		    destination.pose.position.y = 3;
		    destination.pose.position.z = 10;
		    travel(destination, local_pos_pub, next_pos_pub);
		    //final point 
		    destination.pose.position.x = 0;
		    destination.pose.position.y = 0;
		    destination.pose.position.z = 10;
		    travel(destination, local_pos_pub, next_pos_pub);

                    //local_pos_pub.publish(pose);
		ros::ServiceClient land_cl = nh.serviceClient<mavros_msgs::CommandTOL>("/mavros/cmd/land");
		    mavros_msgs::CommandTOL srv_land;
		    srv_land.request.altitude = 10;
		    srv_land.request.latitude = 0;
		    srv_land.request.longitude = 0;
		    srv_land.request.min_pitch = 0;
		    srv_land.request.yaw = 0;
		    if(land_cl.call(srv_land)){
			ROS_INFO("srv_land send ok %d", srv_land.response.success);
		    }else{
			ROS_ERROR("Failed Land");
		    }

                ros::spinOnce();
                rate.sleep();
            }

        }
    }

    return 0;
}
