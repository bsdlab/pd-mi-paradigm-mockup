# MI Paradigm mockup

This is a minimal example of a motor imagery paradigm module implemented for [Dareplane](https://github.com/bsdlab/Dareplane).

For testing, you can use either of:

- direct invocation via python `python -m pi_paradigm.main`;
- or via the server `python -m api.server` + `telnet` connection;
- or via the [`control_room`](https://github.com/bsdlab/dp-control-room) module

You should see a gray [psychopy](https://www.psychopy.org/) window showing up, on which a fixation cross and the letters `L` and `R` are displayed in a light red color.

The intention of this module is to outline how one could build a very simple paradigm and integrate it into the Dareplane system.
