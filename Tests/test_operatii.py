from Domain.obiect import creeaza_obiectul, get_locatie
from Logic.operatii import muta_obiect


def get_data():
    return[
    creeaza_obiectul(11, 'dulap', 'mic', 56.9, 'Arad'),
    creeaza_obiectul(12, 'penar', 'colorat', 13, 'Iasi'),
    creeaza_obiectul(13, 'covor', 'plusat', 103.5, 'Cluj')
    ]

def test_muta_obiect():
    obiecte = get_data()
    l1 = get_locatie(obiecte[0])
    l2 = 'locatie noua'
    obiecte_modificat = muta_obiect(obiecte,l1,l2)
    assert get_locatie(obiecte[0]) != get_locatie(obiecte_modificat[0])
    assert len(obiecte_modificat) == len(obiecte)

def test_operatii():
    test_muta_obiect()