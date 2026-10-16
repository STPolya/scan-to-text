from pathlib import Path
from modules.logging_config import log_error

def save_any_result(recognized_info, method_name):
    try:
        save_method = getattr(recognized_info, method_name)
        save_method('output')
        print('\nУспешно сохранено в папку output')
    except Exception as error:
        print(f'Произошла ошибка при сохранении. {error}')

def save_to_txt_result(recognized_info):
    path_to_file = Path(f'{recognized_info['input_path']}')

    try:
        with open(f'output/{path_to_file.stem}.txt', 'w', encoding = 'utf-8') as file:
            file.writelines(recognized_info['rec_texts'])
    except Exception as error:
        log_error('save_to_txt_result', f'output/{path_to_file.stem}.txt', error)
        print(f'Произошла ошибка при сохранении. {error}')

    print('\nУспешно сохранено в папку output\n')