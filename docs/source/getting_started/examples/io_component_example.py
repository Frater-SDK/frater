from dataclasses import dataclass, field
from typing import List

from frater.component import ComponentState, IOComponent, IOComponentConfig, ComponentBuilder
from frater.stream import InputStream, OutputStream, StreamConfig, StreamState


@dataclass
class SummationComponentState(ComponentState):
    total: int = 0


class SummationComponent(IOComponent):
    def __init__(self, config: IOComponentConfig, input_stream: InputStream, output_stream: OutputStream):
        super(SummationComponent, self).__init__(config, input_stream, output_stream)

    def init_state(self):
        return SummationComponentState()

    def process(self, data):
        self.state.total += data
        return self.state.total


@dataclass
class IterableInputStreamConfig(StreamConfig):
    data: List[int] = field(default_factory=list)


class IterableInputStream(InputStream):
    def __init__(self, config: IterableInputStreamConfig):
        super(IterableInputStream, self).__init__(config)

    def __iter__(self):
        yield StreamState.START
        yield from self.config.data
        yield StreamState.END


class PrintOutputStream(OutputStream):
    def send(self, data):
        print(data)


def main():
    input_stream = IterableInputStream(
        IterableInputStreamConfig.from_dict({'data': list(range(10))}))
    output_stream = PrintOutputStream()
    component = ComponentBuilder.build(SummationComponent, IOComponentConfig(), input_stream, output_stream)

    component.run()


if __name__ == '__main__':
    main()
