# Just wrap the code with fire to also have a CLI
from fire import Fire

# The modules logger is used everywhere necessary. Note this logger will usually only have a NetworkHandler.
# If you want to log to the console, you need to add a StreamHandler to it.
from mymodule.utils.logging import logger


# We will link this function to the server later, so we want to return an int, a thread or a subprocess
# Int this exmaple I will use and int
def run_hello_world(n: int = 5) -> int:
    logger.setLevel(20)

    # We add a basic StreamHandler here for demonstration purposes
    # In an actual Dareplane setup, the modules would be setup from the control
    # room which is also spawning a central logging server at port 9020 (default).
    import logging

    logger.addHandler(logging.StreamHandler())

    for i in range(n):
        logger.info("Hello World!")
    return 0


if __name__ == "__main__":
    Fire(run_hello_world)
