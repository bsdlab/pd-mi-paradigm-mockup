from functools import partial

from dareplane_utils.default_server.server import DefaultServer
from fire import Fire

from mi_paradigm.main import Paradigm, run_mi_task
from mi_paradigm.utils.logging import logger


def main(port: int = 8080, ip: str = "127.0.0.1", loglevel: int = 30):
    # Implement primary commands here

    pdm = Paradigm()

    logger.setLevel(loglevel)
    logger.debug("Paradigm created")

    pcommand_map = {"RUN": partial(run_mi_task, pdm)}

    logger.debug("Pcommands setup")

    server = DefaultServer(
        port, ip=ip, pcommand_map=pcommand_map, name="mi_paradigm"
    )
    server.logger = logger

    # initialize to start the socket
    server.init_server()
    # start processing of the server
    server.start_listening()

    return 0


if __name__ == "__main__":
    Fire(main)
