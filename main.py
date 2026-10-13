import pytesseract
from modules.console import get_language_from_user, image_menu, get_paths_from_user, table_menu

#Путь к исполняемому файлу Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Ввод пути
user_images = get_paths_from_user()

#Ввод языка
language_recognize = get_language_from_user()

#Меню и обработка
while True:
    try:
        choice = int(input('Действия:\n1. Распознать текст\n2. Распознать таблицу\nВведите действие (1 или 2): '))
        if choice > 2:
            print(f'\nВведите корректное действие\n')
    except ValueError:
        print(f'\nВведите корректное действие\n')
        continue

    if choice == 1:
            image_menu(user_images, language_recognize)
            break
    elif choice == 2:
            table_menu(user_images, language_recognize)
            break