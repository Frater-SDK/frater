from dataclasses import dataclass, field
from logging import Logger

from .stream import OutputStream, StreamConfig
from ..logging import summarize
from ..logging.logger import LoggerConfig


@dataclass
class LoggerOutputStreamConfig(StreamConfig):
    logger_config: LoggerConfig = field(default_factory=LoggerConfig)


class LoggerOutputStream(OutputStream):
    def __init__(self, logger: Logger, multiline=True, data_type: type = None):
        super(LoggerOutputStream, self).__init__(data_type)
        self.logger = logger
        self.multiline = multiline

    def send(self, data):
        self.logger.info(summarize(data, self.multiline))
