#D:\Пет проекты\test_images\1.jpg, D:\Пет проекты\test_images\diplomas.png, D:\Пет проекты\test_images\other.jpg, D:\Пет проекты\test_images\test.png

import pytesseract
from modules.console import get_language_from_user, main_app, get_paths_from_user

#указываем путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#запрашиваем у юзера пути до картинок
user_images = get_paths_from_user()

#выбор языка для распознавания
language_recognize = get_language_from_user()

#запуск меню
main_app(user_images, language_recognize)



