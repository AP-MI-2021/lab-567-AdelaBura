from Domain.obiect2 import get_new_object, get_locatie, get_pret_achizitie
from Logic.mutare_locatie import change_location
from Logic.concatenare import concatenare
from Logic.ordonare import ordonare_lista
from Logic.pret_maxim import location_list, pret_maxim_locatie
from Logic.sume_pret import location_list, suma_pret_locatie

def test_change_location():
    obiect1 = get_new_object(1, 'birou', 'alb', 200, 'cluj')
    obiect2 = get_new_object(2, 'masa', 'rotunda', 367, 'cluj')
    obiect3 = get_new_object(3, 'dulap', 'maro', 330, 'iasi')
    lista = [obiect1, obiect2, obiect3]
    new_list = change_location(lista, get_locatie(obiect1), get_locatie(obiect3))
    assert len(lista) == len(new_list)
    assert get_locatie(new_list[0]) == get_locatie(obiect3)
    assert get_locatie(new_list[2]) == get_locatie(obiect3)
    sursa = 'iasi'
    destinatie = ''
    try:
        _ = change_location(lista, sursa, destinatie)
        assert False
    except ValueError:
        assert True

def test_concatenare():
    obiect1 = get_new_object(1, 'birou', 'alb', 200, 'cluj')
    obiect2 = get_new_object(2, 'masa', 'rotunda', 367, 'cluj')
    obiect3 = get_new_object(3, 'dulap', 'maro', 330, 'iasi')
    lista = [obiect1, obiect2, obiect3]
    string_citit = 'REUSIT'
    pret = 150
    new_list = concatenare(lista, string_citit, pret)
    assert len(lista) == len(new_list)
    assert obiect1[2] != new_list[0][2]
    pret2 = 'dj'
    try:
        _ = concatenare(new_list, string_citit, pret2)
        assert False
    except ValueError:
        assert True

def get_data():
    return [
        get_new_object(1, 'birou', 'alb', 200, 'cluj'),
        get_new_object(2, 'masa', 'rotunda', 367, 'cluj'),
        get_new_object(3, 'dulap', 'maro', 330, 'iasi'),
        get_new_object(4, 'canapea', 'living', 2450, 'iasi'),
        get_new_object(5, 'uscator', 'portabil', 78, 'arad'),
        get_new_object(6, 'imprimanta', 'canon', 600, 'cluj')
    ]


def test_ordonare():
    lista = get_data()
    lista_ordonata = ordonare_lista(lista)
    assert lista[4] in lista_ordonata
    assert len(lista) == len(lista_ordonata)


test_ordonare()

def get_data():
    return [
        get_new_object(1, 'birou', 'alb', 200, 'cluj'),
        get_new_object(2, 'masa', 'rotunda', 367, 'cluj'),
        get_new_object(3, 'dulap', 'maro', 330, 'iasi'),
        get_new_object(4, 'canapea', 'living', 2450, 'iasi'),
        get_new_object(5, 'uscator', 'portabil', 78, 'arad'),
        get_new_object(6, 'imprimanta', 'canon', 600, 'cluj')
    ]


def test_pret_max_per_location():
    lista = get_data()
    locationlist = location_list(lista)

    assert get_locatie(lista[0]) in locationlist
    assert get_locatie(lista[2]) in locationlist
    assert get_locatie(lista[4]) in locationlist
    assert len(locationlist) == 3

    lista_preturi = pret_maxim_locatie(lista)

    assert get_pret_achizitie(lista[5]) in lista_preturi
    assert get_pret_achizitie(lista[0]) not in lista_preturi
    assert len(lista_preturi) == len(locationlist)


test_pret_max_per_location()

def get_data():
    return [
        get_new_object(1, 'birou', 'alb', 200, 'cluj'),
        get_new_object(2, 'masa', 'rotunda', 367, 'cluj'),
        get_new_object(3, 'dulap', 'maro', 330, 'iasi'),
        get_new_object(4, 'canapea', 'living', 2450, 'iasi'),
        get_new_object(5, 'uscator', 'portabil', 78, 'arad'),
        get_new_object(6, 'imprimanta', 'canon', 600, 'cluj')
    ]


def test_location_list():
    lista = get_data()
    locationlist = location_list(lista)

    assert get_locatie(lista[0]) in locationlist
    assert get_locatie(lista[2]) in locationlist
    assert get_locatie(lista[4]) in locationlist
    assert len(locationlist) == 3


def test_sume_pret():
    lista = get_data()
    locatie1 = get_locatie(lista[2])
    locatie2= get_locatie(lista[4])
    assert suma_pret_locatie(lista, locatie1) == 2780
    assert suma_pret_locatie(lista, locatie2) == 78
    assert type(suma_pret_locatie(lista, locatie2)) is int


test_sume_pret()
test_location_list()