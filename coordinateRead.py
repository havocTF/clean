import numpy as np
import pyautogui
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\\\tesseract.exe'


def read_coords():
    while True:
        global string1
        image = pyautogui.screenshot(region=(45, 150, 350, 20))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
        hsv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
        color_lower = np.array([100, 255, 220])
        color_upper = np.array([200, 255, 230])
        mask = cv2.inRange(hsv_image, color_lower, color_upper)
        result = cv2.bitwise_and(image, image, mask=mask)
        image = cv2.cvtColor(np.array(result), cv2.COLOR_RGB2GRAY)
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        image = cv2.resize(image, None, fx=30, fy=30, interpolation=cv2.INTER_CUBIC)
        text = pytesseract.image_to_string(image, lang='mc')
        textArr = text.split()
        coordsArr = []
        for string in textArr:
            if any(char.isdigit() for char in string):
                if ',' in string:
                    a = string.index(',')
                    string1 = string[:a]
                else:
                    read_coords()
                coordsArr.append(string1)
        if len(coordsArr) > 3:
            coordsArr = coordsArr[:3]
        try:
            coordsArr = [float(x) for x in coordsArr]
            coordsArr = [int(x) for x in coordsArr]
        except TypeError:
            read_coords()
        except ValueError:
            read_coords()
        print(coordsArr)
        return coordsArr
