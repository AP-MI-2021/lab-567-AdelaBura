from Domain.obiect import get_id, get_nume, get_locatie, get_descriere, get_pret_achizitie, creeaza_obiectul
from Logic.crud import add_obiect, edit_obiect, find_obiect, delete_obiect

def get_data():
    return[
    creeaza_obiectul(1, 'masina', 'alba', 5690, 'Arad'),
    creeaza_obiectul(2, 'masa', 'maro', 56.9, 'Cluj'),
    creeaza_obiectul(3, 'dulap', 'mare', 300, 'Arad')
    ]

def test_add_obiect():
    obiecte = get_data()
    obiect_nou = creeaza_obiectul(4, 'imprimanta', 'canon', 326, 'Cluj')
    obiecte2 = add_obiect(obiecte, 4, 'imprimanta', 'canon', 326, 'Cluj' )
    assert len(obiecte) == len(obiecte2) - 1
    assert obiect_nou in obiecte2

def test_edit_obiect():
    obiecte = get_data()
    obiect_nou = creeaza_obiectul(2, 'masa patrata', 'maro', 56.9, 'Cluj')
    obiecte2 = edit_obiect(obiecte, obiect_nou)
    assert len(obiecte) == len(obiecte2)
    assert obiect_nou in obiecte2
    assert obiecte2[1] != obiecte[1]

def test_find_obiect():
    obiecte = get_data()
    obiect_oarecare = obiecte[1]
    assert find_obiect(obiecte, get_id(obiect_oarecare)) == obiect_oarecare

def test_delete_obiect():
    obiecte = get_data()
    id_sters = 3
    obiect_sters = find_obiect(obiecte,id_sters)
    obiecte2 = delete_obiect(obiecte, id_sters)
    assert len(obiecte2) == len(obiecte) - 1
    assert obiect_sters not in obiecte2
