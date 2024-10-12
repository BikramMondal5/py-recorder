# Screen Recorder

This Python script captures and records the screen of your device in real-time, saving the output as a video file in `.avi` format.

## Features

- Records the entire screen in real-time
- Saves the recorded video in `.avi` format with the XVID codec
- Allows the user to stop recording by pressing the 'q' key

## Requirements

To run this script, you need the following libraries installed:

- `pyautogui` (for capturing screenshots)
- `numpy` (for image array manipulation)
- `opencv-python` (for video recording and image processing)

You can install these libraries using `pip`:

```bash
pip install pyautogui numpy opencv-python
```

## How to use 

- Clone the repository to your local machine
  ```bash
  git clone https://github.com/BikramMondal5/py-recorder.git
  ```
- Navigate to the project directory
  ```bash
  cd py-recorder
  ```
- Run the python script
  ```bash
  python main.py
  ```
- Press the 'q' key at any time to stop recording:
  The recorded video will be saved in the current directory as output.avi.
  
## Code Explanation 

- **pyautogui**: Used to take screenshots of the screen in real-time.
  
- **numpy**: Converts the screenshots into arrays that can be processed by OpenCV.

- **opencv (cv2)**: Responsible for saving the screenshots as frames in a video file.

