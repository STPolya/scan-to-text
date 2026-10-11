from PIL import Image
import pytesseract
from modules.text_recognition import recognize_text
from modules.saving_result import save_to_txt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_to_read = input('Введите путь до картинки в формате "D:\Документы\\example.png": ')

text_from_image, error_recognize_text = recognize_text(image_to_read)

if error_recognize_text is not None:
    print(error_recognize_text)
else:
    print('Текст с картинки: ', text_from_image)
    while True:
        try:
            user_choice = int(input('Действия:\n1. Скачать результат в txt\n2. Выйти\nВведите действие (1 или 2): '))
        except ValueError:
            print('Выберите действие: 1 или 2')
        else:
            if user_choice == 1:
                user_path_to_save = input('Укажите путь куда сохранить файл в формате "D:\Документы\\example.txt": ')
                print(save_to_txt(text_from_image, user_path_to_save))
            elif user_choice == 2:
                print('Спасибо! До свидания!')
                break
            else:
                print('Выберите действие из списка')

