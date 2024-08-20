import cv2
import numpy as np
import pyautogui

def locate_image_opencv(template_path, confidence=0.9):
    # Take a screenshot using PyAutoGUI
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)  # Convert the screenshot to a numpy array
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Load the template image
    template = cv2.imread(template_path, 0)  # 0 means load in grayscale
    if template is None:
        print(f"Template image not found at {template_path}")
        return None

    # Optional: Apply Gaussian Blur to the template image
    template = cv2.GaussianBlur(template, (5, 5), 0)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#!!!!!!!!!!!!!!
    # Check if the match is above the confidence threshold
    if max_val >= confidence:
        template_height, template_width = template.shape
        match_location = (max_loc[0] + template_width // 2, max_loc[1] + template_height // 2)

        # Print the accuracy (confidence level)
        print(f"Match found with confidence: {max_val:.2f}")

        # Draw a rectangle around the matched region for visual debugging
        cv2.rectangle(screenshot, max_loc, (max_loc[0] + template_width, max_loc[1] + template_height), (0, 255, 0), 2)
        cv2.imshow("Matched Image", screenshot)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        screen_width, screen_height = pyautogui.size()
        if 0 < match_location[0] < screen_width and 0 < match_location[1] < screen_height:
            return match_location
        else:
            print("Match location is outside the screen bounds; ignoring.")
            return None
    else:
        print(f"Match confidence {max_val:.2f} is lower than threshold {confidence}")
        return None

# Example usage
template_path = "../Don't Touch/send_button_image.jpg"
match_location = locate_image_opencv(template_path, confidence=0.9)

if match_location:
    print(f"Image found at location: {match_location}")
    pyautogui.click(match_location)
else:
    print("Image not found.")
