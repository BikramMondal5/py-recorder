import pyautogui

import numpy as np
import cv2

# Get the screen resolution
screen_size = pyautogui.size()

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, screen_size)

# Start recording
while True:
    # Capture the screen
    img = pyautogui.screenshot()

    # Convert the image to a numpy array
    img = np.array(img)

    # Convert the image color format from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Write the frame to the file
    out.write(img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop recording
out.release()
