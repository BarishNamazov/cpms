import logging
from cpms.grading.Sandbox import SandboxBase

logger = logging.getLogger("demo")
logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.DEBUG)

logger.debug("hello")
logger.warning("yoo")
