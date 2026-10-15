def show_text_result(recognized_info):
    print(f'Текст с картинки ({recognized_info['input_path']}): {' '.join(recognized_info['rec_texts'])}\n')

def save_text_result(recognized_info):
    recognized_info.save_to_img('output')
    recognized_info.save_to_json('output')
    print('Сохранение завершено')

def show_table_result(recognized_info):
    print(f'Текст с картинки ({recognized_info['input_path']}): {' '.join(recognized_info['overall_ocr_res']['rec_texts'])}\n')

def save_table_result(recognized_info):
    recognized_info.save_to_xlsx('output')
    print('Сохранение завершено')

