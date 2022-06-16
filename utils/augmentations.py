<<<<<<< HEAD
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
=======
# YOLOv5 by Ultralytics, GPL-3.0 license
>>>>>>> 398b673144da8464a02447002def20fcc3a2f949
"""
Image augmentation functions
"""

import math
import random

import cv2
import numpy as np

<<<<<<< HEAD
from utils.general
=======
from utils.general import LOGGER, check_version, colorstr, resample_segments, segment2box
from utils.metrics import bbox_ioa
>>>>>>> 398b673144da8464a02447002def20fcc3a2f949
