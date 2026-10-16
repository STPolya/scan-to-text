import logging

def show_info_messages(func):
    def wrapper(paths):
        print('\nПодготавливаем OCR...', flush=True)
        result = func(paths)
        print(f'Распознаем текст...\n')
        return result
    return wrapper

@show_info_messages
def recognize_text_from_image(paths):
    from paddleocr import PaddleOCR
    logging.getLogger('paddlex').setLevel(logging.WARNING)
    image_ocr = PaddleOCR(
        device='cpu',
        enable_mkldnn=True,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        text_detection_model_name='PP-OCRv5_server_det',
        text_recognition_model_name='eslav_PP-OCRv5_mobile_rec'
    )
    return image_ocr.predict_iter(paths)

@show_info_messages
def recognize_text_from_table(paths):
    from paddleocr import TableRecognitionPipelineV2

    logging.getLogger('paddlex').setLevel(logging.WARNING)

    table_ocr = TableRecognitionPipelineV2(
        device="cpu",
        enable_mkldnn=True,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        text_detection_model_name="PP-OCRv5_server_det",
        text_recognition_model_name="eslav_PP-OCRv5_mobile_rec",
        wired_table_structure_recognition_model_name="SLANet_plus",
        wireless_table_structure_recognition_model_name="SLANet_plus"
    )

    return table_ocr.predict_iter(paths)