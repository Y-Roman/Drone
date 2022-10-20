# Drone
Px4 Compatible Drone Voice Based Navigation System


## Overview

Controllers for controlling UAVs using the [mavros](https://github.com/mavlink/mavros) package in OFFBOARD mode.

The repository contains Offboard Control for controlling UAVs using the mavros package in ROS. The following packages are included in the repo
- Mavros: mavros is a ROS (1) package that enables MAVLink extendable communication between computers running ROS (1) for any MAVLink enabled  autopilot, ground station, or peripheral. MAVROS is the "official" supported bridge between ROS (1) and the MAVLink protocol.
- offboard_pkg: Offboard mode is primarily used for controlling vehicle movement and attitude. It supports a set of MAVLink messages. Offboard package includes the trajectory_publisher which publishes setpoints as states from motion primitives / trajectories for the controller to follow.

[![Circular trajectory tracking](https://img.youtube.com/vi/IEyocdnlYw0/0.jpg)](https://youtu.be/IEyocdnlYw0 "Circular trajectory tracking")

### Pre-Reqs
Linux Ubuntu 18.04 running ROS Melodic
The easiest way to setup PX4 simulation with ROS on Ubuntu Linux is to use the standard installation script that can be found at Development Environment
- on Linux > Gazebo with ROS( [Linux Gazebo with ROS](https://docs.px4.io/main/en/dev_setup/dev_env_linux_ubuntu.html#ros-gazebo) ) 

The script automates the installtion instructions covered in this topic, installing everything you need: PX4, ROS, the Gazebo simulator, and MAVROS.

## Getting Started
### Install PX4 SITL(Only to Simulate)
Follow the instructions as shown in the [ROS with Gazebo Simulation PX4 Documentation](https://dev.px4.io/master/en/simulation/ros_interface.html)
To check if the necessary environment is setup correctly, you can run the gazebo SITL using the following command

```bash
cd <Firmware_directory>
DONT_RUN=1 make px4_sitl_default gazebo
```
To source the PX4 environment, run the following commands
	
```bash
cd <Firmware_directory>
source ~/catkin_ws/devel/setup.bash    # (optional)
source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
```

You can run the rest of the roslaunch files in the same terminal

```bash
 roslaunch px4 posix_sitl.launch
```

You will need to source the PX4 environment in every new terminal you open to launch mavros_controllers. 


### Installing The project

Create a catkin workspace or clone the existing repo:

This folder will probably be already created since the previous process would have created it. If it is not present, do:

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin init
catkin config --merge-devel
cd ~/catkin_ws/src
wstool init
```

###### Clone this repository

```bash
cd ~/catkin_ws/src
git clone https://github.com/Y-Roman/Drone.git
```

Build all the packages:

```bash
cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
```

## Running the code
Running the Gazebo Simulator
Note: Remember to source the workspace `setup.bash` before running any ROS Nodes.

Running the Gazebo Simulator
```bash
cd <catkin_ws>
source ~/catkin_ws/devel/setup.bash    # (necessary)
cd catkin_ws/bash
./1_gazebo.sh
```
To run Mavros in SITL
``` bash
cd <catkin_ws>
source ~/catkin_ws/devel/setup.bash    # (necessary)
cd catkin_ws/bash
./2_mavros.sh
```

To run Offboard Control
``` bash
cd <catkin_ws>
source ~/catkin_ws/devel/setup.bash    # (necessary)
cd catkin_ws/bash
./offboard.sh
```

## Nodes
`mavros_controllers` include the following packages.
### geometric_controller

The geometric controller publishes and subscribes the following topics.
- Parameters
    - /geometric_controller/mavname (default: "iris")
    - /geometric_controller/ctrl_mode (default: MODE_BODYRATE)
    - /geometric_controller/enable_sim (default: true)
    - /geometric_controller/enable_gazebo_state (default: false)
    - /geometric_controller/max_acc (default: 7.0)
    - /geometric_controller/yaw_heading (default: 0.0)
    - /geometric_controller/drag_dx (default: 0.0)
    - /geometric_controller/drag_dy (default: 0.0)
    - /geometric_controller/drag_dz (default: 0.0)
    - /geometric_controller/attctrl_constant (default: 0.2)
    - /geometric_controller/normalizedthrust_constant (default: 0.1)

- Published Topics
	- command/bodyrate_command ( [mavros_msgs/AttitudeTarget](http://docs.ros.org/api/mavros_msgs/html/msg/AttitudeTarget.html) )
	- reference/pose ( [geometry_msgs/PoseStamped](http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/PoseStamped.html) )

- Subscribed Topics
	- reference/setpoint ( [geometry_msgs/TwistStamped](http://docs.ros.org/api/geometry_msgs/html/msg/TwistStamped.html) )
	- /mavros/state ( [mavros_msgs/State](http://docs.ros.org/api/mavros_msgs/html/msg/State.html) )
	- /mavros/local_position/pose ( [geometry_msgs/PoseStamped](http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/PoseStamped.html) )
	- /gazebo/model_states( [gazebo_msgs/ModelStates](http://docs.ros.org/kinetic/api/gazebo_msgs/html/msg/ModelState.html) )
	- /mavros/local_position/velocity( [geometry_msgs/TwistStamped](http://docs.ros.org/api/geometry_msgs/html/msg/TwistStamped.html) )

### trajectory_publisher

Trajectory publisher publishes continous trajectories to the trajectory_controller.
- Parameters
    - /trajectory_publisher/initpos_x (default: 0.0)
    - /trajectory_publisher/initpos_y (default: 0.0)
    - /trajectory_publisher/initpos_z (default: 1.0)
    - /trajectory_publisher/updaterate (default: 0.01)
    - /trajectory_publisher/horizon (default: 1.0)
    - /trajectory_publisher/maxjerk (default: 10.0)
    - /trajectory_publisher/trajectory_type (default: 0)
    - /trajectory_publisher/number_of_primitives (default: 7)
    - /trajectory_publisher/shape_radius (default: 1.0)

- Published Topics
	- reference/trajectory ( [nav_msgs/Path](http://docs.ros.org/kinetic/api/nav_msgs/html/msg/Path.html) )
	- reference/setpoint ( [geometry_msgs/TwistStamped](http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/Twist.html) )

- Subscribed Topics
    - /trajectory_publisher/motionselector ([std_msgs/int32](http://docs.ros.org/api/std_msgs/html/msg/Int32.html));
    - /mavros/local_position/pose ( [geometry_msgs/PoseStamped](http://docs.ros.org/kinetic/api/geometry_msgs/html/msg/PoseStamped.html) )
    - /mavros/local_position/velocity( [geometry_msgs/TwistStamped](http://docs.ros.org/api/geometry_msgs/html/msg/TwistStamped.html) )