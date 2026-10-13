from modules.text_recognition import recognize_text
from modules.saving_result import save_to_pdf, save_to_txt, save_to_docx
from modules.checking import check_save_result
import sys

SUPPORTED_LANGUAGES = ['rus', 'eng', 'rus+eng']

def get_language_from_user():
    user_language = input('Введите язык (rus, eng или rus+eng): ').lower().strip()

    while True:
        if user_language in SUPPORTED_LANGUAGES:
            return user_language
        else:
            user_language = input('Выберите язык из: rus, eng или rus+eng): ').lower().strip()


def get_paths_from_user():
    user_input = input(
        'Введите путь к картинке.'
        f'\nДля нескольких картинок разделите пути запятой.\n'
        rf'Пример: D:\photo1.png, D:\photo2.jpg'
        f'\nПути: '
    )

    while True:
        if not user_input:
            user_input = input(r'Введите пути к картинкам: ')
        else:
            return [
                path.strip()
                for path in user_input.split(',')
                if path.strip()
            ]


def get_item_menu_from_user():
    try:
        user_choice = int(input('Действия:\n1. Сохранить в txt\n2. Сохранить в pdf\n3. Сохранить в docx\n4. Пропустить изображение\n5. Закрыть\nВведите действие (1, 2, 3, 4 или 5): '))
        if user_choice > 5:
            print(f'\nВыберите действие из списка: 1, 2, 3, 4 или 5\n')
        return user_choice
    except ValueError:
        print(f'\nВыберите действие из списка: 1, 2, 3, 4 или 5\n')


def print_summary(counter_all, counter_success_recognize, counter_saved, counter_error, error_images):
    print(f'\nВсего картинок: {counter_all}\n'
          f'Успешно обработано: {counter_success_recognize}\n'
          f'Успешно сохранено: {counter_saved}\n'
          f'Ошибок: {counter_error}\n'
          f'Не обработанные изображения: {", ".join(error_images) if counter_error > 0 else "Нет"}')


def menu_item_save(extension, text_from_image, counter_saved, save_func):
    user_path_to_save = input(rf'Укажите путь куда сохранить файл в формате D:\Документы\example.{extension}: ').strip()
    save_result = save_func(text_from_image, user_path_to_save)
    message, counter_saved = check_save_result(save_result, counter_saved)
    return message, counter_saved


def main_app(user_images, language_recognize):
    counter_all = 0
    counter_saved = 0
    counter_success_recognize = 0
    counter_error = 0
    error_images = []

    for image in user_images:
        counter_all += 1
        text_from_image, error_recognize_text = recognize_text(image.strip(), language_recognize)

        if error_recognize_text is not None:
            print(f'\n-----------------------------------------------------------------------------------'
                  f'\nИзображение {counter_all} не обработано. {error_recognize_text}'
                  f'\n-----------------------------------------------------------------------------------')
            counter_error += 1
            error_images.append(image)
        else:
            counter_success_recognize += 1
            print(f'\nТекст с картинки {counter_all} ({image}): {text_from_image.strip()}\n')

            while True:
                user_choice = get_item_menu_from_user()

                if user_choice == 1:
                    message, counter_saved = menu_item_save('txt', text_from_image, counter_saved, save_to_txt)
                    print(message)
                    break
                elif user_choice == 2:
                    user_path_to_save = input(rf'Укажите путь куда сохранить файл в формате D:\Документы\example.pdf: ').strip()
                    save_result = save_to_pdf(image, user_path_to_save)
                    message, counter_saved = check_save_result(save_result, counter_saved)
                    print(message)
                    break
                elif user_choice == 3:
                    message, counter_saved = menu_item_save('docx', text_from_image, counter_saved, save_to_docx)
                    print(message)
                    break
                elif user_choice == 4:
                    print('К следующей картинке')
                    break
                elif user_choice == 5:
                    print('Спасибо! До свидания!')
                    sys.exit()

    print_summary(counter_all, counter_success_recognize, counter_saved, counter_error, error_images)


