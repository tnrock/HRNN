from keras.models import load_model
from keras.models import model_from_json
import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv



#enter input image here
image = cv2.imread('image/seg.jpg')
height, width, depth = image.shape

#resizing the image to find spaces better
image = cv2.resize(image, dsize=(width*3,height*2), interpolation=cv2.INTER_CUBIC)
#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
 

#dilation
kernel = np.ones((5,5), np.uint8)
d = cv2.dilate(thresh, kernel, iterations=1)

#adding GaussianBlur
gsblur=cv2.GaussianBlur(d,(5,5),0)#img_dilation,(5,5),0)


#find contours
ctrs, hier = cv2.findContours(gsblur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

m = list()
#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
pchl = list()
dp = image.copy()
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    cv2.rectangle(dp,(x-10,y-10),( x + w + 1, y + h + 1 ),(90,0,255),9)
    ims=cv2.resize(dp, (960, 540))
    cv2.imshow("Segmentation",ims)
    
cv2.imwrite("image\seg1.jpg",dp)
    

#os.system('5.prediction.py')
