from modules.console import get_paths_from_user, main_menu
from modules.recognizing_text import recognize_text_from_image, recognize_text_from_table
from modules.saving_result import show_table_result, show_text_result, save_text_result, save_table_result

#D:\Пет проекты\test_images\2.png
import os
import warnings
os.environ["GLOG_minloglevel"] = "1"
warnings.filterwarnings(
    "ignore",
    message=r"No ccache found.*",
    category=UserWarning,
)

user_paths, counter_all = get_paths_from_user()

for element in recognize_text_from_image(user_paths):
    show_text_result(element)
