from modules.logging_config import log_error
import pytesseract
from docx import Document

def save_to_txt(text, file_path_to_save):
    try:
        with open(file_path_to_save, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as error:
        log_error('saving_to_txt', file_path_to_save, error)
        return (False, 'Не удалось сохранить файл')

    else:
        return (True, None)

def save_to_pdf(image, file_path_to_save):
    try:
        pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
        with open(file_path_to_save, 'w+b') as f:
            f.write(pdf)

    except Exception as error:
        log_error('saving_to_pdf', file_path_to_save, error)
        return (False, 'Не удалось сохранить файл')

    else:
        return (True, None)

def save_to_docx(text, file_path_to_save):
    try:
        doc = Document()
        doc.add_paragraph(text)
        doc.save(file_path_to_save)

    except Exception as error:
        log_error('saving_to_docs', file_path_to_save, error)
        return (False, 'Не удалось сохранить файл')

    else:
        return (True, None)
