import sys
from pathlib import Path
from modules.checking import check_save_result
from modules.saving_result import save_to_docx, save_to_pdf, save_to_txt, save_to_xlsx
from modules.text_recognition import recognize_table, recognize_text


SUPPORTED_LANGUAGES = ('rus', 'eng', 'rus+eng')
SAVE_OPTIONS = {
    1: ('txt', save_to_txt),
    2: ('pdf', save_to_pdf),
    3: ('docx', save_to_docx),
}

#Ввод и проверка языка
def get_language_from_user():
    while True:
        language = input('Введите язык (rus, eng или rus+eng): ').strip().lower()
        if language in SUPPORTED_LANGUAGES:
            return language
        print('Введите корректный язык')

#Ввод и проверка пути
def get_paths_from_user():
    print('Введите путь к картинке. Для нескольких картинок разделите пути запятой.')
    print(r'Пример: D:\photo1.png, D:\photo2.jpg')

    while True:
        paths = [
            path.strip().strip('"').strip()
            for path in input('Путь: ').split(',')
        ]
        paths = [path for path in paths if path]

        if not paths:
            print('Введите хотя бы один путь.')
            continue

        invalid_paths = [
            path for path in paths
            if not Path(path).is_file()
        ]

        if invalid_paths:
            print('Введите корректный путь')
            continue

        return paths

#Ввод и проверка пункта меню
def get_item_menu_from_user():
    while True:
        try:
            user_choice = int(input('Действия:\n'
                                '1. Сохранить в TXT\n'
                                '2. Сохранить в PDF\n'
                                '3. Сохранить в DOCX\n'
                                '4. Пропустить изображение\n'
                                '5. Закрыть\n'
                                'Введите действие: ')
            )
        except ValueError:
            print('Выберите действие: 1, 2, 3, 4 или 5.')
            continue

        if user_choice in (1, 2, 3, 4, 5):
            return user_choice
        print('Выберите действие: 1, 2, 3, 4 или 5.')

#Вывод саммари по обработнным файлам
def print_summary(counter_all, counter_success_recognize, counter_saved, counter_error, error_images):
    print(
        f'\nВсего обработано: {counter_all}\n'
        f'Успешно распознано: {counter_success_recognize}\n'
        f'Успешно сохранено: {counter_saved}\n'
        f'Ошибок распознавания: {counter_error}\n'
        f'Необработанные: {', '.join(error_images) if error_images else 'Нет'}'
    )

#Ввод пути для сохранения результата
def menu_item_save(extension, data, counter_saved, save_func):
    user_path = input(rf'Укажите полный путь для сохранения, например D:\Документы\example.{extension}: ').strip()
    result = save_func(data, user_path)
    return check_save_result(result, counter_saved)

#Вывод ошибки
def print_recognition_error(number, image, error):
    print(f'\n{'-' * 70}\nИзображение {number} ({image}) не обработано: {error}\n{'-' * 70}')

#Меню
def save_image_result(image, text, counter_saved):
    user_choice = get_item_menu_from_user()
    if user_choice == 4:
        print('К следующей картинке')
        return counter_saved
    if user_choice == 5:
        print('Спасибо! До свидания!')
        sys.exit()

    extension, save_func = SAVE_OPTIONS[user_choice]

    data = image if extension == 'pdf' else text
    message, counter_saved = menu_item_save(extension, data, counter_saved, save_func)
    print(message)
    return counter_saved

#Распознавание и сохранение картинки
def image_menu(user_images, language_recognize):
    counter_all = 0
    counter_saved = 0
    counter_success_recognize = 0
    error_images = []

    for number, image in enumerate(user_images, start=1):
        image = image.strip()
        counter_all += 1
        text, error = recognize_text(image, language_recognize)

        if error is not None:
            print_recognition_error(number, image, error)
            error_images.append(image)
            continue

        counter_success_recognize += 1
        print(f'\nТекст с картинки {number} ({image}): {text.strip()}\n')
        counter_saved = save_image_result(image, text, counter_saved)

    print_summary(counter_all, counter_success_recognize, counter_saved,
                  len(error_images), error_images)

#Распознавание и сохранение таблицы
def table_menu(user_images, language_recognize):
    counter_all = 0
    counter_saved = 0
    counter_success_recognize = 0
    error_images = []

    for number, image in enumerate(user_images, start=1):
        image = image.strip()
        counter_all += 1
        table, error = recognize_table(image, language_recognize)

        if error is not None:
            print_recognition_error(number, image, error)
            error_images.append(image)
            continue

        counter_success_recognize += 1
        print(f'\nТаблица с картинки {number} ({image}): {table}\n')
        # В показанной версии save_to_xlsx ожидает кортеж и читает table[0].values().
        message, counter_saved = menu_item_save('xlsx', (table, None), counter_saved, save_to_xlsx)
        print(message)

    print_summary(counter_all, counter_success_recognize, counter_saved,
                  len(error_images), error_images)
