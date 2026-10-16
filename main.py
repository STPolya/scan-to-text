from modules.console import console_app

import os
import warnings
os.environ['GLOG_minloglevel'] = '1'
warnings.filterwarnings(
    'ignore',
    message=r'No ccache found.*',
    category=UserWarning,
)

console_app()
