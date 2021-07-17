import cv2
import numpy as np

lefttemplate=cv2.imread("./left arrow resize.jpg",0)
lefttemplate=cv2.GaussianBlur(lefttemplate,(13,13),0)
#lefttemplate=cv2.Canny(lefttemplate,100,200)
righttemplate=cv2.imread("./right arrow resize.jpg",0)
righttemplate=cv2.GaussianBlur(righttemplate,(13,13),0)
#rightemplate=cv2.Canny(righttemplate,100,200)
#cv2.imshow("Canny template",template)5.jpg",1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img=cv2.imread("./Dataset/frame131.jpg",1)
    #r l l l r r r l
w, h = righttemplate.shape[::-1] 
foundright = 0
foundleft=0
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
for scale in np.linspace(0.1, 1.0, 100)[::-1]:
    width = int(img.shape[1] * scale) 
    height = int(img.shape[0] * scale) 
    dim = (width, height) 
    resized = cv2.resize(img_gray,dim) 
    r = img_gray.shape[1] / float(resized.shape[1]) 
    resized=cv2.GaussianBlur(resized,(13,13),0)
    
    if resized.shape[0] < h or resized.shape[1] < w: 
            break
   
    edges = resized
    #edges = cv2.Canny(resized, 100, 200) 
    #Applying right template
    result = cv2.matchTemplate(edges, righttemplate, cv2.TM_CCOEFF)
    (_, maxValright, _, maxLocright) = cv2.minMaxLoc(result) 
    # if we have found a new maximum correlation value, then update 
    if  maxValright > foundright: 
            foundright = maxValright
    
     #Applying left template
    result = cv2.matchTemplate(edges, lefttemplate, cv2.TM_CCOEFF)
    (_, maxValleft, _, maxLocleft) = cv2.minMaxLoc(result) 
    # if we have found a new maximum correlation value, then update 
    if  maxValleft > foundleft: 
            foundleft = maxValleft
   
    
if foundright > foundleft:
    print("Right")
else:
    print("Left")