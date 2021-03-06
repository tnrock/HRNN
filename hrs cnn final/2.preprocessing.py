#import
import sys
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from keras.models import load_model
from keras.models import model_from_json
import tensorflow
#Coding
file="image\pre.jpg"


kernel = np.ones((5,5),np.uint8)
img = cv2.imread(file,0)
ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ims=cv2.resize(thresh_img, (960, 540))
cv2.imshow('Binarization',ims)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
bil=cv2.bilateralFilter(thresh_img,5,500,500)
ret,thrg = cv2.threshold(bil,127,255,cv2.THRESH_BINARY)
bilo=cv2.bilateralFilter(thrg,5,500,500)

ims1=cv2.resize(bilo, (960, 540))

cv2.imshow("Smoothing",ims1)
cv2.waitKey(0)
cv2.destroyAllWindows()



#
kernel = np.ones((5,5), np.uint8)
d = cv2.dilate(bilo, kernel, iterations=1)
ims2=cv2.resize(d, (960, 540))

cv2.imshow("Dilation",ims2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
o = cv2.morphologyEx(d, cv2.MORPH_OPEN, kernel)
ims3=cv2.resize(o, (960, 540))
cv2.imshow("Morphology",ims3)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("image\seg.jpg",o)


#os.system('3.segmentation.py')

