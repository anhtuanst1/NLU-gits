import cv2
import numpy as np

img = cv2.imread('CD7.jpg')

height = np.size(img, 0)
width = np.size(img, 1)
print("height: ",height,"\n")
print("width: ",width,"\n")

cv2.imshow("img",img)
edges = cv2.Canny(img,100,200)
cv2.imshow("edges",edges)

cv2.imwrite("CD7_1.jpg", edges)
