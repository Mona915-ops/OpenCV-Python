import cv2
import numpy as np
image1 = cv2.imread(r"C:\Users\mohan\OneDrive\Desktop\OpenCV\star-1.jpg")
image2 = cv2.imread(r"C:\Users\mohan\OneDrive\Desktop\OpenCV\dot.jpg")
sub = cv2.subtract(image1, image2)
cv2.imshow("Subtracted Image", sub)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()