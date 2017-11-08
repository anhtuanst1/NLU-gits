import cv2
import numpy as np

drawing = False
ix,iy = -1,-1
font = cv2.FONT_HERSHEY_SIMPLEX

def mousePosition(event,x,y,flags,param):
    global ix,iy,drawing,font

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img,(ix,iy),(x,y),(0,255,0),1)
            ix,iy = x,y
            print('PUSH',ix,iy)
            cv2.rectangle(img,(360,460),(500,490),(0,0,0),-1)
            t1 = cv2.putText(img,"PUSH ["+ str(ix)+","+str(iy)+"]",(360,480), font, 0.5, (0,0,255),1, cv2.LINE_AA)
            #param = (ix,iy)
        else:
            ix,iy = x,y
            print(ix,iy)
            cv2.rectangle(img,(360,460),(500,490),(0,0,0),-1)
            t2 = cv2.putText(img,"["+ str(ix)+","+str(iy)+"]",(360,480), font, 0.5, (0,0,255),1, cv2.LINE_AA)
            #cv2.putText(img,'NO PUSH',(420,480), font, 0.5, (0,0,255),1, cv2.LINE_AA)       #error no exit
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
                
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mousePosition)    #param

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
