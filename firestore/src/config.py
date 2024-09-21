import datetime
import os

FolderYear = datetime.datetime.now().strftime("%Y")
FolderDate = datetime.datetime.now().strftime("%m-%d")
FileName = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOG_FILE_PATH = f".log/{FolderYear}/{FolderDate}/{FileName}"
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
