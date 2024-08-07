# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e6suegQgsFoZOdHs8tMQgL4RBg4lHet_
"""

!nvidia-smi

!pip install ultralytics

import os
HOME = os.getcwd()
print(HOME)

from ultralytics import YOLO
import os
from IPython.display import display, Image
from IPython import display
display.clear_output()
!yolo mode-checks

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="W7zBp6P0SLLm7pzwjLRQ")
project = rf.workspace("aiforengineer").project("ai_for_engineer_class")
version = project.version(3)
dataset = version.download("yolov8")

!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=100 imgsz=640

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename='runs/detect/train2/confusion_matrix.png', width=600)

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename='runs/detect/train2/results.png', width=600)

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
Image(filename='runs/detect/train2/val_batch0_pred.jpg', width=600)

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
!yolo task=detect mode=val model={HOME}/runs/detect/train2/weights/best.pt source={dataset.location}/data.yaml

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
!yolo task=detect mode=predict model={HOME}/runs/detect/train2/weights/best.pt source={dataset.location}/test/images

import glob
from IPython.display import Image, display
for imageName in glob.glob('runs/detect/predict/*.jpg'):
    display(Image(filename=imageName))

# Commented out IPython magic to ensure Python compatibility.
# %cd {HOME}
!yolo task=detect mode=predict model={HOME}/runs/detect/train2/weights/best.pt source=https://www.youtube.com/watch?v=oIPoA22qMvE