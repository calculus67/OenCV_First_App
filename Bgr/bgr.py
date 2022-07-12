import cv2
import numpy as np

picture = cv2.imread("kurt.jpg")
cv2.imshow("Kurt Resmi",picture)
print(picture[(80,80)])
picture[200,250]=[255,0,0]

print("Resmin Boyutu:"+str(picture.size))
print("Resmin Özellikler:"+str(picture.shape))
print("Resmin Özellikler:"+str(picture.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()

