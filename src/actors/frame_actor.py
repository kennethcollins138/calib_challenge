import pykka

from src.core.result import Result

class FrameSourceActor(pykka.ThreadingActor):
    def __init__(self, logger, next_actor):
        super().__init__()
        self.next_actor = next_actor
        self.logger = logger

    def on_receive(self, message):
        # TODO: break into frame define stricter type
        # Preprocessing should take place here
        if isinstance(message, Result):
            self.next_actor.tell(message)
        else:
            self.next_actor.tell(Result(value=message))