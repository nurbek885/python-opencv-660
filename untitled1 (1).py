# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ogi49i8CmbqI4wBltJIt-Zws2TX6yyAM
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread('rasm.png')
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread('picture.jpg')
rasm1=cv2.imread('rasm.jpg')
rasm2=cv2.imread('surat.jpg')
rasm3=cv2.imread('rasm.jpg_wh860.jpg')
rasm4=cv2.imread('rasmlar.jpg')
cv2_imshow(rasm)
cv2_imshow(rasm1)
cv2_imshow(rasm2)
cv2_imshow(rasm3)
cv2_imshow(rasm4)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
oqqora1=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
oqqora2=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
oqqora3=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
oqqora4=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
cv2_imshow(oqqora1)
cv2_imshow(oqqora2)
cv2_imshow(oqqora3)
cv2_imshow(oqqora4)