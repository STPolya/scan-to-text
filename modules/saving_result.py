from modules.logging_config import log_error

def save_to_txt(text, file_path_to_save):
    try:
        with open(file_path_to_save, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as error:
        log_error('saving_to_txt', file_path_to_save, error)
        return (False, 'Не удалось сохранить файл')
    else:
        return (True, None)
