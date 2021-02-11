from actions.logaction import logger
from core.config import Config
from flask import Flask

logger.info("Start db init")
conn = Config().get_db()
logger.info("db init success")

app = Flask(__name__)

from core.routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5090)
