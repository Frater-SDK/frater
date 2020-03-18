from dataclasses import dataclass, field

from pymongo import MongoClient

from .factory import *
from .stream import InputStream, OutputStream, StreamConfig
from ..io import json_to_frater, frater_to_json


@output_stream_configs.register('mongo')
@input_stream_configs.register('mongo')
@dataclass
class MongoStreamConfig(StreamConfig):
    name: str = 'mongo_stream_config'
    host: str = 'localhost'
    port: int = 27017
    db: str = 'db'
    collection: str = 'collection'
    filter: dict = field(default_factory=dict)


@input_stream_factory.register('mongo')
class MongoInputStream(InputStream):
    def __init__(self, config: MongoStreamConfig):
        super(MongoInputStream, self).__init__(config)
        self.client = MongoClient(self.config.host, self.config.port)
        self.cursor = self.collection.find(filter=self.config.filter)

    @property
    def db(self):
        return self.client[self.config.db]

    @property
    def collection(self):
        return self.db[self.config.collection]

    def __next__(self):
        if self._closed:
            raise StopIteration('Mongo Input Stream Closed')

        return json_to_frater(next(self.cursor))

    def __iter__(self):
        return self

    def reset(self):
        self.cursor = self.collection.find(filter=self.config.filter)

    def close(self):
        super(MongoInputStream, self).close()
        self.cursor.close()
        self.client.close()


@output_stream_factory.register('mongo')
class MongoOutputStream(OutputStream):
    def __init__(self, config: MongoStreamConfig):
        super(MongoOutputStream, self).__init__(config)
        self.client = MongoClient(self.config.host, self.config.port)

    @property
    def db(self):
        return self.client[self.config.db]

    @property
    def collection(self):
        return self.db[self.config.collection]

    def send(self, data):
        self.collection.insert_one(frater_to_json(data))

    def close(self):
        super(MongoOutputStream, self).close()
        self.client.close()
