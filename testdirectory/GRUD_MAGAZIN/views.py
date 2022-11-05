import random
import json
from decimal import Decimal

FILE_PATH = '/home/user/Desktop/testdirectory/GRUD_MAGAZIN/baza.json'
ID_FILE_PATH = '/home/user/Desktop/testdirectory/GRUD_MAGAZIN/id.txt'


def get_baza():
    with open(FILE_PATH) as file:
        return json.load(file)


def save_baza(baza):
    with open(FILE_PATH, 'w') as file:
        json.dump(baza, file)


def listing():
    baza = get_baza()
    return f'Список всех товаров: {baza}'


def retrieve():
    baza = get_baza()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], baza))
        return product[0]
    except:
        return 'Неверный id!'


def get_id():
    with open(ID_FILE_PATH, 'r')as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id


def create_():
    baza = get_baza()
    try:
        product = {
            'id': get_id(),
            'marka': input('Введите марку ноутбука: '),
            'model': input('Введите модель ноутбука: '),
            'sena': float(input('Введите цену ноутбука: ')),
            'god_vypuska': int(input('Введите год выпуска ноутбука: ')),
            'opisanie': input('Введите описание: ')

        }
    except:
        return 'Неверные данные!'

    baza.append(product)
    save_baza(baza)
    return 'Создан новый товар!'


def update_():
    baza = get_baza()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, baza))[0]
        print(f'Товар для обновления: {product ["marka"]}')
    except:
        return 'Неверный id!'

    index = baza.index(product)
    choice = input(
        'Что вы хотите изменить?(1-Марка, 2-Модель , 3-Цена, 4-Год выпуска, 5-Описание: ')
    if choice.strip() == '1':
        baza[index]['marka'] = input('Введите марку: ')
    elif choice.strip() == '2':
        baza[index]['model'] = input('Введите модель: ')
    elif choice.strip() == '3':
        try:
            baza[index]['sena'] = float(input('Введите цену: '))
        except:
            return 'Неверное значение для цены!'
    elif choice.strip() == '4':
        baza[index]['god_vypuska'] = int(input('Введите год выпуска: '))
    elif choice.strip() == '5':
        baza[index]['opisanie'] = input('Введите описание: ')
    else:
        return 'Неверные значение для обновления!'
    save_baza(baza)
    return 'Товар обновлен!'


def delete_():
    baza = get_baza()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, baza))[0]
        print(f'Товар для удаления {product["marka"]}')
    except:
        return 'Неверный id!'

    choice = input('Удалить этот товар?(yes/no): ')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    baza.remove(product)
    save_baza(baza)
    return 'Товар удален!'
