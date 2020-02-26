from dataclasses import dataclass, field
from logging import Handler
from typing import List

from kafka import KafkaProducer

from .config import HandlerConfig
from .factory import handler_factory, handler_config_factory
from ...io import get_kafka_serializer

__all__ = ['KafkaHandler', 'KafkaHandlerConfig']


@handler_config_factory.register('kafka')
@dataclass
class KafkaHandlerConfig(HandlerConfig):
    name: str = 'kafka_handler_config'
    topic: str = 'logging'
    servers: List[str] = field(default_factory=lambda: ['localhost:9092'])


@handler_factory.register('kafka')
class KafkaHandler(Handler):
    def __init__(self, config: KafkaHandlerConfig):
        """Initialize an instance of the kafka handler."""
        super(KafkaHandler, self).__init__(level=config.level)
        self.producer = KafkaProducer(bootstrap_servers=config.servers, value_serializer=get_kafka_serializer(),
                                      linger_ms=10)
        self.topic = config.topic

    def emit(self, record):
        """Emit the provided record to the kafka_client producer."""
        # drop kafka logging to avoid infinite recursion
        if 'kafka.' in record.name:
            return

        try:
            # apply the logger formatter
            msg = self.format(record)
            self.producer.send(self.topic, {'message': msg})
            self.flush(timeout=1.0)
        except Exception as e:
            Handler.handleError(self, record)

    def flush(self, timeout=None):
        """Flush the objects."""
        self.producer.flush(timeout=timeout)

    def close(self):
        """Close the producer and clean up."""
        self.acquire()
        try:
            if self.producer:
                self.producer.close()

            Handler.close(self)
        finally:
            self.release()
