# IMPORT LIBRARIES
import easyocr as eo
import numpy as np
import matplotlib.pyplot as plt

# READ AND PLOT IMAGE
img = plt.imread('1.png')
plt.imshow(img)

# INSTANCE OCR VARIABLE
reader = eo.Reader(['en'], gpu=False)

# IDENTIFY TEXT IN IMAGE
text = reader.readtext(img)

print(text)