import cv2
import numpy as np

lower = 0
upper = 0

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.createTrackbar('upper','frame',0,255,nothing)
cv2.createTrackbar('lower','frame',0,255,nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'frame',0,1,nothing)
    
while(True):
    ret, frame = cap.read()

    edged = cv2.Canny(frame, lower, upper)

    cv2.imshow('frame',edged)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    upper = cv2.getTrackbarPos('upper','frame')
    lower = cv2.getTrackbarPos('lower','frame')
    s = cv2.getTrackbarPos(switch,'frame')

    if s == 0:
        lower = upper = 0
    else:
        lower
        upper
        print ("lower: ",lower,"\n")
        print ("upper: ",upper,"\n")

cv2.destroyAllWindows()
