from src.actors import OutputActor, DirectionActor, FlowActor, FrameSourceActor
from src.configs import setup_logger

def main():
    print("Hello from calib-challenge!")

    # TODO: initialize config loader based off of environment and input from cli
    # pass args to logger and actors
    logger = setup_logger(name="calib-challenge")

    # initialize actors
    # debating about splitting each actor into its separate logger and have them bubble out

    output_actor = OutputActor(logger)
    direction_actor = DirectionActor(logger=logger, next_actor=output_actor)
    flow_actor = FlowActor(logger=logger, next_actor=direction_actor)
    frame_actor = FrameSourceActor(logger=logger, next_actor=flow_actor)

if __name__ == "__main__":
    main()
