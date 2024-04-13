def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("Первый аргумент должен быть списком или кортежем")
    
    if not isinstance(index, int):
        raise TypeError("Индекс должен быть целым числом")
    
    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    if not isinstance(coll, (list, tuple)):
        raise TypeError("Аргумент 'coll' должен быть списком или кортежем")

    length = len(coll)
    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    elif start < 0:
        normalized_start = max(length + start, 0)
    else:
        normalized_start = min(start, length)

    if end is None:
        normalized_end = length
    elif end < 0:
        normalized_end = max(length + end, 0)
    else:
        normalized_end = min(end, length)

    return coll[normalized_start:normalized_end]
