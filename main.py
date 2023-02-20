# IMPORT LIBRARIES
import cv2
import easyocr as eo
from googletrans import Translator

# READ IMAGE
img = cv2.imread('tel.jpg')

# INSTANCE FOR TEXT DETECTOR
reader = eo.Reader(['en'], gpu=False)

# DETECT TEXT IN IMAGE
text = reader.readtext(img)

# TEXT TRANSLATOR
translator = Translator()
for i in text:
    print(translator.detect(i[1]))
    print(translator.translate(i[1]))
    print()

# DRAW BOUNDING BOX
for t in text:
    print(t)
    bbox, text, score = t
    l_bbox = bbox[0][0]
    l_bbox1 = bbox[0][1]
    r_bbox = bbox[2][0]
    r_bbox1 = bbox[2][1]

    cv2.rectangle(img, (int(l_bbox), int(l_bbox1)), (int(r_bbox), int(r_bbox1)), (0, 255, 0),2)
    cv2.putText(img, text, (int(l_bbox), int(l_bbox1)), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0 ,0), 2)

# OUTPUT WINDOW
cv2.imshow("Out", img)
cv2.waitKey(0)