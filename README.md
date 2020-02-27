# Frater
> Frater - A Machine Learning and Data-Driven Systems Framework and Toolkit

Frater is a framework and toolkit whose goal is to simplify and streamline building 
large scale machine learning and data driven systems in research and production, as well as providing 
insight into a system at each step of the pipeline. Currently, transitioning a machine 
learning project from a research model to a production system requires a lot of time and effort. 
Even more, building systems that use more than one model can be an even bigger headache. 
Along with this transition process, there is a need to build out ways to retrieve and 
understand the data passing through the system.

Frater accomplishes its goal by providing a set of tools that abstract away the 
engineering side of machine learning for researchers, while still letting software engineers 
build powerful systems with the work done by their research counterparts. The plan is to provide a hub 
for any task that would come up in the process of building machine learning systems: 
- Running experiments
- Designing systems
- Developing new models and system components
- Analyzing and visualizing results
- Sharing and using pre-built components
- Resource management and configuration (GPU, CPU, memory)

Frater will also provide an API for developers and researchers to build components to use 
in a Frater system. Under the hood, Frater will run each component as a Docker container, 
which allows for portability and flexibility. All of this will be available through a web 
interface as well as a CLI. Frater will be able to be installed on to a local system, or 
deployed in a cloud environment. 

## Install
### Requirements:
- `python 3.7+`
 To install Frater, execute the following:
```shell 
pip install frater
```

## Getting Started

### Frater API
To start using the Frater API
```python
import frater
```

### Frater System

We’re currently looking for people interested in helping to make Frater’s vision into a 
reality. If you’re interested, contact John Henning at


- Email: [john.l.henning@ibm.com](mailto:john.l.henning@ibm.com)
- Slack (IBM): @john-l-henning 
- Twitter: [@johnlhenning](twitter.com/johnlhenning) 

Links:
- Code: https://github.com/frater-sdk/frater
- Docs: https://frater.readthedocs.io
