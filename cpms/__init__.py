__version__ = '0.0.1'

import logging

logger = logging.getLogger("cpms")
logging.basicConfig(
    filename="logs.log", 
    encoding='utf-8', 
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


from .conf import config
from .util import mkdir, rmtree, pretty_print_cmdline