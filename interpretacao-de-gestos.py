import cv2 #importando o OpenCV
import os
import numpy as np
import math
cap = cv2.VideoCapture(0)

while(1):
    
    try:
        
        ret, frame = cap.read()