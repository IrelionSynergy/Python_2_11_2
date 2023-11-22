pets = {
    1:
    {
        'Мухтар': {
            'Вид питомца': 'Собака',
            'Возраст питомца': 9,
            'Имя владельца': 'Павел'
            },
        },
    2:
    {
        'Каа': {
            'Вид питомца': 'желторотый питон',
            'Возраст питомца': 19,
            'Имя владельца': 'Саша'
            },
        },
}


import collections

def get_pet(id):
    if not list(pets.keys()).count(int(id)):
        return False
    else:
        return pets[id]


def get_suffix(age):
    suffix = ''
    endingException = [11, 12, 13, 14]
    endingGod = [1]
    endingLet = [5, 6, 7, 8, 9]
    endingGoda = [2, 3, 4]
    if age >= 10:
        twoNumber = int(str(age)[-2:])
        if twoNumber in endingException: suffix = 'лет'
        elif twoNumber % 10 in endingGod: suffix = 'год'
        elif twoNumber % 10 in endingLet: suffix = 'лет'
        elif twoNumber % 10 in endingGoda: suffix = 'года'
        elif twoNumber % 10 == 0: suffix = 'лет'
    elif age < 10 and age > 0:
        if age in endingException: suffix = 'лет'
        elif age % 10 in endingGod: suffix = 'год'
        elif age % 10 in endingLet: suffix = 'лет'
        elif age % 10 in endingGoda: suffix = 'года'

    return suffix


def pets_list():
    nicknames = set()
    for pet in pets.values():
        nicknames.add(list(pet.keys())[0])
    return nicknames


def create():
    lastIndex =  collections.deque(pets, maxlen=1)[0]
    pet = dict()

    print('Введите животного.')
    nickname = input('Кличка: ')
    typePet = input('Вид питомца: ')
    age = int(input('Возраст: '))
    if age < 0: raise Exception('Неверно указано сколько лет')
    owner = input('Имя хозяина: ')

    petDetails = {
        'Вид питомца': typePet,
        'Возраст питомца' : age,
        'Имя владельца' : owner
        }
    
    pet.update({f'{nickname}': petDetails})
    pets.update({lastIndex + 1 : pet})


def read(nickname):
    for key in pets.keys():
        pet = dict(pets[key])
        for petKey in pet.keys():
            if petKey.lower() == nickname.lower():
                petDetails = pet[petKey]
                nickname = petKey
                typePet = petDetails['Вид питомца']
                age = petDetails['Возраст питомца']
                owner = petDetails['Имя владельца']
                print(f'Это {typePet} по кличке "{nickname}". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}') 


def update(nickname):
    pet = dict()
    id = ''

    for key in pets.keys():
        pet = dict(pets[key])
        for petKey in pet.keys():
            if petKey == nickname:
                id = int(key)
    if id == '': raise Exception('В списке нет такого животного')


    print('Введите животного.')
    nicknameNew = input('Кличка: ')
    typePet = input('Вид питомца: ')
    age = int(input('Возраст: '))
    if age < 0: raise Exception('Неверно указано сколько лет')
    owner = input('Имя хозяина: ')

    petDetails = {
        'Вид питомца': typePet,
        'Возраст питомца' : age,
        'Имя владельца' : owner
        }
    pet.clear()
    pet.update({f'{nicknameNew}': petDetails})
    pets.update({int(id) : pet})


def delete(id):
    id = ''

    for key in pets.keys():
        pet = dict(pets[key])
        for petKey in pet.keys():
            if petKey == nickname:
                id = int(key)

    del pets[int(id)]


command = ''

while command != 'stop':
    print('список команд: create, read, update, delete, stop')
    print('Введите команду:')
    command = input().lower()
    
    if command == 'create':
        create()

    elif command == 'read':
        print(f'Введите животного из списка: {pets_list()}')
        nickname = input()
        if nickname not in pets_list():
            print('Нет такого имени.')
            continue
        else:
            read(nickname)


    elif command == 'update':
        print(f'Введите животного из списка для обновления данных: {pets_list()}')
        nickname = input()
        update(nickname)

    elif command == 'delete':
        print(f'Введите животного для удаления из списка: {pets_list()}')
        nickname = input()
        delete(nickname)

    elif command == 'stop':
        break
    else:
        print('Не верная команда. введите заново')