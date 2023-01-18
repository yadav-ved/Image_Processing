import cv2

cap = cv2.VideoCapture('image\Demo.mp4')
print('acp',cap)

while True:
    ret,frame  = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR) # change color
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    k=cv2.waitKey(25) # 0 mins Statics and 25(milisecond) video play back sheed control. 
    if k == ord('q') & 0xFF:
        break

# Now Copture video from webcam and save in memory
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 0 Laptop and 1 WEB camera

# DIVX, XVID, MJPGF, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# It contain 4 Parameters , name , codec, fps, resolution
output = cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480),0)  # 0 Gray Scale frame save 
print(cap)
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow(frame)
        output.write(frame)
        if cv2.waitKey(1)& 0xFF == ord('q'):
            break
cap.relase()
output.relase()
cv2.destroyAllWindows()