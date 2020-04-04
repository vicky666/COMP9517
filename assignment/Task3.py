import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./dog.jpg',1)
imgB = img.copy()
img2 = cv2.imread('./dog task2_15*15.jpg',0) 
h = img2.shape[0]
w = img2.shape[1]
s = 15
for i in range(0,h):
    for j in range(0,w):
        l = (i-s/2)
        r = (i+s/2)
        t = (j-s/2)
        b = (j+s/2)
        if (i-s/2) <0:
            l = 0
        if (j-s/2)<0:
            t = 0
        if (i+s/2) >h:
            r = h
        if (j+s/2) >w:
            b = w
        list = [0,0,0]
        n=0
        for x in range(int(l),int(r)):
            for y in range(int(t),int(b)):
                if img2[i,j] == img2[x,y]:
                    n+=1
                    l1=imgB[x,y].tolist()
                    list=[l1[i]+list[i] for i in range(0,3)]
        list[0] = list[0]/n
        list[1] = list[1]/n
        list[2] = list[2]/n
        imgB[i,j] = [list[0],list[1],list[2]]
cv2.imshow("dog task3_15*15", imgB) 
#cv2.imwrite('dog task3_15*15.jpg',imgB)
cv2.waitKey (0)  
cv2.destroyAllWindows()
