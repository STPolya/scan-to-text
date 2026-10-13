def check_save_result(result, counter):
    if result[0]:
        return 'Успешно сохранено', counter + 1
    else:
        return result[1], counter