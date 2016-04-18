"""
The sinks package contains all the sink modules, plus a decorator and base
class in `sinks.sink`.

Add any new sinks here with `from . import <name>`.
"""

from . import ftdi, tkinter, leonardo
from .sink import loaded_sinks
