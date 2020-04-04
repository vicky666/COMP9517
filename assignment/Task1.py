import numpy as np 
import cv2
import matplotlib.pyplot as plt

# read an image
img = cv2.imread('./light_rail.jpg',1)
#print(img)
height =img.shape[0]
width =img.shape[1]

#print(img)
for i in range(height):
    for j in range(width):
        gray=0.299*img[i,j][0] + 0.587*img[i,j][1] + 0.114*img[i,j][2] 
        img[i,j] = np.uint8(gray)

cv2.imshow('image',img)
#cv2.imwrite('light_rail task1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
