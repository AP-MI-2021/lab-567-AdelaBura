from Domain.obiect import get_id, get_nume, get_locatie, get_descriere, get_pret_achizitie, creeaza_obiectul
from Logic.crud import add_obiect, edit_obiect, find_obiect


def test_add_obiect():
    obiecte = []
    obiect_adaugat = creeaza_obiectul('1a', 'Scaun', 'maro', 120.5, 's250')
    add_obiect(obiecte, '1a', 'Scaun', 'maro', 120.5, 's250')
    assert len(obiecte) == 1
    assert obiecte[0] == obiect_adaugat
    assert get_id(obiecte[0]) == '1a'
    assert get_nume(obiecte[0]) == 'Scaun'
    assert get_descriere(obiecte[0]) == 'maro'
    assert get_pret_achizitie(obiecte[0]) == 120.5
    assert get_locatie(obiecte[0]) == 's250'

    add_obiect(obiecte, '1b', 'Canapea', 'de piele', 310, 's200')
    obiect_adaugat_2 = creeaza_obiectul('1b', 'Canapea', 'de piele', 310, 's200')
    assert len(obiecte) == 2
    assert obiecte[0] == obiect_adaugat
    assert obiecte[1] == obiect_adaugat_2

def test_edit_obiect():
    o1 = creeaza_obiectul('1a', 'Scaun', 'maro', 120.5, 's250')
    o2 = creeaza_obiectul('1ab', 'Scaun mobil', 'maro-alb', 120.5, 's250')
    obiecte = [o1, o2]
    assert len(obiecte) == 2
    obiecte = edit_obiect(obiecte, '1a', 'Scaun la reducere', 'maro-alb', 120, 's259')
    assert len(obiecte) == 2
    o1_nou = find_obiect(obiecte, '1a')
    assert get_id(o1_nou) == '1a'
    assert get_nume(o1_nou) == 'Scaun la reducere'
    assert get_descriere(o1_nou) == 'maro-alb'
    assert get_pret_achizitie(o1_nou) == 120
    assert get_locatie(o1_nou) == 's259'