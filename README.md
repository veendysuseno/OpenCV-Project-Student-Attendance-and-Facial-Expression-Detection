# OpenCV Project: Student Attendance and Facial Expression Detection - My Project LKTIM 2020

## Overview

- This project combines computer vision and deep learning techniques to facilitate student attendance and facial expression detection. Using OpenCV for real-time face detection and TensorFlow/Keras for emotion recognition, the system provides two main functionalities: training a model for facial expression recognition and performing real-time emotion detection via a webcam feed. It is specifically designed to track student attendance based on facial expressions and can operate either by training a recognition model or by displaying live emotion detection results.

- This is my project (LKTIM 2020 --> Lomba Karya Tulis Ilmiah Mahasiswa 2020).
- National Student Scientific Writing Competition.

## Summary:

- This project is designed for student attendance and facial expression detection using OpenCV and TensorFlow. The system can either train a facial expression recognition model or display real-time emotion detection using a webcam feed.

## Directory Structure / Explanation :

Student_Attendance_and_Facial_Expression_Detection_Project/
├── data/ # Directory for training and testing data
│ ├── test/ # Testing data
│ └── train/ # Training data
├── dataSet/ # Directory for dataset files
├── recognizer/ # Directory for face recognition training_data.yml
├── trainer/ # Directory for face recognition training_data.yml
├── dataset.py # Script for managing datasets
├── datatrainner.py # Script for training the model
├── emotions.py # Script for real-time emotion detection and attendance
├── face.csv # CSV file, tracks student attendance with facial recognition data and codes from a numbered dataset.
├── haarcascade_frontalface_default.xml # Haar Cascade XML file for face detection
├── How-to-Run.txt # provides instructions to run the model for real-time emotion detection or training with the respective commands.
├── model.h5 # file contains the saved weights of the trained facial expression recognition model.
├── output[i].avi # file contains a video of the live webcam feed with annotations for detected faces and recognized emotions.
├── README.md # file contains information about the purpose of the code and instructions on how to use it, as well as how to create it.
├── requirements.txt # List of required Python packages
└── time.py # Script for time-related functionalities

## Dependencies

The project requires the following Python packages. You can install them using `pip`:

## Features

- **Facial Expression Detection**: Uses a convolutional neural network (CNN) to detect and classify facial expressions into seven categories.
- **Student Attendance**: Captures and records student attendance based on facial recognition.
- **Real-time Processing**: Displays live video feed with detected emotions and student names.

<hr/>

## Requirements

- Python 3.x
- Libraries listed in requirements.txt =
  - numpy
  - argparse
  - opencv-python
  - Pillow
  - tensorflow
  - matplotlib
  - imutils

<hr/>

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**

   Create a `requirements.txt` file with the following content:

   ```
   numpy
   argparse
   opencv-python
   Pillow
   tensorflow
   matplotlib
   imutils
   ```

   Then, install the packages using:

   ```bash
   pip install -r requirements.txt
   ```

<hr/>

## Usage

### Training the Model

To train the facial expression recognition model, use the following command:

```bash
python emotions.py --mode train
```

This will:

- Train the model using images from the data/train and data/test directories.
- Save the trained model weights to model.h5.
- Plot and save the training history as plot.png.

### Display Mode

To start the real-time emotion detection and student attendance system, use:

```bash
python emotions.py --mode display

```

This will:

- Open the webcam and display the live video feed.
- Detect faces and predict emotions from the webcam feed.
- Record attendance in face.csv if the user inputs the correct class when prompted.

<hr/>

## Files

- emotions.py: Main script for training and displaying.
- haarcascade_frontalface_default.xml: Haar cascade for face detection.
- recognizer/training_data.yml: Pre-trained data for face recognition (required for display mode).
- data/train and data/test: Directories containing training and validation images.

<hr/>

## Interfaces:

- Detect expressions of students whose data has been registered: <br/>
  ![Implementation-1](img/2.png)<br/>

- Detect expressions of students whose data has not been registered: <br/>
  ![Implementation-2](img/4.png)<br/>

<hr/>

## Accuracy Testing

- ![Accuracy-Testing](img/accuracy.png)<br/>

## Notes

- Ensure that the haarcascade_frontalface_default.xml file is in the same directory as emotions.py.
- Modify the script emotions.py to match your specific face recognizer setup and class IDs.
- The dataset.py and datatrainner.py scripts should be used as required for dataset preparation and model training, respectively.

<hr/>

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```css

Feel free to adjust any details according to your project's specifics or preferences.

```

<br/>

# Student-Attendance-and-Facial-Expression-Detection"

<br/>

#### @Copyright 2020 | Team-LKTI-PSMURO-GUNDAR
