import cv2

# Load an image
image = cv2.imread(r'C:\Users\mohan\OneDrive\Pictures\mona.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the image
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
