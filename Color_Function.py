import cv2
import numpy as np
import matplotlib.pyplot as plt


cap=cv2.VideoCapture(0)   # 0 is default cam , can change value to 1 or 2

while(1):
    ret,frame=cap.read()
    frame=cv2.flip(frame, 1)
    hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height,width,ret=frame.shape
    lower_blue=np.array(["90","1126","97"], np.uint8)  #MAVİ 150,150,0 or 110 50 50 or enson 85,118,114
    upper_blue=np.array(["140","255","255"],np.uint8) #MAVİ 140,255,255    or 130 255 255 or 154,255,255  (These values ​​can be changed according to the camera difference)
    blue_mask=cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue=cv2.bitwise_and(frame,frame,mask=blue_mask)
    
    
    
    kernal=np.ones((5,5),"uint8")
    blue_mask=cv2.dilate(blue_mask, kernal)
    res_blue=cv2.bitwise_and(frame,frame,mask=blue_mask)
    cv2.rectangle(frame, (283,200), (356,280), (100,250,0), 3)  #size for square in the middle of the image (replaceable values to your need)
    contours,hierarchy=cv2.findContours(blue_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):
        area=cv2.contourArea(contour)
#---------------startpoint of private function loop-------------------
    
        if(area>300):   #checks for certain color sizes on the screen and indicates
            x,y,w,h=cv2.boundingRect(contour)
            frame=cv2.rectangle(frame,(x,y), (x+w,y+h), (0,0,255),2)
            text=  cv2.putText(frame, "blue color", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,255))
            
            height,width,ret=frame.shape
            cx=int(width/2)
            cy=int(height/2)            
            cv2.circle(frame, (cx,cy), 5, (255,0,0),3)             


            pixel_center=hsv_frame[cy,cx]
            hue_value=pixel_center[0]
            hue_value1=pixel_center[1]
            hue_value2=pixel_center[2]
#----------------main loop for the function--------------
            if x>283 and y+h<280 and y>200 and x+w<356  : #checks if the area is inside the within the desired value ranges
                                                          #if loop find blue area in the square private function will work 
                print("x değeri:",x," y değeri:",y," x+w degerı:",x+w , " y+h değeri:",y+h)                
                color="undefined"
                if hue_value <9:
                    color="red"
                elif hue_value<85:
                    color="green"
                elif hue_value<120  :
                       color="blue"
                       
                       def func(): #your function 
                           pass  
                print("deger:",pixel_center)
                cv2.putText(frame, color, (10,50), 0, 1, (250,0,0),2)
#---------------endpoint of private function loop-------------------

    cv2.imshow("webcam",frame)
    cv2.imshow("mask", blue)
    
    if  cv2.waitKey(1)& 0xFF==ord("q"):
        print(pixel_center)
        break
cap.release()
cv2.destroyAllWindows()
    
#made by batuhan
#batuddxd@gmail.com