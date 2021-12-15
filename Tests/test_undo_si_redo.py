from Domain.obiect2 import get_new_object, get_id
from Logic.crud import update
from Logic.undo_si_redo import undo, redo, list_versions


def get_data():
    #returneaza o lista de obiecte
    return [
        get_new_object(1, 'birou', 'maro', 450, 'cluj'),
        get_new_object(2, 'scaun', 'lemn', 100, 'cluj'),
        get_new_object(3, 'masa', 'patrata', 330, 'arad'),
        get_new_object(4, 'frigider', 'alb', 2900, 'iasi'),
        get_new_object(5, 'cafetiera', 'scumpa', 470, 'iasi'),
        get_new_object(6, 'imprimanta', 'canon', 890, 'cluj')
    ]


def test_undo_redo():
    lista = get_data()
    versions_list = [lista]
    current_version = 1

    #modific un obiect din lista

    initial_object = get_new_object(5, 'cafetiera', 'scumpa', 470, 'iasi')
    updated_object = get_new_object(5, 'cafetiera', 'ieftina', 200, 'iasi')

    lista = update(lista, updated_object)

    #lista de versiuni va fi actualizata

    versions_list, current_version = list_versions(versions_list, current_version, lista)

    assert initial_object not in versions_list[current_version - 1]
    assert updated_object in versions_list[current_version - 1]

    #in urma unui undo, obiectul initial se va afla in lista curenta

    current_version = undo(current_version)

    assert initial_object in versions_list[current_version - 1]
    assert updated_object not in versions_list[current_version - 1]

    #in urma unui redo, obiectul modificat se va afla in lista curenta

    current_version = redo(versions_list, current_version)

    assert initial_object not in versions_list[current_version - 1]
    assert updated_object in versions_list[current_version - 1]
