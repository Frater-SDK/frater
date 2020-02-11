from logging import Logger

from .stream import OutputStream
from ..logging import summarize


class LoggerOutputStream(OutputStream):
    def __init__(self, logger: Logger, multiline=True, data_type: type = None):
        super(LoggerOutputStream, self).__init__(data_type)
        self.logger = logger
        self.multiline = multiline

    def send(self, data):
        self.logger.info(summarize(data, self.multiline))
