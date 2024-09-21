import datetime
import os
from logging import ERROR, INFO, FileHandler, Formatter, StreamHandler, getLogger

import colorlog

logger = getLogger(__name__)
logger.setLevel(INFO)

stream = StreamHandler()
stream.setLevel(INFO)
stream_format = colorlog.ColoredFormatter(
    "%(asctime)s | %(log_color)s%(levelname)-8s%(reset)s | %(funcName)-15s | %(message)s",
    datefmt="%H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)
stream.setFormatter(stream_format)
logger.addHandler(stream)

log_file_name = f"log/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

file = FileHandler(log_file_name)
file.setLevel(ERROR)
file_formatter = Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s")
file.setFormatter(file_formatter)
logger.addHandler(file)
