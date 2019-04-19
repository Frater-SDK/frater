from kafka import KafkaProducer, KafkaConsumer

from frater.io.serialization import get_kafka_serializer, get_kafka_deserializer
from frater.stream.stream import OutputStream, InputStream


class KafkaOutputStream(OutputStream):
    def __init__(self, stream_type, topic, bootstrap_servers=None):
        super(KafkaOutputStream, self).__init__(stream_type)
        if bootstrap_servers is None:
            bootstrap_servers = ['localhost:9092']
        self._producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                       value_serializer=get_kafka_serializer(self.stream_type))
        self.topic = topic

    def send(self, data):
        super(KafkaOutputStream, self).send(data)
        self._producer.send(self.topic, data)


class KafkaInputStream(InputStream):
    def __init__(self, stream_type, topic, bootstrap_servers=None):
        super(KafkaInputStream, self).__init__(stream_type)
        if bootstrap_servers is None:
            bootstrap_servers = ['localhost:9092']

        self._consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers,
                                       value_deserializer=get_kafka_deserializer(self.stream_type))
        self._topic = topic

    def __next__(self):
        return next(self._consumer)

    def __iter__(self):
        for msg in self._consumer:
            yield msg.value
