# YOLOv5 by Ultralytics, GPL-3.0 license
"""
Common modules
"""

import json
import math
import platform
from collections import OrderedDict, namedtuple
from copy import copy
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
import requests
import torch
import torch.nn as nn
import yaml
from PIL import Image
from torch.cuda import amp

from utils.datasets import exif_transpose, letterbox