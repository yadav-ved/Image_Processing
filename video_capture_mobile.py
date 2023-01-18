import cv2
import pafy

# connect your laptop and android device with same netywork either wifi
camera = ''# android camera acsses copy camera addres (http://192.168.0.102:8080/video)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(camera)
print('check == ',cap.isOpened())

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# It cantain 4 parameter, name, codec, fps, resolution
output = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while cap.isOpened():
    ret, frame = cv2.read()
    if ret == True:
        frame = cv2.resize(frame,(600,580))
        cv2.imshow('Colorframe',frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Capture video fram youtube
# install library pafy
url = "https://www.youtube.com/watch?v=pVBmn5uJNKE&list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g"
data = pafy.new(url)
data = data.getbest(preftype = 'mp4')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# It cantain 4 parameter, name, codec, fps, resolution
output = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while cap.isOpened():
    ret, frame = cv2.read()
    if ret == True:
        frame = cv2.resize(frame,(600,580))
        cv2.imshow('Colorframe',frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
output.release()
cv2.destroyAllWindows()
