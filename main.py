import requests

def call_director_menu(debug, login, password):
    status, id = requests.director_authentication(login, password)
    # TODO Во всех селектах добавить вывод через функцию вывода таблиц
    if status:
        while True:
            print('#'*30)
            input_ = input('Введите действие:\n1) Посмотреть штрафы сотрудников\n2) Добавить сотрудника\n3) Удалить сотрудника\n4) Вывести пациентов\n5) Вывести все услуги\n6) Выход\n')
            if input_ == '1':
                requests.print_table( requests.select_sotrud_fines(debug),[1,2,3,4,5,6,7] )

            elif input_ == '2':
                requests.add_sotrud(debug),[1,2,3,4,5,6]

            elif input_ == '3':
                requests.delete_sotrud(debug)
            elif input_ == '4':
                requests.print_table( requests.select_patient(debug),[1,2,3,4,5,6] )
            elif input_ == '5':
                requests.print_table( requests.select_services(debug),[1,2,3] )
            elif input_ == '6':
                break
            else:
                print(print('Выбрано несуществующее меню. Попробуйте ещё раз...'))
    else:
        return False

def call_registrate_menu(debug, login, password):
    status, id = requests.registrate_authentication(login, password)
    # TODO Во всех селектах добавить вывод через функцию вывода таблиц
    if status:
        while True:
            print('#' * 30)
            input_ = input('Введите действие:\n1) Посмотреть сотрудников\n2) Посмотреть пациентов\n3) Посмотреть услуги\n4) Редактировать сотрудников\n5) Редактировать услуги\n6) Выход\n')

            if input_ == '1':
                # Вывод таблицы     |     Запрос таблицы           |  Названия столбцов
                requests.print_table( requests.select_sotrud(debug),[1,2,3,4,5,6,7] )

            elif input_ == '2':
                # Вывод таблицы     |     Запрос таблицы           |  Названия столбцов
                requests.print_table( requests.select_patient(debug),[1,2,3,4,5,6] )

            elif input_ == '3':
                requests.select_services(debug)
            elif input_ == '4':
                requests.edit_sotrud(debug)
            elif input_ == '5':
                requests.edit_services(debug)
            elif input_ == '6':
                break
            else:
                print(print('Выбрано несуществующее меню. Попробуйте ещё раз...'))
    else:
        return False

def call_doctor_menu(debug, login, password):
    status, id = requests.doctor_authentication(login, password)
    # TODO Во всех селектах добавить вывод через функцию вывода таблиц
    if status:
        while True:
            print('#' * 30)
            input_ = input('Введите действие:\n1) Посмотреть пациентов\n2) Посмотреть историю пациента\n3) Посмотреть проивопоказания пациента\n4) Изменить противопоказания\n5) Добавить диагноз приёма\n6) Выйти\n')
            if input_ == '1':
                requests.select_patient(debug)
            elif input_ == '2':
                # Функция для примера запроса с условием
                requests.print_table(requests.select_history_patient(debug),[1,2,3,4,5,6])
            elif input_ == '3':
                requests.select_contr_patient(debug)
            elif input_ == '4':
                requests.edit_contr_patient(debug)
            elif input_ == '5':
                requests.edit_diagnoz_patient(debug)
            elif input_ == '6':
                break
            else:
                print(print('Выбрано несуществующее меню. Попробуйте ещё раз...'))
    else:
        return False

def call_patient_menu(debug, login, password):
    status, id = requests.patient_authentication(login, password)
    # TODO Во всех селектах добавить вывод через функцию вывода таблиц
    if status:
        while True:
            print('#' * 30)
            input_ = input('Введите действие:\n1) Посмотреть свои записи\n2) Посмотреть список услуг\n3) Посмотреть свои противопоказания\n4) Добавить запись\n5) Удалить запись\n6) Выход\n')
            if input_ == '1':
                requests.select_my_history(debug)
            elif input_ == '2':
                requests.select_services(debug)
            elif input_ == '3':
                requests.select_my_contrs(debug)
            elif input_ == '4':
                requests.add_history_raw(debug)
            elif input_ == '5':
                requests.delete_history_raw(debug)
            elif input_ == '6':
                break
            else:
                print(print('Выбрано несуществующее меню. Попробуйте ещё раз...'))
    else:
        return False

if __name__ == '__main__':
    debug = False # False - Если нужно проверять запросы
    while True:
        move = input('Выберите роль:\n1) Директор\n2) Регистратура\n3) Доктор\n4) Пациент\n5) Выйти\n')
        if move in ('1','2','3','4'):
            print('\n'+'#'*30+'\n')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            print('\n'+'#'*30+'\n')

        if move == '1':
            if call_director_menu(debug, login, password) == False:
                print('Неудачное подключение')

        elif move == '2':
            if call_registrate_menu(debug, login, password) == False:
                print('Неудачное подключение')

        elif move == '3':
            if call_doctor_menu(debug, login, password) == False:
                print('Неудачное подключение')

        elif move == '4':
            if call_patient_menu(debug, login, password) == False:
                print('Неудачное подключение')
        elif move == '5':
            break
        else:
            print('Выбрано несуществующее меню. Попробуйте ещё раз...')