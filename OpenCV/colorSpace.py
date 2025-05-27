import cv2
image = cv2.imread('C://Users//mohan//OneDrive//Desktop//OpenCV//RGB.png')
B, G, R = cv2.split(image)
cv2.imshow("Original",image)
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()