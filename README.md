# BSN implementation on ROS

This is a Body Sensor Network implementation on ROS. So far, the BSN was used for experimentation on solutions for adaptation on the Self-Adaptive Software Systems domain, refer to https://arxiv.org/pdf/1804.00994.pdf and https://arxiv.org/pdf/1905.02228.pdf for more information.  The following instructions will guide you to to compile, deploy and run the BSN on Linux Ubuntu 18.04 with ROS Melodic distributions. We have not yet tested on other distributions.

## Dependencies:
* [Ros Melodic](http://wiki.ros.org/melodic) which provides software libraries for BSN engines.
* [Cpp rest Sdk](https://github.com/Microsoft/cpprestsdk) which implements HTTP protocols on C++ (get, post...)
* [Lepton](https://github.com/rdinizcal/lepton) ("lightweight expression parser") is a small C++ library for parsing, evaluating, differentiating, and analyzing mathematical expressions.
* [Bsn Library](https://github.com/rdinizcal/libbsn)  provides the implementation of sensors, data fusers and emergency detection
* [Bsn arch](https://github.com/rdinizcal/arch)

## Instalation of dependencies: 
#### ROS:
Firstly it is required Ros Melodic installation. Our development team is sctrictly using Ubuntu 18.04 (Bionic). To install it please follow this [link](http://wiki.ros.org/melodic/Installation/Ubuntu).  
Also, it is strongly advised to use catkin for managing the ROS packages, refer to this [link](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) after installing ROS Melodic. As such you will need to create a catkin workspace. You can do so by following the steps:

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

#### CPP rest sdk:
In order to use Cpp rest sdk in a Cmake file it is required to build this dependencie source code.  
Firstly install its dependencies:

```
sudo apt-get install g++ git libboost-atomic-dev libboost-thread-dev libboost-system-dev libboost-date-time-dev libboost-regex-dev libboost-filesystem-dev libboost-random-dev libboost-chrono-dev libboost-serialization-dev libwebsocketpp-dev openssl libssl-dev ninja-build
```

Clone the repository:

```
git clone https://github.com/Microsoft/cpprestsdk.git casablanca
```

Build it:
```
cd casablanca
mkdir build.debug
cd build.debug
cmake -G Ninja .. -DCMAKE_BUILD_TYPE=Debug
ninja
```

#### Lepton:
1. Clone the repository in your desired folder cointaining Lepton and its dependencies

```
git clone https://github.com/rdinizcal/lepton
``` 

2. Then, create and enter build folder
```
cd lepton
``` 
``` 
mkdir build && cd build
``` 

3. Execute cmake from the build folder
``` 
cmake ..
``` 

4. Finally, compile and install lepton library
``` 
sudo make install
``` 

#### Libbsn:
1. Clone the repository in your desired folder cointaining Bsn library and its dependencies

```
git clone https://github.com/rdinizcal/libbsn
``` 

2. Then, create and enter build folder
```
cd libbsn
``` 
``` 
mkdir build && cd build
``` 

3. Execute cmake from the build folder
``` 
cmake ..
``` 

4. Finally, compile and install lepton library
``` 
sudo make install
``` 

#### Bsn Arch:
Firstly enter in catkin workspace:

```
cd ~/catkin_ws/src
```

Clone the repository:
```
git clone https://github.com/rdinizcal/arch
```

Finally build it:

```
cd .. 
catkin_make
```

Once ALL the dependencies have been successfully installed, you can proceed to the next steps.

## Compiling

1. Clone the repository inside the 'catkin_ws/src' directory:
```
cd ~/catkin_ws/src
git clone https://github.com/rdinizcal/bsn_ros
``` 

2. Then, compile under 'catkin_ws' directory:
```
cd ~/catkin_ws/ && 
catkin_make
``` 
## Configuration and Execution

3. Configure roslaunch files for personalized execution under '/catkin_ws/src/bsn_ros/configurations';

4. Execute the BSN either by executing the pre-set run.sh file, that executes all nodes, 
or use roslaunch x.launch to execute a single node:
```
cd ~/catkin_ws/src/bsn_ros/ && 
bash run.sh
``` 

## Authors

* **Ricardo D. Caldas** - https://github.com/rdinizcal
* **Eric B. Gil** - https://github.com/ericbg27/
* **Gabriel Levi** - https://github.com/gabrielevi10
* **Léo Moraes** - https://github.com/leooleo 
* **Samuel Couto** - https://github.com/SCouto97
* **Jorge Mendes** - https://github.com/luzmendesj 

Adviser: **Dr. Genaína Nunes Rodrigues** - https://cic.unb.br/~genaina/
