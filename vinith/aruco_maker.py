import cv2

# Load the image
image = cv2.imread("image.jpg")

# Create a detector object
detector = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Detect the markers in the image
markerCorners, markerIds, _ = cv2.aruco.detectMarkers(image, detector)

# Draw the detected markers on the image
image = cv2.aruco.drawDetectedMarkers(image, markerCorners, markerIds)

# Display the image
cv2.imshow("Aruco markers", image)
cv2.waitKey(0)