import logging

def recognize_text_from_image(paths):
    print('\nПодготавливаем OCR...', flush=True)

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

    print(f'Модели готовы. Распознаем текст...\n')

    return image_ocr.predict_iter(paths)


def recognize_text_from_table(paths):
    print('\nПодготавливаем OCR...', flush=True)

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

    print(f'Модели готовы. Распознаем текст...\n')

    return table_ocr.predict_iter(paths)