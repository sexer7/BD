import psycopg2
from constants import HOST_DB, PORT_DB, PASSWORD_DB, USER_DB, NAME_DB

# HELPERS
def print_table(table_list,columns_list):
    '''
    :param table_list: - массив с данными таблицы
    :param columns_list:  - массив в котором лежат значения столбцов в нужном порядке
    :return: None
    '''
    # Проверка на соответствие количества столбцов
    assert len(table_list[0]) == len(columns_list)

    # Расчёт длинн столбцов
    len_list = []
    for column in range(len(table_list[0])):
        max = 0
        for raw in range(len(table_list)):
            if len(str(table_list[raw][column])) > max:
                max = len(str(table_list[raw][column]))
        if max < len(str(columns_list[column])):
            max = len(str(columns_list[column]))
        len_list.append(max)

    # Расчёт полной длинный таблицы
    finally_len = 0
    for i in len_list:
        finally_len += i

    # Вывод названий столбцов
    for column in range(len(columns_list)):
        print(str(' {:'+f'^{len_list[column]}'+'} |').format(columns_list[column]),end='')
    print('\n'+'-' * (finally_len+len(columns_list)*3))

    # Вывод данных таблицы
    for raw in range(len(table_list)):
        for column in range(len(table_list[0])):
            print(str(' {:'+f'^{len_list[column]}'+'} |').format(str(table_list[raw][column])),end='')
        print('')
    return None

# SELECTS
def select_sotrud(debug):
    if debug:
        print('Сотрудники выведены')
    else:
        response = []
        try:
            connection = psycopg2.connect(
                host=HOST_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                database=NAME_DB,
                port=PORT_DB
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                # TODO сделать правильный запрос
                cursor.execute(
                    ''' select * from sotrud; ''' # Твой запрос на SQL
                )
                response = cursor.fetchall()
        except Exception as _ex:
            print('Error while working with PostgreSQL\n','-'*50,'\n',_ex,'-'*50)
        finally:
            if connection:
                connection.close()
                return response
                print('Connection closed')

def select_patient(debug):
    if debug:
        print('Пациенты выведены')
    else:
        response = []
        try:
            connection = psycopg2.connect(
                host=HOST_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                database=NAME_DB,
                port=PORT_DB
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                # TODO сделать правильный запрос
                cursor.execute(
                    ''' select * from patient; ''' # Твой запрос на SQL
                )
                response = cursor.fetchall()
        except Exception as _ex:
            print('Error while working with PostgreSQL\n','-'*50,'\n',_ex,'-'*50)
        finally:
            if connection:
                connection.close()
                return response
                print('Connection closed')

def select_services(debug):
    if debug:
        print('Услуги выведены')
    else:
        response = []
        try:
            connection = psycopg2.connect(
                host=HOST_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                database=NAME_DB,
                port=PORT_DB
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                # TODO сделать правильный запрос
                cursor.execute(
                    ''' . . . '''               # Твой запрос на SQL
                )
                response = cursor.fetchall()    # Результат его работы
        except Exception as _ex:
            print('Error while working with PostgreSQL\n','-'*50,'\n',_ex,'-'*50)
        finally:
            if connection:
                connection.close()
                return response
                print('Connection closed')

def select_history_patient(debug):
    if debug:
        print('История пациента выведена')
    else:
        # Пример логики для выбора объекта из другой таблицы
        #             ------------------------------------------------
        patients = select_patient(debug) # Получаем таблицу с пациентами из БД

        patients_names = [i[2] for i in patients] # создаём список с именами пациентов
        patients_ids = [i[0] for i in patients]   # создаём список с id пациентов
        patients_dict = dict(zip(patients_names,patients_ids)) # собираем из имён и id словарь

        print_table(patients,[1,2,3,4,5,6]) # Выводим таблицу для пользователя
        finding_patient = input('Введите имя нужного пациента:')
        patient_id = [i.strip() for i in patients_dict if i.strip() == finding_patient][0] # Получаем id нужного пациента
        #             ------------------------------------------------

        response = []
        try:
            connection = psycopg2.connect(
                host=HOST_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                database=NAME_DB,
                port=PORT_DB
            )
            connection.autocommit = True
            with connection.cursor() as cursor:
                # TODO сделать правильный запрос
                cursor.execute(
                    f''' select * from <table_name> where pat_id = {patient_id} ''' # Твой запрос на SQL
                )
                response = cursor.fetchall()  # Результат его работы
        except Exception as _ex:
            print('Error while working with PostgreSQL\n','-'*50,'\n',_ex,'-'*50)
        finally:
            if connection:
                connection.close()
                return response
                print('Connection closed')

def select_contr_patient(debug):
    if debug:
        print('Противопоказания пациента выведены')
    # else:

def select_my_history(debug):
    if debug:
        print('История посещёний выведена')
    # else:

def select_my_contrs(debug):
    if debug:
        print('Противопоказания выведены')
    # else:

# EDITS (UPDATE/DELETE/INSERT)
def edit_contr_patient(debug):
    if debug:
        print('Противопоказания пациента изменены')
    # else:

def edit_diagnoz_patient(debug):
    if debug:
        print('Диагноз пациента после посещения изменён')
    # else:

def edit_sotrud(debug):
    if debug:
        print('Сотрудники изменены')
    # else:

def edit_services(debug):
    if debug:
        print('Услуги изменены')
    # else:

def add_history_raw(debug):
    if debug:
        print('Запись добавлена')
    # else:

def delete_history_raw(debug):
    if debug:
        print('Запись удалена')
    # else:

# AUTHENTICATION
#TODO Сделать аутентификацию пользователя для всех ролей
def director_authentication(login, password):
    return True, 1


def registrate_authentication(login, password):
    return True, 2

# Пример аутентификации
def doctor_authentication(login, password):
    response = []
    try:
        connection = psycopg2.connect(
            host=HOST_DB,
            user=USER_DB,
            password=PASSWORD_DB,
            database=NAME_DB,
            port=PORT_DB
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            # TODO сделать правильный запрос
            cursor.execute(
                ''' select id, login, password from sotrud where job = 'doctor'; '''  # Твой запрос на SQL
            )
            response = cursor.fetchall()
            #TODO Убрать отладочный вывод таблицы с паролями ----\
            print_table(response,['id','login','password']) #<---/

    except Exception as _ex:
        print('Error while working with PostgreSQL\n', '-' * 50, '\n', _ex, '-' * 50)
    finally:
        if connection:
            connection.close()
            print('Connection closed')
            for raw in response:
                if ((raw[1] == login) and (raw[2] == password)):
                    return True, raw[0]
            return False, 0



def patient_authentication(login, password):
    return True, 4

# Эта часть кода запускается только если напрямую запустить этот py файл|  |  |
# Она не запустится при импорте этого файла как модуля в другой файл    |  |  |
#                                                                       | \_/ |
#                                                                       |  |  |
if __name__ == '__main__':
    print_table(select_patient(False),[1,2,3,4,5,6]) # тестовый запуск вывода запроса в таблице
    print_table(select_sotrud(False), ['id', 'sec_name', 'name', 'something', 'job', 'wtf', 'number']) # тестовый запуск вывода запроса в таблице