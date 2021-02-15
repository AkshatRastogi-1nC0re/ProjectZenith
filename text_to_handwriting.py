import pywhatkit
import pyautogui
from PIL import Image
import pytesseract as pyt


def text_to_handwriting(file_name):
    pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    print('[Info]: Starting Text Conversion')
    text = pyt.image_to_string(file_name)
    a = (str(text))
    pywhatkit.text_to_handwriting(a,rgb=[0,0,0])
    print("[Info]: Conversion Complete")
