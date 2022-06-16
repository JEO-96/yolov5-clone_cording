# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
General utils
"""

import contextlib
import glob
import inspect
import logging
import math
import os
import platform
import random
import re
import shutil
import signal
import time
import urllib
from datetime import datetime
from itertools import repeat
from multiprocessing.pool import ThreadPool
from pathlib import Path
from subprocess import check_output
from typing import Optional
from zipfile import ZipFile

import cv2
import numpy as np
import pandas as pd
import pkg_resources as pkg
import torch
import torchvision
import yaml

from utils.downloads import gsutil_getsize
from utils.metrics import box_iou, fitness

# Settings
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
DATASETS_DIR = ROOT.parents / 'datasets'  # YOLOv5 datasets directory
NUM_THREADS = min(8, max(1, os.cpu_count() - 1))  # number of YOLOv5 multiprocessing threads
AUTOINSTALL = str(os.getenv('YOLOv5_AUTOINSTALL', True)).lower() == 'true'  # global auto-install mode
VERBOSE = str(os.getenv('YOLOv5_VERBOSE', True)).lower() == 'true'  # global verbose mode
FONT = 'Arial.ttf'  # https://ultralytics.com/assets/Arial.ttf

torch.set_printoptions(linewidth=320, precision=5, profile='long')
np.set_printoptions(linewidth=320, formatter={'float_kind': '{:11.5g}'.format})  # format short g, %precision=5
pd.options.display.max_columns = 10
cv2.setNumThreads(0)  # prevent OpenCV from multithreading (incompatible with PyTorch DataLoader)
os.environ['NUMEXPR_MAX_THREADS'] = str(NUM_THREADS)  # NumExpr max threads
os.environ['OMP_NUM_THREADS'] = str(NUM_THREADS)  # OpenMP max threads (Pytorch and SciPy)


def is_kaggle():
    # Is environment a Kaggle Notebook?
    try:
        assert os.environ.get('PWD') == '/kaggle/working'
        assert os.environ.get('KAGGLE_URL_BASE') == 'https://www.kaggle.com'
        return True
    except AssertionError:
        return False


def is_writeable(dir, test=False):
    # Return True if directory has write permissions, test opening a file with write permissions if test=True
    if test:  # method 1
        file = Path(dir) / 'tmp.txt'
        try:
            with open(file, 'w'):  # open file with write permissions
                pass
            file.unlink()  # remove file
            return True
        except OSError:
            return False
    else:  # method 2
        return os.access(dir, os.R_OK)  # possible issues on Windows
