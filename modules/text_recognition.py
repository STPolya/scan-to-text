from PIL import Image, UnidentifiedImageError
import pytesseract
from modules.logging_config import log_error

def recognize_text(image, language):
    try:
        return (pytesseract.image_to_string(Image.open(image), lang=language), None)
    except UnidentifiedImageError as error:
        log_error('recognition', image, error)
        return (None, 'Не поддерживаемый файл')
    except FileNotFoundError as error:
        log_error('recognition', image, error)
        return (None, 'Файл не найден')
    except Exception as error:
        log_error('recognition', image, error)
        return (None, f'Произошла ошибка. Попробуйте позже. {error}')