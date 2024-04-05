# FINAL PROJECT (EDGE DETECTION / COLOR CORRECTION)

This server is built with Flask and uses OpenCV for image processing. It allows users to upload images and apply different edge detection and color correction algorithms.

## Prerequisites

Before running the server, you need to have the following installed:
- Python 3
- Flask
- OpenCV
- NumPy
- Pillow

You can install them using pip: `pip install flask opencv-python numpy pillow`

## Running the Server

To run the server, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the directory where the server code is located.
3. Run the server using the following command: `python app.py`

The server will start, and you can access it by going to `http://127.0.0.1:5000/` in your web browser.

## Using the Server

To use the server:

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Use the form to upload an image.
3. The server will process the image and display the results, including the original image and its processed versions.

## Features

The server applies the following image processing algorithms:

- Roberts Cross Edge Detection
- Sobel Edge Detection
- Prewitt Edge Detection
- Laplacian Edge Detection
- Canny Edge Detection
- Color Correction with CLAHE
- Brightness, Contrast, and Saturation Adjustment

Each processed image will be saved in the `static/uploads` directory with a unique filename indicating the applied algorithm.

## Notes

- Ensure the `static/uploads` directory exists and is writable.

    
