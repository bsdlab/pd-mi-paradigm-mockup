import random
import time

import pylsl
from fire import Fire
from psychopy.visual import TextStim, Window

from mi_paradigm.utils.logging import logger

logger.setLevel(10)

BG_COLOR = (0, 0, 0)
TEXT_COLOR = (1, 0, 0)

t_pre = 1
t_show = 1
t_post = 1


class Outlet:
    def __init__(self):
        self.logger = logger
        info = pylsl.StreamInfo(name="markers", channel_format="string")
        self.outlet = pylsl.StreamOutlet(info)

    def push_sample(self, sample: str):
        self.logger.debug(f"Pushing sample {sample}")
        self.outlet.push_sample([sample])


class Paradigm:
    def __init__(self):
        self.open_window()

    def open_window(self):
        self.win = Window((800, 600), screen=1, color=BG_COLOR)
        self.rstim = TextStim(win=self.win, text="R", color=TEXT_COLOR)
        self.lstim = TextStim(win=self.win, text="L", color=TEXT_COLOR)
        self.fix_cross = TextStim(win=self.win, text="+", color=TEXT_COLOR)

    def close_window(self):
        self.win.close()


def run_mi_task(paradigm: Paradigm | None = None, nrep: int = 4) -> int:
    # Create on the fly if not specified, to allow api.server to manage the
    # instance
    if paradigm is None:
        paradigm = Paradigm()

    outlet = Outlet()
    win = paradigm.win
    fix_cross = paradigm.fix_cross
    rstim = paradigm.rstim
    lstim = paradigm.lstim

    fix_cross.draw()
    win.flip()

    directions = ["R"] * (nrep // 2) + ["L"] * (nrep // 2)
    random.shuffle(directions)

    for i, dir in enumerate(directions):
        fix_cross.draw()
        win.flip()
        outlet.push_sample("new_trial")

        time.sleep(t_pre)

        if dir == "R":
            rstim.draw()
        else:
            lstim.draw()

        win.flip()
        outlet.push_sample(dir)

        # clear screen and sleep for post
        time.sleep(t_show)
        win.flip()
        outlet.push_sample("cleared")

        win.flip()
        time.sleep(t_post)

    return 0


if __name__ == "__main__":
    Fire(run_mi_task)
