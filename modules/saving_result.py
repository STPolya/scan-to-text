def save_to_txt(text, file_path_to_save):
    try:
        with open(file_path_to_save, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        return None
    else:
        return 'Успешно записано'
