def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    count_container = int(input("Количество контейнеров: "))
    all_conteiners = []
    for _ in range(count_container):
        container = int(input("Введи вес контейнера: "))
        if container < 0 or container > 200:
            print("Вес контейнера не соотвествует параметрам 0 < вес < 200 "
                  "\n повторяем процедуру ввода")
            get_input_parameters()
        all_conteiners.append(container)
    weight = int(input("Введи вес нового контейнера: "))
    if weight < 0 or weight > 200:
        print("Вес контейнера не соотвествует параметрам 0 < вес < 200 "
              "\n повторяем процедуру ввода")
        get_input_parameters()

    return(all_conteiners, weight)

    pass


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    print(f"\nНомер куда встанет новый контейнер {serial_number_new_container}")
    pass


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    count = 1
    for container in list_container_weights:
        if new_container_weight > container:
            break
        count += 1
    return (count)
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
