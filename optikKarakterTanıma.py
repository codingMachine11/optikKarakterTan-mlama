from PIL import Image
import pytesseract

# Tesseract'ın yüklü olduğu dizini belirtin
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR işlemi yapılacak görüntünün yolu
image_path = r'C:\Users\zaman\OneDrive\Desktop\ornekMetin.png'

# Görüntüyü açma
img = Image.open(image_path)

# OCR işlemi
metin = pytesseract.image_to_string(img, lang='tur')

# Tanınan metni ekrana yazdırma
print(metin)
