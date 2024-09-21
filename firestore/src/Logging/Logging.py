import datetime
import os
from logging import ERROR, INFO, FileHandler, Formatter, StreamHandler, getLogger

logger = getLogger(__name__)
logger.setLevel(INFO)

sh = StreamHandler()
sh.setLevel(INFO)
sh_format = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(sh_format)
logger.addHandler(sh)

log_file_name = f"log/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
os.makedirs(os.path.dirname(log_file_name), exist_ok=True)

fh = FileHandler(log_file_name)
fh.setLevel(ERROR)
fh_formatter = Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s")
fh.setFormatter(fh_formatter)
logger.addHandler(fh)
