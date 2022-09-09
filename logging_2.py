import logging
from logging.config import fileConfig

fileConfig("logging-config.ini")
logging.info("Hello there!")