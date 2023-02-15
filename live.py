# IMPORT LIBRARIES
import cv2
import numpy as np
import easyocr as eo
from matplotlib import pyplot as plt

# LIVE FEED WEB CAM
path = "http://192.168.0.122:8080/video"
# "0" for WebCam
cap = cv2.VideoCapture(path)
cap.set(3, 500)
cap.set(4, 500)

while True:
    # READ IMAGE
    # img = cv2.imread('mockup-sign.jpg')
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    success, img = cap.read()
    cv2.imshow("Live feed", img)

    # THRESHOLDING IMAGE
    # ret, thresh1 = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Thres", thresh1)

    # INCREASE IMAGE CONTRAST
    alpha = 3 # Contrast control (1.0-3.0)
    beta = 10 # Brightness control (0-100)
    # cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # adjusted = cv2.convertScaleAbs(thresh1, alpha=alpha, beta=beta)

    # WARP PRESPECTIVE
    # width, height = 1800, 800

    # pts1 = np.float32([[308,78], [949,217], [302,239], [971,344]])
    # pts2 = np.float32([[0,0], [width,0],[0,height],[width,height]])

    # matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # imgOut = cv2.warpPerspective(img, matrix, (width,height))
    # cv2.imshow("Out", imgOut)

    # INSTANCE FOR TEXT DETECTOR
    reader = eo.Reader(['en'], gpu=False)

    # DETECT TEXT IN IMAGE
    text = reader.readtext(img)

    # DRAW BOUNDING BOX
    for t in text:
        print(t)
        bbox, text, score = t
        l_bbox = bbox[0][0]
        l_bbox1 = bbox[0][1]
        r_bbox = bbox[2][0]
        r_bbox1 = bbox[2][1]
        # print((bbox[0][0]))
        # print(tuple(bbox[2]))
        # print(l_bbox, l_bbox1)
        # print(r_bbox, r_bbox1)

        cv2.rectangle(img, (int(l_bbox), int(l_bbox1)), (int(r_bbox), int(r_bbox1)), (0, 255, 0),2)

    # cv2.imshow("Out", img)
    # cv2.waitKey(0)

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break