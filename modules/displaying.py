def show_result(recognized_info, keys):
    texts = recognized_info

    for key in keys:
        texts = texts[key]

    text = ' '.join(texts)
    print(f'({recognized_info['input_path']})\nТекст с картинки: {text}\n')
