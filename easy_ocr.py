import os
import cv2

import easyocr 
# pip install easyocr

import numpy as np
import matplotlib.pyplot as plt


threshold = 0.25
reader = easyocr.Reader(["en"], gpu=False)

for i in range(0, len(os.listdir("test_images/"))):
    
    path = os.path.join("test_images", os.listdir("test_images/")[i])
    path_ = os.path.join("results", os.listdir("test_images/")[i])
    
    img = cv2.imread(path)
    text_ = reader.readtext(img)
    
    for t_, t in enumerate(text_):
        # print(t)
        bbox, text, score = t
        if score > threshold:
            cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)
            cv2.imwrite(path_, img)
