# Getting Started

The core classes that frater provides are `Stream` and `Task` as well as
some classes for activity detection systems.

## Streams
The Stream class provides simple interfaces for sending and receiving data. The source of this data 
depends on the implementation of the stream classes. 

Streams have specific types associated with them

We've provided Kafka Streams that wrap the Kafka API for sending or receiving data on a Kafka topic. 
## Tasks

The Task class is focused on abstracting away the pain of communicating with other components of
the system, and focusing on the computation that needs to be done. Below is an example task
class using the Task abstract class
 
```python
from frater.task import Task
from frater.stream import InputStream, OutputStream

class ExampleTask(Task):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(ExampleTask, self).__init__()
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

For more examples, see [Task Examples](examples.md#task)

