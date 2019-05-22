# Frater

Frater is an Machine Learning System Framework and SDK (Currently focused on activity detection) for researchers 
and developers to easily deploy their components into a system and quickly prototype and get results.
Frater's main goal is to provide tools that are easy to use for researchers and engineers alike and allow them to 
spend less time dealing with headaches of system design, and more time running experiments and 
discovering the next state of the art.

Frater is library agnostic, so developers are free to use any standard tools for machine learning,
deep learning, computer vision, NLP, etc. By providing an ecosystem which encourages researchers to focus just on 
the research problem at hand, we hope Frater can be the catalyst for helping explore innovative 
and novel ideas on the system level, the same way the GPUs were the catalyst on the computation and algorithmic level.

## About
Frater is divided into two main components:  

- The Frater system which is a set of preconfigured tools to get you off the ground when deploying your system 
- The Frater API for developing components to work with the Frater system

At the moment, the main focus of development is the Frater API and specifically libraries for developing 
activity detection systems, as this project originated as a framework for teams participating 
in the [DIVA](https://www.iarpa.gov/index.php/research-programs/diva) research program. 

#### Note
*Both the Frater system and API are still under active development, so be aware of any changes
made. These will be reported in a changelog whenever a new release is available*  

## Frater System
The base system includes the following components:  

 - Database for saving and loading results - `MongoDB`  
 - Message Broker for message passing between components - `Apache Kafka`  
 
### Planned features:

 - Web UI for result visualization and analysis
 - Running custom experiments through Web UI
 - Model/Component Zoo for getting available components
 
### Planned Out of the Box Components:

 - Video cache and server for handling video stream input
 - Off the shelf object detection
 - Off the shelf activity detection
 
### System Requirements
These requirements are for running the full system out of the box:  

- `docker`  
- `docker-compose`  

As you develop your own system, you can pick and choose which components are used in your system. For example, 

## Frater API

The Frater API provides developers a way to build components for their Frater system.  
See [Getting Started](getting_started.md) for a basic introduction. The API can also be used
standalone outside of the Frater system, however more configuration is required by the
developer to have it communicate with other modules.
 

#### Note
*The Frater API at the moment only supports Python 3.6+. The decision to not support Python 2.x was made 
due to it being [deprecated soon](https://pythonclock.org/). However, we plan to build the API for other languages such as C and C++, as
these are the other most common languages for machine learning models and systems.* 

