import cv2
img = cv2.imread('3a.jpg')
h,w = img.shape[:2]

new_h , new_w = int(h/2),int (w/2)
resizeimg = cv2.resize(img,(new_w,new_h))

cv2.imshow('original',img)
cv2.imshow('resizing',resizeimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
