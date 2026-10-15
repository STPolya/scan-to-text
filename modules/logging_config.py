import logging
import json
from datetime import datetime

logger = logging.getLogger('scan_to_text')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('logs/logs.log', encoding='utf-8',)
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)

def log_error(operation, file_path, error):
    record = {
        'timestamp': datetime.now().astimezone().isoformat(),
        'level': 'ERROR',
        'operation': operation,
        'file_path': str(file_path),
        'error_type': type(error).__name__,
        'message': str(error),
    }
    logger.error(json.dumps(record, ensure_ascii=False))