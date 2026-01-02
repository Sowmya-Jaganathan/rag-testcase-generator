from PIL import Image
import pytesseract

# Path is CORRECT based on your screenshot
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_image_text(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"OCR failed for {image_path}: {e}")
        return ""
