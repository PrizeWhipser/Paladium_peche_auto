import window_capture
import numpy as np
import cv2
import window_capture

def find_template(template_path, hwnd):
    region = (0, 0, 1920, 1040)
    screenshot = window_capture.capture_window(hwnd,region)
    if screenshot:
        screenshot_np = np.array(screenshot)
        
        template = cv2.imread(template_path)
        result = cv2.matchTemplate(screenshot_np, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        h, w = template.shape[:-1]

        if max_val > 0.22:  # You can adjust this threshold as needed
            # Calculate the position of the match in window coordinates
            match_x = max_loc[0]
            match_y = max_loc[1]
            print("Template found at position (x={}, y={}, w={}, h={}), passing to `search_and_click_color`".format(match_x, match_y, w, h))
            template_region = match_x, match_y, w+match_x, h+match_y-100
            screenshot = window_capture.capture_window(hwnd,template_region)
            screenshot.save("testtemplate.png")
            return template_region, screenshot
        else:
            # print("Template not found in the window.")
            return False