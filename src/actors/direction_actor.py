import loguru
import pykka

from src.core.result import Result

class DirectionActor(pykka.ThreadingActor):
    """
    DirectionActor is the last stage of the data postprocessing pipeline.
    It is responsible for estimating the direction of the movement.
    """
    def __init__(self, next_actor, logger: loguru.Logger):
        super().__init__()
        self.next_actor = next_actor
        self.logger = logger

    @staticmethod
    def estimate_direction(self, flow):
        return {
            "yaw": 0,
            "pitch": 0
        }

    def on_receive(self, result: Result):
        result.map(self.estimate_direction) \
              .tap(lambda msg: print(f"[DirectionActor] {msg}")) \
              .map(lambda direction: self.next_actor.tell(Result(value=direction)))
