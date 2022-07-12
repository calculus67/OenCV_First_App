import cv2
import numpy as np

picture=cv2.imread("joker.jpg")

picture[30,50]=[255,255,255]

for i in range(100):
    picture[50,i]=[255,255,255]

cv2.imshow("Joker",picture)
cv2.waitKey(0)
cv2.destroyAllWindows()