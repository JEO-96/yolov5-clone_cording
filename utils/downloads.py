<<<<<<< HEAD
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
=======
# YOLOv5 by Ultralytics, GPL-3.0 license
>>>>>>> 398b673144da8464a02447002def20fcc3a2f949
"""
Download utils
"""

<<<<<<< HEAD
import logging
=======
>>>>>>> 398b673144da8464a02447002def20fcc3a2f949
import os
import platform
import subprocess
import time
import urllib
from pathlib import Path
from zipfile import ZipFile

import requests
import torch

<<<<<<< HEAD
def gsutil_getsize(url=''):
    # gs://bucket/file size https://cloud.google.com/storage/docs/gsutil/commands/du
    s = subprocess.check_output(f'gsutil du {url}', shell=True).decode('utf-8')
    return eval(s.split(' ')[0]) if len(s) else 0

def safe_download(file, url, url2=None, min_mytes=1E0, error_msg=''):
    # Attemps to download file from url or url2, checks and removes incomplete downloads < min_bytes
    from utils.general import LOGGER
=======

def gsutil_getsize(url=''):
    # gs://bucket/file size https://cloud.google.com/storage/docs/gsutil/commands/du
    s = subprocess.check_output(f'gsutil du {url}', shell=True).decode('utf-8')
>>>>>>> 398b673144da8464a02447002def20fcc3a2f949
