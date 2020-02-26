from dataclasses import dataclass, field
from typing import List

from kafka import KafkaProducer, KafkaConsumer

from .factory import *
from .stream import OutputStream, InputStream, StreamConfig
from ..io import get_kafka_serializer, get_kafka_deserializer


@input_stream_configs.register('kafka')
@dataclass
class KafkaInputStreamConfig(StreamConfig):
    topics: List[str] = field(default_factory=list)
    servers: List[str] = field(default_factory=lambda: ['localhost:9092'])


@input_stream_factory.register('kafka')
class KafkaInputStream(InputStream):
    def __init__(self, config: KafkaInputStreamConfig):
        super(KafkaInputStream, self).__init__(config)

        deserializer = get_kafka_deserializer()

        self._consumer = KafkaConsumer(*self.config.topics, bootstrap_servers=self.config.servers,
                                       value_deserializer=deserializer)

    def __iter__(self):
        for msg in self._consumer:
            yield msg.value

    def close(self):
        self._consumer.close()


@output_stream_configs.register('kafka')
@dataclass
class KafkaOutputStreamConfig(StreamConfig):
    topic: str = ''
    servers: List[str] = field(default_factory=lambda: ['localhost:9092'])


@output_stream_factory.register('kafka')
class KafkaOutputStream(OutputStream):
    def __init__(self, config: KafkaOutputStreamConfig):
        super(KafkaOutputStream, self).__init__(config)

        serializer = get_kafka_serializer()
        self._producer = KafkaProducer(bootstrap_servers=self.config.servers,
                                       value_serializer=serializer)

    def send(self, data):
        self._producer.send(self.config.topic, data).get()

    def close(self):
        self._producer.close()
