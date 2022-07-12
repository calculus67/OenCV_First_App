import cv2
import numpy as np

picture = cv2.imread("logo.png") 
cv2.imwrite("grayLogo.png",picture)
cv2.imshow("Logo",picture) 
print(picture.dtype)
print(picture.size)
print(picture.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

