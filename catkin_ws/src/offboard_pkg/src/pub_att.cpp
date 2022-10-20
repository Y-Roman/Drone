#include <ros/ros.h>
#include <std_msgs/String.h> 
#include <stdio.h>
#include <math.h>
#include "geometry_msgs/PoseStamped.h"
#include "geometry_msgs/Vector3Stamped.h"
#include "std_msgs/Float64.h"
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

 
//#include </home/mahesh/catkin_ws/src/beginner_tutorials/src/Qualisys.h>
 
int main(int argc, char **argv)
{
   ros::init(argc, argv, "pub_setpoints");
   ros::NodeHandle n;
   ros::Subscriber state_sub = n.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);
   ros::Publisher local_pos_pub = n.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 100);
   ros::Publisher pub_att = n.advertise<geometry_msgs::PoseStamped>("/mavros/setpoint_attitude/attitude",100);
   ros::Publisher pub_thr = n.advertise<std_msgs::Float64>("/mavros/setpoint_attitude/att_throttle", 100);
   ros::ServiceClient arming_client = n.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");
    ros::ServiceClient set_mode_client = n.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");
   ros::Rate loop_rate(100);
    
    // wait for FCU connection
    while(ros::ok() && !current_state.connected){
        ros::spinOnce();
        loop_rate.sleep();
    }

    geometry_msgs::PoseStamped pose;
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 2;

    //send a few setpoints before starting
    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(pose);
        ros::spinOnce();
        loop_rate.sleep();
    }


   mavros_msgs::SetMode offb_set_mode;
   offb_set_mode.request.custom_mode = "OFFBOARD";

   mavros_msgs::CommandBool arm_cmd;
   arm_cmd.request.value = true;
   if( arming_client.call(arm_cmd) &&
                    arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                }
   	if( set_mode_client.call(offb_set_mode) &&
                offb_set_mode.response.mode_sent){
                ROS_INFO("Offboard enabled");
            }


   geometry_msgs::PoseStamped cmd_att;
   std_msgs::Float64 cmd_thr;
   int count = 1;
   double v[3]={1.0, 0.0, 0.0};
   double lambda = 0.3;
 
   double v_norm=sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);
   double theta=0.0;
   
        //PositionReciever qp;
        //Body some_object;
        //qp.connect_to_server();
 
     
   while(ros::ok()){
       //some_object = qp.getStatus();
        // some_object.print();
        //printf("%f\n",some_object.position_x);
        //Create attitude command message
       cmd_att.header.stamp = ros::Time::now();
       cmd_att.header.seq=count;
       cmd_att.header.frame_id = 1;
       cmd_att.pose.position.x = 0.0;//0.001*some_object.position_x;
       cmd_att.pose.position.y = 0.0;//0.001*some_object.position_y;
       cmd_att.pose.position.z = 0.0;//0.001*some_object.position_z;
 
       cmd_att.pose.orientation.x = sin(theta/2.0)*v[0]/v_norm;
       cmd_att.pose.orientation.y = sin(theta/2.0)*v[1]/v_norm;
       cmd_att.pose.orientation.z = sin(theta/2.0)*v[2]/v_norm;
       cmd_att.pose.orientation.w = cos(theta/2.0);
      /*
       double q_norm = sqrt(sin(theta/2.0)*sin(theta/2.0)+cos(theta/2.0)*cos(theta/2.0));
        printf("%f\t",v_norm);
        printf("%f\n", q_norm);
    */
       //Create throttle command message
       cmd_thr.data = lambda;
       
       pub_att.publish(cmd_att);
       pub_thr.publish(cmd_thr);
       ros::spinOnce();
       count++;
       theta=0.3*sin(count/300.0);
       loop_rate.sleep();
/*
   if(count>1000){
        count =0;
    }
    */
   }
    
       
   return 0;
}
