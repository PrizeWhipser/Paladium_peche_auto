import numpy as np
import random
import time
import findandclick_better_test as facbt
import window_capture
import win32gui
from pywinauto.application import Application
VK_SPACE = 0x20
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205
VK_ALT = 0x12
args = {
    "windowtitle": "Paladium - juju2428282"
}
hwnd = win32gui.FindWindow(None, 'Paladium - juju2428282')
random_list= [0.75,1,0.75,2,2.757546,2,2.984,2.1541,2.5,3.541,10]
list_wait_fish=[0.2,0.5,1.2,1.3,1.51,1,1,1,0.75,2,2.757546,2,2.1541,2.5,2]
list_red_found=[0,0,0,0,0,0,0,0.1]
random_list_click_space=np.linspace(0, 0.1, 50)
random_list_click=np.linspace(0, 0.7, 50)

def if_white(region, color_found):
    # print("région")
    # print(region)
    region = region[0], region[1], region[2], region[3]-49
    if color_found == "violet":
        region=(region[0]-10,region[1],region[2]+10,region[3])
    elif color_found == "orange":
        region=(region[0]-22,region[1],region[2]+22,region[3])
    hwnd = win32gui.FindWindow(None, (args["windowtitle"]))
    app = Application()
    app.connect (handle=hwnd)
    time.sleep(random.choice(list_wait_fish))
    temps = time.time()
    screenshot = window_capture.capture_window(hwnd,region)
    screenshot_np = np.array(screenshot)
    while True:
        
        # gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
        # Convert the region to grayscale
        if (np.any(np.all(screenshot_np == [255, 255, 255], axis=2))):
            print("White pixel found.")
            # press_key()
            app.window(title=args["windowtitle"]).send_keystrokes("{VK_SPACE}")
            time.sleep(0.5)
            screenshot.save("test.png")
            time.sleep(random.choice(random_list))
            app.window(title=args["windowtitle"]).right_click()
            break
        else:
            screenshot = window_capture.capture_window(hwnd,region)
            screenshot_np = np.array(screenshot)
            if time.time()-temps>10:
                print("time out")
                app.window(title=args["windowtitle"]).right_click()
                break
    
