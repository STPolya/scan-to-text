from PIL import Image, UnidentifiedImageError
import pytesseract

def recognize_text(image):
    try:
        return (pytesseract.image_to_string(Image.open(image), lang='rus+eng'), None)
    except UnidentifiedImageError:
        return (None, 'Не поддерживаемый файл')
    except FileNotFoundError:
        return (None, 'Файл не найден')
    except Exception:
        return (None, 'Произошла ошибка. Попробуйте позже')