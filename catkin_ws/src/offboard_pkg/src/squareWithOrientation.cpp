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

#define FLIGHT_ALTITUDE 2.5f

#define LEFT90 0.7071f
#define SQUARE 2.0f

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

int main(int argc, char **argv)
{
    
    //************************Setup Pubs and Subs************************\\
    
    ros::init(argc, argv, "offb_node");
    ros::NodeHandle nh;

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);
    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");
    ros::ServiceClient land_client = nh.serviceClient<mavros_msgs::CommandTOL>
      ("mavros/cmd/land");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(30.0);

    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
        ROS_INFO("connecting to FCT...");
    }

    geometry_msgs::PoseStamped home_pose;
    geometry_msgs::PoseStamped pose;

    //Set Home Position
    home_pose.pose.position.x = 0;
    home_pose.pose.position.y = 0;
    home_pose.pose.position.z = FLIGHT_ALTITUDE;
    
    //Set Initial Position
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = FLIGHT_ALTITUDE;
 
    //send a few setpoints before starting
    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(home_pose);
        ros::spinOnce();
        rate.sleep();
    }

    //************************Setup Offboard Arm and Land Services ************************\\

    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";

    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;

    mavros_msgs::CommandTOL land_cmd;
    land_cmd.request.yaw = 0;
    land_cmd.request.latitude = 0;
    land_cmd.request.longitude = 0;
    land_cmd.request.altitude = 0;

//************************ Enter Offboard Mode and Arm Drone ************************\\

    ros::Time last_request = ros::Time::now();
   
    // change to offboard mode and arm
    while(ros::ok() && !current_state.armed){
        if( current_state.mode != "OFFBOARD" &&
            (ros::Time::now() - last_request > ros::Duration(5.0))){
          ROS_INFO(current_state.mode.c_str());
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
	ros::spinOnce();
        rate.sleep();
    }

//************************ Start Mission ************************\\

    // go to the first waypoint
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = FLIGHT_ALTITUDE;

    ROS_INFO("going to the first way point");
    for(int i = 0; ros::ok() && i < 10*20; ++i){
      local_pos_pub.publish(pose);
      ros::spinOnce();
      rate.sleep();
    }
    ROS_INFO("first way point finished!");
    
    //set orientation to be left
    pose.pose.orientation.w=LEFT90;
    pose.pose.orientation.z=LEFT90;

    // go to the second waypoint
    pose.pose.position.x = 0;
    pose.pose.position.y = SQUARE;
    pose.pose.position.z = FLIGHT_ALTITUDE;

    //send setpoints for 10 seconds
    ROS_INFO("going to second way point");
    for(int i = 0; ros::ok() && i < 10*20; ++i){

      local_pos_pub.publish(pose);
      ros::spinOnce();
      rate.sleep();
    }
    ROS_INFO("second way point finished!");

   //set orientation to be right
    pose.pose.orientation.w=1;
    pose.pose.orientation.z=0;

    // go to the third waypoint
    pose.pose.position.x = SQUARE;
    pose.pose.position.y = SQUARE;
    pose.pose.position.z = FLIGHT_ALTITUDE;

    //send setpoints for 10 seconds
    ROS_INFO("going to third way point");
    for(int i = 0; ros::ok() && i < 10*20; ++i){

      local_pos_pub.publish(pose);
      ros::spinOnce();
      rate.sleep();
    }
    ROS_INFO("third way point finished!");
    
    //set orientation to be right
    pose.pose.orientation.w=LEFT90;
    pose.pose.orientation.z=-1*LEFT90;
    
   // go to the forth waypoint
    pose.pose.position.x = SQUARE;
    pose.pose.position.y = 0;
    pose.pose.position.z = FLIGHT_ALTITUDE;

    //send setpoints for 10 seconds
    ROS_INFO("going to forth way point");
    for(int i = 0; ros::ok() && i < 10*20; ++i){

      local_pos_pub.publish(pose);
      ros::spinOnce();
      rate.sleep();
    }
    ROS_INFO("forth way point finished!");
    
    //set orientation to be right
    pose.pose.orientation.w=0;
    pose.pose.orientation.z=-1;

    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = FLIGHT_ALTITUDE;
    ROS_INFO("going back to the first point!");
    //send setpoints for 10 seconds
    for(int i = 0; ros::ok() && i < 10*20; ++i){

      local_pos_pub.publish(pose);
      ros::spinOnce();
      rate.sleep();
    }

    // Orient back to origin
    pose.pose.orientation.w=1;
    pose.pose.orientation.z=0;

    for(int i = 0; ros::ok() && i < 5*20; ++i){
    local_pos_pub.publish(pose);
    ros::spinOnce();
    rate.sleep();
}


    ROS_INFO("trying to land");
    while (!(land_client.call(land_cmd) &&
            land_cmd.response.success)){
      //local_pos_pub.publish(pose);
      ROS_INFO("trying to land");
      ros::spinOnce();
      rate.sleep();
    }
    return 0;
}




