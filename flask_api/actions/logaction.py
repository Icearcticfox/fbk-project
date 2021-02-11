import logging

logging.basicConfig(level=logging.INFO)
logging.debug("This will get logged")

logger = logging.getLogger("web_app")
