import cv2
import numpy as np
import time
color_orange=["orange","239, 159, 39"]
color_violet=["violet","175, 38, 238"]
color_red=["red","255, 57, 57"]

def search_and_click_color(screenshot, region):
    #Ckeck for color orange
    print ("_of search_dans_click_color_",region)
    result = check_color(region, color_orange, screenshot)
    if result is not False:
        # region = tuple(region)  # Convert back to tuple
        return result, color_orange[0]
    else:
        result = check_color(region, color_violet, screenshot)
        if result is not False:
            # print(region)
            return result, color_violet[0]
        else:
            result = check_color(region, color_red, screenshot)
            if result is not False:
                # print(region)
                return result, color_red[0]
            else:
                print("No color found")
                return False
    
def check_color(region, color, screenshot):
    contour_threshold = 20
    tuplecolor = tuple(map(int, color[1].split(',')))  # Convert string to tuple of integers
    # Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)

    # Define the lower and upper bounds of the color to search for
    lower_bound = np.array(tuplecolor, dtype=np.uint8) - np.array([5, 5, 5])
    upper_bound = np.array(tuplecolor, dtype=np.uint8) + np.array([5, 5, 5])
    # Create a mask for the color within the search area
    mask = cv2.inRange(screenshot_np, lower_bound, upper_bound)
    # Check if the color is found
    if np.any(mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        valid_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > contour_threshold:
                valid_contours.append(cnt)

        if valid_contours:
            # Assuming you're still interested in the largest contour,
            # you can sort the contours by area and take the largest one
            largest_contour = min(valid_contours, key=cv2.contourArea)

            # Get the bounding rectangle of the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)

            pos_x = x + region[0]
            pos_y = y + region[1]
            print("Color", color[0], "found! at:", pos_x, pos_y, w, h, "passing to if_white")
            modified_region = (pos_x, pos_y, w + pos_x, h + pos_y)  # Example region to search within (x, y, width, height)
            modified_region = list(modified_region)
            return modified_region
    else:
        print("Color", color[0], "not found. passing to next color")
        return False
