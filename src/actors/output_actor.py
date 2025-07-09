import loguru
import pykka

from src.core.result import Result

class OutputActor(pykka.ThreadingActor):
    def  __init__(self, logger: loguru.Logger):
        super().__init__()
        self.logger = logger

    def on_receive(self, result: Result):
        result.tap(self.logger)