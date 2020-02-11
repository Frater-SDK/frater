from dataclasses import dataclass, field
from typing import List

from kafka import KafkaProducer, KafkaConsumer

from .stream import OutputStream, InputStream
from ..config import Config
from ..io import get_kafka_serializer, get_kafka_deserializer


@dataclass
class KafkaOutputStreamConfig(Config):
    topic: str = ''
    data_type: str = ''
    servers: List[str] = field(default_factory=lambda: ['localhost:9092'])


class KafkaOutputStream(OutputStream):
    def __init__(self, topic, data_type=None, servers=None, serializer=None):
        super(KafkaOutputStream, self).__init__(data_type)
        if servers is None:
            servers = ['localhost:9092']

        if serializer is None:
            serializer = get_kafka_serializer()

        self._producer = KafkaProducer(bootstrap_servers=servers,
                                       value_serializer=serializer)
        self.topic = topic

    def send(self, data):
        self._producer.send(self.topic, data).get()

    def close(self):
        self._producer.close()


class KafkaInputStream(InputStream):
    def __init__(self, *topics, data_type=None, servers=None, deserializer=None):
        super(KafkaInputStream, self).__init__(data_type)
        if servers is None:
            servers = ['localhost:9092']

        if deserializer is None:
            deserializer = get_kafka_deserializer()

        self._consumer = KafkaConsumer(*topics, bootstrap_servers=servers,
                                       value_deserializer=deserializer)
        self.topics = list(topics)

    def __iter__(self):
        for msg in self._consumer:
            yield msg.value

    def close(self):
        self._consumer.close()
