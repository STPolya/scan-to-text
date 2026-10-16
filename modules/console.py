from pathlib import Path
from modules.recognizing_text import recognize_text_from_image, recognize_text_from_table
from modules.displaying import show_result
from modules.saving_result import save_any_result, save_to_txt_result

SUPPORTED_FILES = ['.bmp', '.dib', '.jpeg', '.jpg', '.png', '.webp', '.pbm', '.pgm', '.ppm', '.pnm', '.sr', '.ras', '.tiff', '.tif', '.pdf']

def get_paths_from_user():
    print('\nВведите путь к картинке. Для нескольких картинок разделите пути точкой с запятой.')
    print(r'Пример: D:\photo1.png; D:\photo2.jpg')

    while True:
        user_paths = [path.strip() for path in input('Путь: ').split(';')]
        error_paths = []

        for path in user_paths:
            if Path(path).suffix.lower() not in SUPPORTED_FILES:
                print(f'\n!!! Поддерживаем только картинки форматов: {', '.join(SUPPORTED_FILES)} !!!\n')
                break

            if not Path(path).exists():
                print(f'\n!!! Произошла ошибка. Файл не найден: {'; '.join(error_paths)} !!!\n')
                break

        else:
            return user_paths, len(user_paths)

def get_menu(print_text, input_text, count_menu_items):
    print(print_text)

    while True:
        try:
            user_menu_choice = int(input(input_text).strip())
            if int(user_menu_choice) > count_menu_items:
                print('\n!!! Выберите из доступных действий !!!\n')
            else:
                break
        except ValueError:
            print('\n!!! Введите число !!!\n')

    return user_menu_choice

def console_app():
    main_menu_user_choice = get_menu(print_text = '1. Распознать текст с картинки\n2. Распознать таблицу\n3. Закрыть\n',
             input_text = 'Введите действие (1, 2 или 3): ',
             count_menu_items = 3
             )

    if main_menu_user_choice == 3:
        print('\nДо свидания!\n')
        return

    user_paths, counter_all = get_paths_from_user()
    counter_picture = 0

    if main_menu_user_choice == 1:
        for element in recognize_text_from_image(user_paths):
            counter_picture += 1

            print(f'Картинка {counter_picture} ', end = '')
            show_result(element, ('rec_texts',))

            download_menu_user_choice = get_menu(print_text = '1. Скачать обработанную картинку\n2. Скачать txt\n3. Пропустить картинку\n4. Закрыть',
                 input_text = 'Введите действие (1, 2, 3 или 4): ',
                 count_menu_items = 4)

            if download_menu_user_choice == 1:
                save_any_result(element, 'save_to_img')
            elif download_menu_user_choice == 2:
                save_to_txt_result(element)
            elif download_menu_user_choice == 3:
                print(f'\nПропускаем картинку {counter_picture}\n')
                continue
            elif download_menu_user_choice == 4:
                print('\nДо свидания!\n')
                return

        print(f'Всего картинок обработано: {counter_all}')


    elif main_menu_user_choice == 2:
        for element in recognize_text_from_table(user_paths):
            counter_picture += 1

            print(f'Картинка {counter_picture} ', end='')
            show_result(element, ('overall_ocr_res', 'rec_texts'))

            if not element['table_res_list']:
                print(f'!!! Таблицы на картинке {counter_picture} не найдены. !!!')
                continue

            download_menu_user_choice = get_menu(print_text = '1. Скачать обработанную картинку\n2. Скачать xlsx\n3. Скачать html\n4. Пропустить картинку\n5. Закрыть',
                 input_text = 'Введите действие (1, 2, 3, 4 или 5): ',
                 count_menu_items = 5)

            if download_menu_user_choice == 1:
                save_any_result(element, 'save_to_img')
            elif download_menu_user_choice == 2:
                save_any_result(element, 'save_to_xlsx')
            elif download_menu_user_choice == 3:
                save_any_result(element, 'save_to_html')
            elif download_menu_user_choice == 4:
                print(f'\nПропускаем картинку {counter_picture}!\n')
                continue
            elif download_menu_user_choice == 5:
                print('\nДо свидания!\n')
                return

        print(f'\nВсего картинок обработано: {counter_all}')