from PIL import Image
import pytesseract
from modules.text_recognition import recognize_text
from modules.saving_result import save_to_txt
import sys

SUPPORTED_LANGUAGES = ['rus', 'eng', 'rus+eng']
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

user_images = input(r'Введите пути до картинок в формате D:\Документы\example.png через запятую: ').split(',')
language_recognize = input('Введите язык (rus, eng или rus+eng): ').lower().strip()

counter_all = 0
counter_saved = 0
counter_success_recognize = 0
counter_error = 0
error_images = []

while True:
    if language_recognize in SUPPORTED_LANGUAGES:
        break
    else:
        language_recognize = input('Выберите язык из: rus, eng или rus+eng): ').lower().strip()

for image in user_images:
    counter_all += 1

    text_from_image, error_recognize_text = recognize_text(image.strip(), language_recognize)

    if error_recognize_text is not None:
        print(f'\n---------------------------------------------------------------'
              f'\nИзображение {counter_all} не обработано. {error_recognize_text}'
              f'\n---------------------------------------------------------------')
        counter_error += 1
        error_images.append(image)
    else:
        counter_success_recognize += 1

        print(f'\nТекст с картинки {counter_all} ({image}): {text_from_image.strip()}\n')
        while True:
            try:
                user_choice = int(input('Действия:\n1. Скачать результат в txt\n2. Пропустить изображение\n3. Закрыть\nВведите действие (1, 2 или 3): '))
            except ValueError:
                print('Выберите действие: 1, 2 или 3')
            else:
                if user_choice == 1:
                    user_path_to_save = input(r'Укажите путь куда сохранить файл в формате D:\Документы\example.txt: ').strip()
                    save_result = save_to_txt(text_from_image, user_path_to_save)

                    if save_result[0]:
                        print('Успешно сохранено')
                        counter_saved += 1
                        break
                    else:
                        print(save_result[1])
                        break

                elif user_choice == 2:
                    print('К следующей картинке')
                    break
                elif user_choice == 3:
                    print('Спасибо! До свидания!')
                    sys.exit()
                else:
                    print('Выберите действие из списка')


print(f'\nВсего картинок: {counter_all}\n'
        f'Успешно обработано: {counter_success_recognize}\n'
        f'Успешно сохранено: {counter_saved}\n'
        f'Ошибок: {counter_error}\n'
        f'Не обработанные изображения: {", ".join(error_images) if counter_error > 0 else "Нет"}')
