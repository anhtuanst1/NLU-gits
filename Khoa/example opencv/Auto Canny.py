import cv2
import numpy as np

sigma = 0

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.createTrackbar('sigma','frame',0,100,nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'frame',0,1,nothing)
    
while(True):
    ret, frame = cap.read()

    v = np.median(frame)
    
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    
    edged = cv2.Canny(frame, lower, upper)

    cv2.imshow('frame',edged)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    sigma = cv2.getTrackbarPos('sigma','frame')
    s = cv2.getTrackbarPos(switch,'frame')

    if s == 0:
        sigma = 0
    else:
        sigma
        print ("lower: ",sigma,"\n")

cv2.destroyAllWindows()
