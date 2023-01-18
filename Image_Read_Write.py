import cv2 #  openCV use as CV2 in Python 

img1 = cv2.imread('image\image.png',1) # imread function use to read image  1 is minse color image amd 0 is gray scale image
img1 = cv2.resize(img1,(1280,700)) # resize width and height
print(img1)
cv2.imshow('Original', img1) # imshow function use to show image 

# cv2.IMREAD_GRAYSCALE : Loods image in grascale mode
img2 = cv2.imread('image\image.png',0)
img2 = cv2.resize(img2,(1280,700)) # resize width and height
print(img2)
cv2.imshow('Gray Image', img2)

# cv2.IMREAD_UNCHANGED : Loods image as such including alpha 
img3 = cv2.imread('image\image.png',-1)
img3 = cv2.resize(img3,(1280,700)) # resize width and height
print(img3)
cv2.imshow('Unchange', img3)

# Image conversion project colored image into grayscale.
Path = input('Enter the path and name of an image ==')
print('Your Enter this ==', Path)

img4 = cv2.imread(Path,0)
img4 = cv2.resize(img4,(560,700))
img4 = cv2.flip(img4,0) # it accept 3 parameters 0.-1,1 Rotate images

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('image\Output.png')
else:
    cv2.destroyAllWindows()

cv2.waitKey(0) # waitkey visulazation control
cv2.destroyAllWindows() # use memory free all windows