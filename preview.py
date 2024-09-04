#!/usr/bin/env python3

# preview usb camera video stream with opencv, in full hd resolution
# usage: python3 preview.py

import cv2

# open the video capture device
cap = cv2.VideoCapture(0)

# set the resolution to full hd
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# check if the video capture device was opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture device.")
    exit(1)

# loop to read frames from the video capture device

while True:
    # read a frame from the video capture device
    ret, frame = cap.read()

    # check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # display the frame
    cv2.imshow("Frame", frame)

    # check if the user pressed the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()
