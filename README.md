# turtle_chaser homework

>Assignment for Intelligent Systems course @LETI university 2022/23 academic session

### Contributors
**Yaseer Buruji Ibrahim** - ibyaseer@mail.ru

[Buruji Yaseer](https://github.com/Meizzy)


### About Project
A ROS node that manipulates the turtlesim node. By default  when the node is launched, a turtle named `turtle1` approaches a turtle2 named `victim`, that has been spawned in a random position. Further using the function of the `turtle_teleop_key`, the position of the `victim` can be manipulated using inputs from the keyboard, and the `turtle1` in turn, chases the `victim`.

### Prerequisites
*Python 3.0
*ROS
*Turtlesim


#### Installation

Clone the repository

```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/Meizzy/turtle_chaser
```
build ROS packages and update the environment

```sh
$ catkin build
$ re.
```

#### Usage

The execution can be started simply using the following command:

```bash
$ roslaunch turtle_chaser ready_launch.launch
```

The file `ready_launch.launch` is a launch file that contains the instruction to implement the nodes. 
