import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\Users\mohan\OneDrive\Desktop\img.png", cv2.IMREAD_COLOR)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close('all')