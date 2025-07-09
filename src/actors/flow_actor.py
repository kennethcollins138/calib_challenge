import loguru

from src.core.result import Result

class FlowActor:
    """
    FlowActor will server as the flow manager between frames tracking things like moving objects etc.
    These vectors are crucial to the calculation of the movement vector.
    """
    def __init__(self, next_actor, logger: loguru.Logger):
        super().__init__()
        self.logger = logger
        self.next_actor = next_actor

    @staticmethod
    def estimate_flow(self):
        pass
        # TODO: finish implementation

    def on_receive(self, result: Result):
        result.map(self.estimate_flow).tap(lambda msg: print(f"[FlowActor] {msg}")).map(
            lambda flow: self.next_actor.tell(Result(value=flow))
        )