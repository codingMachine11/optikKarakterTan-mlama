from typing import List, Tuple
import pytesseract
from PIL import Image
import numpy as np
import cv2

def read_text(image: Image.Image, lang: str = "eng") -> str:
    """Görüntüden düz metin döndürür."""
    img = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return pytesseract.image_to_string(Image.fromarray(gray), lang=lang)

def read_words_with_boxes(image: Image.Image, lang: str = "eng") -> List[Tuple[str, Tuple[int,int,int,int]]]:
    """(kelime, bbox) listesi döndürür. bbox = (x, y, w, h)"""
    img = np.array(image.convert("RGB"))
    data = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT)
    words = []
    for i in range(len(data["text"])):
        txt = data["text"][i].strip()
        if txt and int(data["conf"][i]) > 0:
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            words.append((txt, (x, y, w, h)))
    return words

def draw_boxes(image: Image.Image, words) -> Image.Image:
    """Kelime kutularını görüntü üzerine çizer."""
    img = np.array(image.convert("RGB")).copy()
    for _, (x, y, w, h) in words:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return Image.fromarray(img)
