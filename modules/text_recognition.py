from PIL import Image, UnidentifiedImageError
import pytesseract

def recognize_text(image, language):
    try:
        return (pytesseract.image_to_string(Image.open(image), lang=language), None)
    except UnidentifiedImageError:
        return (None, 'Не поддерживаемый файл')
    except FileNotFoundError:
        return (None, 'Файл не найден')
    except Exception as e:
        return (None, f'Произошла ошибка. Попробуйте позже{e}')