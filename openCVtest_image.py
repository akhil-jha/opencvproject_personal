import cv2

img = cv2.imread('luke.jpg',0)
imG = cv2.resize(img,(240,360))
cv2.imshow('Luke', imG)

flag=True
while flag:
    k = cv2.waitKey(0) & 0xFF
    if k==32:
        cv2.destroyAllWindows()
        flag=False
    else:
        k = cv2.waitKey(0)