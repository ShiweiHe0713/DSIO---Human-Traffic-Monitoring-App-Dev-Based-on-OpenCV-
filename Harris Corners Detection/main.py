import numpy as np
import cv2

# Load the image
img = cv2.imread('images/chessboard.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set the parameters in Harris Corner Detection
blockSize = 3
# ksize is the sobel kernel size
ksize = 3
k = 0.04

# Apply Harris Corner Detection
harris1 = cv2.cornerHarris(gray, blockSize, ksize, k)

# Dilate the detected corners
harris1 = cv2.dilate(harris1, None)

# Τhreshold for an optimal R Value, it is subjective to change
img[harris1 > 0.01*harris1.max()] = [0,0,255]

# Display the image
cv2.imshow('cornersShow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
