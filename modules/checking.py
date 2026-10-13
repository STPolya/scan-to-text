def check_save_result(result, counter):
    if result is True:
        return 'Успешно сохранено', counter + 1
    else:
        return result, counter