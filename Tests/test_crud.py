from Domain.obiect2 import get_new_object, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        get_new_object(1, 'birou', 'alb', 200, 'cluj'),
        get_new_object(2, 'masa', 'rotunda', 367, 'cluj'),
        get_new_object(3, 'dulap', 'maro', 330, 'iasi'),
        get_new_object(4, 'canapea', 'living', 2450, 'iasi'),
        get_new_object(5, 'uscator', 'portabil', 78, 'arad'),
        get_new_object(6, 'imprimanta', 'canon', 600, 'cluj')
    ]


def test_create():
    lista = get_data()
    new_object = get_new_object(7, 'telefon', 'iphone', 2500, 'cluj')
    new_list = create(lista, new_object)
    assert len(lista) + 1 == len(new_list)
    assert new_object in new_list
    new_object2 = get_new_object(7, 'telefon', 'samsung', 2500, 'cluj')
    try:
        _ = create(new_list, new_object2)
        assert False
    except ValueError:
        assert True
    try:
        new_object3 = get_new_object(7, 'dulap7', 'samsung', 2500, 'clu')
        _ = create(new_list, new_object3)
        assert False
    except ValueError:
        assert True


def test_read():
    lista = get_data()
    random_object = lista[5]
    assert read(lista, get_id(random_object)) == random_object
    assert read(lista) == lista
    try:
        _ = read(lista, 10)
        assert False
    except ValueError:
        assert True


def test_update():
    lista = get_data()
    new_object = get_new_object(3, 'dulap lemn', 'maro', 400, 'arad')
    update_list = update(lista, new_object)
    assert len(lista) == len(update_list)
    assert new_object in update_list
    assert update_list[2] != lista[2]
    new_object2 = get_new_object(12, 'dulap lemn', 'maro', 400, 'arad')
    try:
        _ = update(update_list, new_object2)
        assert False
    except ValueError:
        assert True


def test_delete():
    lista = get_data()
    delete_id = 2
    delete_object = read(lista, delete_id)
    new_list = delete(lista, delete_id)
    assert len(new_list) == len(lista) - 1
    assert delete_object not in new_list
    delete_id3 = 19
    try:
        _ = delete(new_list, delete_id3)
    except ValueError:
        assert True
    delete_id2 = 'iu'
    try:
        _ = delete(new_list, delete_id2)
        assert False
    except TypeError:
        assert True


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


test_crud()

