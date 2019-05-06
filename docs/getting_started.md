# Getting Started

The core classes that frater provides are `Stream` and `Task` as well as
some classes for activity detection systems.

## Core
The `core` package contains classes and factory methods (and eventually related methods using these classes) for 
core concepts related to activity detection. These include

- [`Activity`](api/core.md#fratercoreactivity)
- [`Object`](api/core.md#fratercoreobject)
- [`Frame`](api/core.md#fratercoreframe)
- [`Trajectory`](api/core.md#fratercoretrajectory)
- [`BoundingBox`](api/core.md#fratercorebounding_box)
- [`TemporalRange`](api/core.md#fratercoretemporal_range)

The schema for these classes can be found in the API documentation. 

## Streams
The Stream class provides simple interfaces for sending and receiving data. The source of this data 
depends on the implementation of the stream classes. 

A stream has specific types associated with them so that there is a guarantee of what kind of data is
sent to or received from the stream.

There are two types of base stream types: `InputStream` and `OutputStream`

Below is an example implementation of these streams

```python
from frater.stream import InputStream, OutputStream

class ExampleDataType:
    def __init__(self):
        self.value = 'example'
    
class ExampleInputStream(InputStream):
    def __init__(self, stream_type):
        super().__init__(stream_type)
        self.examples = [ExampleDataType()] * 5

    def __next__(self) -> ExampleDataType():
        return next(self.examples)

    def __iter__(self):
        for example in self.examples:
            yield example


class ExampleOutputStream(OutputStream):
    def send(self, example: ExampleDataType):
        print(example.value, 'test')
        

def main():
    input_stream = ExampleInputStream(ExampleDataType)
    output_stream = ExampleOutputStream(ExampleDataType)
    
    for example in input_stream:
        output_stream.send(example)
        # can also pass example by calling 
        # output_stream(example)
        
if __name__ == '__main__':
    main()

```    
**Output**

```text
example test
example test
example test
example test
example test
```

We've also provided Kafka Streams which are fully implemented streams that wrap the Kafka API for 
sending or receiving data on a Kafka topic. This is the default method of communication between 
components for the Frater system.
 
## Tasks

The Task class is focused on abstracting away the pain of communicating with other components of
the system, and focusing on the computation that needs to be done. Below is an example task
class using the Task abstract class
 
```python
from frater.task import Task
from frater.stream import InputStream, OutputStream

class ExampleTask(Task):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(ExampleTask, self).__init__(input_stream.stream_type, output_stream.stream_type)
        self._input_stream = input_stream
        self._output_stream = output_stream

    @property
    def input_stream(self):
        return self._input_stream

    @property
    def output_stream(self):
        return self._output_stream   
    
    def run(self):
        # receive data from input stream
        for data in self.input_stream:
            output = self.perform_task(data)
            # send data to output stream
            self.output_stream(output)
        
    def perform_task(self, data):
        # do something with the data
        return self.do_something(data)
        
    def do_something(self, data):
        return data        

```

In this example, the task receives data from the input stream and sends data to the output stream.
This isn't necessary, and can vary based on the task at hand. For example, you could only receive some input 

For more examples, see [Task Examples](examples/task.md)

