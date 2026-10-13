from PIL import Image, UnidentifiedImageError
import pytesseract
from modules.logging_config import log_error

def recognize_text(image, language):
    try:
        text_from_image = pytesseract.image_to_string(Image.open(image), lang=language).strip()
        if not text_from_image:
            return (None, 'Не удалось распознать текст на картинке')
        return (text_from_image, None)

    except UnidentifiedImageError as error:
        log_error('recognition', image, error)
        return (None, 'Неподдерживаемый файл')

    except FileNotFoundError as error:
        log_error('recognition', image, error)
        return (None, 'Файл не найден')

    except Exception as error:
        log_error('recognition', image, error)
        return (None, f'Произошла ошибка. Попробуйте позже. {error}')