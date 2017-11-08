import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Writing on CAM
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Ha Tong',(10,300), font, 1, (0,0,255),2, cv2.LINE_AA)
    
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('hsv',hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
