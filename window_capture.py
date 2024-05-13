import win32gui
import win32ui
import win32con
from ctypes import windll
from PIL import Image
screen_region = (0, 0, 1920, 1080)  # Example region to capture.

def capture_window(hwnd, region):
    
    left, top, width, height = region
    # print(region)

    # Get the device context of the window
    hwndDC = win32gui.GetWindowDC(hwnd)

    # Create a memory device context compatible with the window device context
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # Create a compatible bitmap
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)

    # Create a memory device context that is compatible with the window device context
    saveDC = mfcDC.CreateCompatibleDC()

    # Select the compatible bitmap into the compatible memory device context
    saveDC.SelectObject(saveBitMap)

    # Capture the specified region of the window
    result =windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
    # Convert the bitmap to PIL image
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    im = im.crop((region))
    # Clean up
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    # Save the image if capture successful
    if result == 1:
        #im.save(test.png)
        return im
    else:
        return False
    
if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, 'Paladium - juju2428282')
    screen=capture_window(hwnd, (874, 542, 894, 592))
    screen.show()