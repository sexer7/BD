import psycopg2
from constants import HOST_DB, PORT_DB, PASSWORD_DB, USER_DB, NAME_DB

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
                cursor.execute(
                    ''' select * from sotrud; '''
                )
                response = cursor.fetchall()
        except Exception as _ex:
            print('Error while working with PostgreSQL', _ex)
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
                cursor.execute(
                    ''' select * from patient; '''
                )
                response = cursor.fetchall()
        except Exception as _ex:
            print('Error while working with PostgreSQL', _ex)
        finally:
            if connection:
                connection.close()
                return response
                print('Connection closed')

def select_services(debug):
    if debug:
        print('Услуги выведены')
    # else:

def select_history_patient(debug):
    if debug:
        select_patient(debug)
        print('История пациента выведена')
    # else:

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
def director_authentication(login, password):
    return True, 1
def registrate_authentication(login, password):
    return True, 2
def doctor_authentication(login, password):
    return True, 3
def patient_authentication(login, password):
    return True, 4