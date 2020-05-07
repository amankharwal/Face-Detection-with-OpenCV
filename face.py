import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('aman.xml')

# Read the input image
img = cv2.imread('ww.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 4), 10)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()