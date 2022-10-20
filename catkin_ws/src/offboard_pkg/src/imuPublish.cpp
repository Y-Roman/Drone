#include "ros/ros.h"
#include "sensor_msgs/Imu.h"
#include "mavros_msgs/State.h"


void chatterCallback(const sensor_msgs::Imu::ConstPtr& msg)
{
  ROS_INFO("Imu Seq: [%d]", msg->header.seq);
  ROS_INFO("Imu Stamp sec: [%d]", msg->header.stamp.sec);
  ROS_INFO("Imu Stamp nsec: [%d]", msg->header.stamp.nsec);
  ROS_INFO("Imu Orientation x: [%f], y: [%f], z: [%f], w: [%f]", msg->orientation.x,msg->orientation.y,msg->orientation.z,msg->orientation.w);
}

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "imu_listener");

  ros::NodeHandle n;

 ros::Subscriber state_sub = n.subscribe<mavros_msgs::State>
          ("mavros/state", 10, state_cb);
  ros::Subscriber sub = n.subscribe<sensor_msgs::Imu>
          ("mavros/imu/data", 1000, chatterCallback);


  ros::Rate rate(20.0);

  while(ros::ok() && current_state.connected){
      ros::spinOnce();
      rate.sleep();
  }

  for(int i = 100; ros::ok() && i > 0; --i){
      ros::spinOnce();
      rate.sleep();
  }

  ros::spin();

  return 0;
}
