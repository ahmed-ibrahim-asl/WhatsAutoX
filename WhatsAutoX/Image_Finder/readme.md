# Image Locator with OpenCV and PyAutoGUI

This project provides a utility to locate a specific image on the screen using OpenCV, and optionally interact with it using PyAutoGUI.

## Overview

The `locate_image_opencv` function takes an image path and attempts to find its location on the screen. If the image is found, the function returns the coordinates of the center of the matched region, along with a confidence score. This can be integrated with automation libraries like PyAutoGUI for further actions, such as clicking on the located image.

## How It Works

### 1. Image Capture and Preprocessing

- **Screenshot**: The screen is captured using PyAutoGUI and converted into a NumPy array because OpenCV processes images as NumPy arrays.
- **Grayscale Conversion**: The screenshot is converted to grayscale. Grayscale images are simpler and faster to process, which is why this step is crucial.
- **Target Image**: The target image (the one you want to locate) is loaded in grayscale and a Gaussian Blur filter is applied to reduce noise and smooth the edges. This helps in focusing on the significant features of the image.

### 2. Template Matching

Template matching is used to locate the target image within the larger screenshot.

- **What is Template Matching?**
  - Template matching is a technique used to find a portion of a target image (template) within another larger image (screenshot). The template is slid over the screenshot, compared at each position, and a result matrix is generated indicating how well the template matches each part of the screenshot.

- **cv2.TM_CCOEFF_NORMED:**
  - This method is used in OpenCV to find where a smaller image appears within a larger image. It’s particularly effective in handling differences in brightness and provides a clear score between `-1`, `0`, and `1` to indicate how well the images match.
  - `1` indicates a perfect match.
  - `0` means no match.
  - `-1` indicates that the template matches but with inverted colors or brightness.

        - Dark areas in the template correspond to light areas in the image.
        - Light areas in the template correspond to dark areas in the image.
    

### 3. Interpreting Results

- **Match Location**: 
  - The best match location is identified using the `cv2.minMaxLoc` function, which returns the coordinates of the top-left corner of the best match.
  - The coordinates of the center of the matched region are then calculated by adding half the width and height of the template to the top-left corner coordinates.
  
- **Screen Bounds Check**:
  - Before returning the match location, the script checks if the calculated center is within the screen's bounds to ensure it's a valid and reliable match.

## Parameters

- **`target_image_path`**: (str) The file path to the target image you want to locate on the screen.
- **`confidence`**: (float, optional) The confidence threshold for accepting a match. The match is considered valid only if the confidence score is greater than or equal to this value. Default is `0.9`.

## Returns

The function returns a list containing:
- **Status**: (bool) `True` if the image is found with sufficient confidence, `False` otherwise.
- **Location**: (tuple) Coordinates `(x, y)` of the center of the matched region, or `None` if the image is not found.
- **Confidence**: (float) The confidence score of the match, or `None` if the image is not found.

## Usage

```python
import pyautogui
from image_locator import locate_image_opencv

target_image_path = "path_to_your_image.jpg"
status, location, confidence = locate_image_opencv(target_image_path)

if status:
    print(f"Image found at location: {location} with confidence: {confidence:.2f}")
    pyautogui.click(location)
else:
    print("Image not found or match was not confident enough.")
