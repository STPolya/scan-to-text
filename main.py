from modules.console import console_app


# D:\Пет проекты\test_images\2.png; D:\Пет проекты\test_images\ruk3.jpg; D:\Пет проекты\test_images\3.jpg;
# D:\Пет проекты\test_images\4.jpg; D:\Пет проекты\test_images\1.png

#D:\Пет проекты\test_images\tabbig.png; D:\Пет проекты\test_images\test.jpg; D:\Пет проекты\test_images\tabbig.png

#D:\Пет проекты\test_images\tabl.png


import os
import warnings
os.environ['GLOG_minloglevel'] = '1'
warnings.filterwarnings(
    'ignore',
    message=r'No ccache found.*',
    category=UserWarning,
)

console_app()
