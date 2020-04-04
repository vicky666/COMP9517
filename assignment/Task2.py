import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./dog.jpg',0)
img2 = img.copy()
h = img.shape[0]
w = img.shape[1]
s=15
for i in range(0,h):
    for j in range(0,w):
        if (i-s/2) <0:
            if (j-s/2)<0:
                block = img[0:(i+s//2),0:(j+s//2)]
            else:
                block = img[0:(i+s//2),(j-s//2):(j+s//2)]
        elif (j-s/2)<0:
            block = img[(i-s//2):(i+s//2),0:(j+s//2)]
        elif (i+s/2) >h:
            if (j+s/2)>w:
                block = img[(i-s//2):h,(j-s//2):w]
            else:
                block = img[(i-s//2):h,(j-s//2):(j+s//2)]
        elif (j+s/2)>w:
            block = img[(i-s//2):(i+s//2),(j-s//2):w]
        else:
            block = img[(i-s//2):(i+s//2),(j-s//2):(j+s//2)]
        block_hist = cv2.calcHist([block], [0], None, [256], [0.0,255.0])
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(block_hist)
        img2[i,j] = maxLoc[1]
        j +=1        
    i += 1
        
cv2.imshow("test1 task2_5*5", img2) 
#cv2.imwrite('test1 task2_5*5.jpg',img)
cv2.waitKey (0)  
cv2.destroyAllWindows()

