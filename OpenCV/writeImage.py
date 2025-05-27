import cv2
import os
path = r"C:\Users\mohan\OneDrive\Desktop\OpenCV\geeksforgeeks.png"
directory = r"C:\Users\mohan\OneDrive\Desktop\OpenCV"
img = cv2.imread(path)
os.chdir(directory)
print("Before saving iamge:")
print(os.listdir(directory))
filename= "savedimg.jpg"
cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))
print("Successfully saved")
