import cv2
import numpy as np
img1 = cv2.imread(r'C:\Users\mohan\OneDrive\Desktop\OpenCV\1bit1.png')
img2 = cv2.imread(r'C:\Users\mohan\OneDrive\Desktop\OpenCV\2bit2.png')
dest_and = cv2.bitwise_and(img1, img2, mask = None)
dest_or = cv2.bitwise_or(img1, img2, mask = None)
dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)
cv2.imshow('Bitwise AND', dest_and)
cv2.imshow('Bitwise OR', dest_or)
cv2.imshow('Bitwise XOR', dest_xor)
cv2.imshow('Bitwise NOT 1', dest_not1)
cv2.imshow('Bitwise NOT 2', dest_not2)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()