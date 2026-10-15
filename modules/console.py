from pathlib import Path

SUPPORTED_FILES = ['.bmp', '.dib', '.jpeg', '.jpg', '.png', '.webp', '.pbm', '.pgm', '.ppm', '.pnm', '.sr', '.ras', '.tiff', '.tif', '.pdf']

def get_paths_from_user():
    print('Введите путь к картинке. Для нескольких картинок разделите пути точкой с запятой.')
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

def main_menu():
    print('1. Распознать текст с картинки\n2. Распознать таблицу\n')

    while True:
        user_menu_choice = input('Введите действие (1 или 2): ').strip()
        try:
            if int(user_menu_choice) > 2:
                print('\n!!! Выберите из доступных действий (1 или 2) !!!\n')
            else:
                break
        except ValueError:
            print('\n!!! Введите число !!!\n')

    return user_menu_choice





