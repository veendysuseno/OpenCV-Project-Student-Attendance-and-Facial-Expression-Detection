import numpy as np
import cv2
import os

# Create directory if it doesn't exist
if not os.path.exists('dataSet'):
    os.makedirs('dataSet')

# Initialize webcam and face detector
cam = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Input user ID
user_id = input('Enter user ID: ')
sample_num = 0

while True:
    # Capture frame-by-frame
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Loop through detected faces
    for (x, y, w, h) in faces:
        sample_num += 1
        # Save the captured image into the dataset folder
        file_path = f"dataSet/User.{user_id}.{sample_num}.jpg"
        cv2.imwrite(file_path, gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.waitKey(100)

    # Display the result
    cv2.imshow("Face", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Stop capturing after 50 samples
    if sample_num == 50:
        print(f"Captured {sample_num} images.")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
