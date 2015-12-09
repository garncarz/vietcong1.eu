import os

from .base import *
from .aws import *

if 'DEBUG' in os.environ and os.environ['DEBUG']:
    from .development import *

try:
    from .local import *
except ImportError:
    pass
