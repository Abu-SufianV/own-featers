import os


def directory_generator(path: str, amount: int, suffix='', prefix=''):
    """
    Данная функция генерирует заданное кол-во директорий с учётом суффикса и префикса

    Например: directory_generator('C:/Users/name/Dir', 3, 'new', '_')

    Результат: newDir_1, newDir_2, newDir_3

    :param path: Полный путь до директории (вкл. само название директории)
    :param amount: Количество генерируемых директорий
    :param suffix: Суффикс добавляемый кназванию папки
    :param prefix: Префик добавляемый кназванию папки

    :return: None
    """

    if '\\' in path:  # Проверяем путь при введении через '\'
        path = path.split('\\')
        path = list(filter(None, path))
    elif '/' in path:  # Проверяем путь при введении через '/'
        path = path.split('/')
        path = list(filter(None, path))

    path[-1] = suffix + path[-1] + prefix  # Добавляем суффикс и префикс
    path = '/'.join(path)  # "Собираем" путь с новымм суффиксом и префиксом
    for i in range(1, amount + 1):  # Создаём директории "count" раз
        os.mkdir(path + f"{i}")

    print('\nВсе директории созданы успешно!\n')


directory_generator(input('Path: '), int(input('Amount: ')), input('Suffix: '), input('Prefix: '))
