# Frater

Frater is an Machine Learning System Framework and SDK (Currently focused on activity detection) for researchers 
and developers to easily deploy their components into a system and quickly prototype and get results.
Frater's main goal is to provide tools that are easy to use for researchers and engineers alike and allow them to 
spend less time dealing with headaches of system design, and more time 
running experiments and discovering the next state of the art.

Frater is library agnostic, so developers are free to use any standard tools for machine learning,
deep learning, computer vision, etc. Out of the box, we provide a quick docker compose deploy


## About
Frater is divided into two main components:  

- The Frater system which contains a suite of tools to get you off the ground with deploying your system 
- The Frater API for developing components to work with the Frater system

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

As you develop your own system,  

## Frater API

The Frater API provides developers a way to build components for their Frater system.  
See [Getting Started](getting_started.md) for a basic introduction. The API can also be used
standalone outside of the Frater system, however more configuration is required by the
developer to have it communicate with other modules.
 

#### Note
*The Frater API at the moment only supports Python 3.6+. The decision to not support Python 2.x was made 
due to it being [deprecated soon](https://pythonclock.org/). However, we plan to build the API for other languages such as C and C++, as
these are the other most common languages for machine learning models and systems.* 

