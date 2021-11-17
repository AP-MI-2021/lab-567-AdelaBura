from Domain.obiect2 import get_new_object
from Logic.mutare_locatie import change_location
from Logic.concatenare import concatenare
from Logic.crud import create, read, update, delete


def handle_add(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        return create(lista, obiect)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_read(lista, lista_date):
    try:
        read_id = int(lista_date[1])
        if read(lista, read_id) is None:
            return 'Id-ul citit nu corespunde vreunui element din lista!'
        else:
            return read(lista, read_id)
    except ValueError as ve:
        print('Eroare: ', ve)
    return []


def handle_update(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        update_obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        update_list = update(lista, update_obiect)
        return update_list
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_delete(lista, lista_date):
    try:
        delete_id = int(lista_date[1])
        new_list = delete(lista, delete_id)
        return new_list
    except ValueError as ve:
        print('Eroare:', ve)
    except TypeError as te:
        print('Eroare:', te)
    return lista


def showmenu():
    print('''
        MENIU
        1.Crud
        2.Mutarea unor obiecte dintr-o locatie in alta.
        3.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
        4.Determinarea celui mai mare pret pentru fiecare locatie.
        5.Ordonarea obiectelor crescător după prețul de achiziție.
        6.Afișarea sumelor prețurilor pentru fiecare locație.
        7.Undo.
        8.Redo.
        9.Afisarea listei.
        x.Iesire
        ''')

def handle_change_location(lista, lista_date):
    try:
        sursa = lista_date[1]
        destinatie = lista_date[2]
        return change_location(lista, sursa, destinatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_concatenare(lista, lista_date):
    try:
        string_citit = lista_date[1]
        pret = int(lista_date[2])
        return concatenare(lista, string_citit, pret)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista



