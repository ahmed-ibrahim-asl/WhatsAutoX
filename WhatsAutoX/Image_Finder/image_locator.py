import cv2
import numpy as np
import pyautogui


def locate_image_opencv(target_image_path, confidence=0.9):
    """
    This function uses OpenCV to locate the specified image on the screen and returns its location.
    so it could be integrated with modules like 
    

    Locate an image on screen using OpenCV and return it's position to be integerated with modules
    like pyautogui.

    Parameters:
    -----------
        1. target_image_path: str
            Path to the target image

        2. confidence: float, optional parameter 
            Minimum confidence for a match (default is 0.9)


    Returns:
    --------
        Type: list
        - [bool]: True if found, Flase if not found
        - [tuple]: (x, y) coordinates of the center of the matched region, or None if not found.
        - [float]: confidence score
    """

    # We convert image into NumPy array. because OpenCv processes images as NumPy arrays
    screenshot_of_screen = np.array(pyautogui.screenshot())

    # Convert the screenshot into grayscale to simplifies the image data for easier and faster processing
    screenshot_gray  = cv2.cvtColor(screenshot_of_screen, cv2.COLOR_BGR2GRAY)



    #Load the Image in grayscale
    target_image = cv2.imread(target_image_path, 0)  # 0 means load in grayscale
    
    if target_image is None:
        print(f"Target image is not found at {target_image_path}")
        return [False, None, None]

    # Applying Gaussian Blur Filter
    target_image = cv2.GaussianBlur(target_image, (5, 5), 0)



    #Matching operation
    result = cv2.matchTemplate(screenshot_gray, target_image, cv2.TM_CCOEFF_NORMED)
   
    """
    - 'min_val': Lowest match score in the result matrix.
    - 'max_val': Highest match score in the result matrix.
    - 'min_loc': Coordinates of the worst match in the screenshot.
    - 'max_loc': Coordinates of the best match in the screenshot. 
    """
   
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)





    if max_val >= confidence:
        target_image_height, target_image_width = target_image.shape 

        
        match_location = ( (target_image_width // 2),  (target_image_height // 2) )

        #max_loc[0]: x-coordinate of the top-left
        #max_loc[1]: y-coordinate of the top-left

        # we return the location to center of that image
        match_location = (max_loc[0] + target_image_width // 2, max_loc[1] + target_image_height // 2)



        # Ensures the match location is accurate and reliable before returning the coordinates

        screen_width, screen_height = pyautogui.size()
        if( (0 < match_location[0] < screen_width) and (0 < match_location[1] < screen_height) ):
            return [True, match_location, max_val]
        
        else:
            return [False, None, None]


    else:
        return [False, None, max_val]




if __name__ == "__main__":
    target_image_path = input("Please enter the path to the image you want to locate: ")
    
    status, location, confidence = locate_image_opencv(target_image_path)

    if status:
        print(f"Image found at location: {location} with confidence: {confidence:.2f}")
        pyautogui.click(location)
    else:
        print("Image not found or match was not confident enough.")