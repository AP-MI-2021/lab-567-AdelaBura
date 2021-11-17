from Domain.obiect2 import get_new_object, get_id
from Logic.crud import create, delete
from Logic.undo_si_redo import undo, redo, list_versions


def get_data():
    return [
        get_new_object(1, 'birou', 'maro', 450, 'cluj'),
        get_new_object(2, 'scaun', 'lemn', 100, 'cluj'),
        get_new_object(3, 'masa', 'patrata', 330, 'arad'),
        get_new_object(4, 'frigider', 'alb', 2900, 'iasi'),
        get_new_object(5, 'cafetiera', 'scumpa', 470, 'iasi'),
        get_new_object(6, 'imprimanta', 'canon', 890, 'cluj')
    ]


def test_undo_redo():
    lista = []
    versions_list = []
    current_version = 0
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    obiect1 = get_new_object(1, 'birou', 'maro', 450, 'cluj')
    lista = create(lista, obiect1)
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    obiect2 = get_new_object(2, 'scaun', 'lemn', 100, 'cluj')
    lista = create(lista, obiect2)
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    obiect3 = get_new_object(3, 'masa', 'patrata', 330, 'arad')
    lista = create(lista, obiect3)
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    del lista[2]
    current_version = undo(current_version)
    assert versions_list[current_version-1] == lista

    del lista[1]
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    del lista[0]
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista = create(lista, obiect1)
    versions_list, current_version = list_versions(versions_list, current_version, lista)
    lista = create(lista, obiect2)
    versions_list, current_version = list_versions(versions_list, current_version, lista)
    lista = create(lista, obiect3)
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    current_version = redo(versions_list, current_version)
    assert versions_list[current_version - 1] == lista

    lista = delete(lista, get_id(obiect3))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista = delete(lista, get_id(obiect2))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista_verificare = lista + [obiect2]
    current_version = redo(versions_list, current_version)
    lista = versions_list[current_version - 1]
    assert lista == lista_verificare

    lista_verificare2 = lista_verificare + [obiect3]
    current_version = redo(versions_list, current_version)
    lista = versions_list[current_version - 1]
    assert len(lista) == len(lista_verificare2)
    assert obiect3 in lista

    lista = delete(lista, get_id(obiect3))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista = delete(lista, get_id(obiect2))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    obiect4 = get_new_object(4, 'frigider', 'desc 4', 2900, 'l112')
    lista = create(lista, obiect4)
    versions_list, current_version = list_versions(versions_list, current_version, lista)

    current_version = redo(versions_list, current_version)
    assert versions_list[current_version - 1] == lista

    lista = delete(lista, get_id(obiect4))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista = delete(lista, get_id(obiect1))
    current_version = undo(current_version)
    assert versions_list[current_version - 1] == lista

    lista_verificare = lista + [obiect1]
    current_version = redo(versions_list, current_version)
    lista = versions_list[current_version - 1]
    assert lista == lista_verificare

    lista_verificare = lista + [obiect4]
    current_version = redo(versions_list, current_version)
    lista = versions_list[current_version - 1]
    assert lista == lista_verificare

    current_version = redo(versions_list, current_version)
    assert versions_list[current_version - 1] == lista


test_undo_redo()