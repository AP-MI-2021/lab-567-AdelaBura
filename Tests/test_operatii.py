from Domain.obiect import creeaza_obiectul, get_locatie
from Logic.operatii import muta_obiect


def get_data():
    return[
    creeaza_obiectul(13, 'a', 'ght', 56.9, 'l1'),
    creeaza_obiectul(83, 'hju', 'ght', 56.9, 'l1'),
    creeaza_obiectul(63, 'dh', 'ght', 56.9, '98v5')
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