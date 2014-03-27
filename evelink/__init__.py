"""EVELink - Python bindings for the EVE API."""

import logging

__version__ = "0.3.1"

from evelink import account
from evelink import api
from evelink import char
from evelink import constants
from evelink import corp
from evelink import eve
from evelink import map
from evelink import server

# Implement NullHandler because it was only added in Python 2.7+.
class NullHandler(logging.Handler):
    def emit(self, record):
        pass

# Create a logger, but by default, have it do nothing
_log = logging.getLogger('evelink')
_log.addHandler(NullHandler())

__all__ = [
  "account",
  "api",
  "char",
  "constants",
  "corp",
  "eve",
  "map",
  "parsing",
  "server",
]
