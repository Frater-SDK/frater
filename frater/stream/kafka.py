from kafka import KafkaProducer, KafkaConsumer

from frater.io import get_kafka_serializer, get_kafka_deserializer
from frater.stream.stream import OutputStream, InputStream


class KafkaOutputStream(OutputStream):
    def __init__(self, topic, stream_type=None, servers=None):
        super(KafkaOutputStream, self).__init__(stream_type)
        if servers is None:
            servers = ['localhost:9092']
        self._producer = KafkaProducer(bootstrap_servers=servers,
                                       value_serializer=get_kafka_serializer())
        self.topic = topic

    def send(self, data):
        self._producer.send(self.topic, data).get()

    def close(self):
        self._producer.close()


class KafkaInputStream(InputStream):
    def __init__(self, topic, stream_type=None, servers=None):
        super(KafkaInputStream, self).__init__(stream_type)
        if servers is None:
            servers = ['localhost:9092']

        self._consumer = KafkaConsumer(topic, bootstrap_servers=servers,
                                       value_deserializer=get_kafka_deserializer(self.stream_type))
        self._topic = topic

    def __next__(self):
        return next(self._consumer)

    def __iter__(self):
        for msg in self._consumer:
            yield msg.value

    def close(self):
        self._consumer.close()
