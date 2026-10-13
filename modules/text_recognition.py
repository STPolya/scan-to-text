from PIL import Image, UnidentifiedImageError
import pytesseract
from modules.logging_config import log_error


def extract_text(image, language, config=""):
    #Распознает текст с картинки и обрабатывает ошибки
    try:
        with Image.open(image) as opened_image:
            text = pytesseract.image_to_string(
                opened_image,
                lang=language,
                config=config,
            ).strip()

        if not text:
            return None, 'Не удалось распознать текст на картинке'

        return text, None

    except UnidentifiedImageError as error:
        log_error('recognition', image, error)
        return None, 'Неподдерживаемый файл'

    except FileNotFoundError as error:
        log_error('recognition', image, error)
        return None, 'Файл не найден'

    except Exception as error:
        log_error('recognition', image, error)
        return None, 'Не удалось выполнить распознавание'


def recognize_text(image, language):
    #Распознаёт обычный текст
    return extract_text(image, language)


def recognize_table(image, language):
    #Распознаёт текст и разбивает строки по пробельным символам
    text, error = extract_text(image, language, config="--psm 6")

    if error is not None:
        return None, error

    table_rows = {}
    row_number = 1

    for line in text.splitlines():
        if line.strip():
            table_rows[row_number] = line.split()
            row_number += 1

    return table_rows, None