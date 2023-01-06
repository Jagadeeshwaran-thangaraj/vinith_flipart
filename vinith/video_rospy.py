
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

detector = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

# Instantiate CvBridge
bridge = CvBridge()

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(1)

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

        # Detect the markers in the image
        markerCorners, markerIds, _ = cv2.aruco.detectMarkers(cv2_img, detector)
        cv2_img = cv2.aruco.drawDetectedMarkers(cv2_img, markerCorners, markerIds)

        cv2.imshow('image', cv2_img)
        cv2.waitKey(1)
    except CvBridgeError as e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/rrbot/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()