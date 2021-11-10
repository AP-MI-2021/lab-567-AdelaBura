from Domain.obiect import creeaza_obiectul, get_descriere, get_id, get_locatie, get_nume, get_pret_achizitie, set_locatie

def get_all_locations(obiecte):
    lst = []
    for obiect in obiecte:
        if get_locatie(obiect) not in lst:
            lst.append(get_locatie(obiect))
    return lst

def get_max_price(obiecte, locatie):
    pret_maxim = None
    for obiect in obiecte:
        if get_locatie(obiect) == locatie:
            if pret_maxim is None:
                pret_maxim = get_pret_achizitie(obiect)
            elif get_pret_achizitie(obiect) > pret_maxim:
                pret_maxim = get_pret_achizitie(obiect)
    return pret_maxim

def muta_obiect(obiecte, locatie1, locatie2):
    lst = []
    for obiect in obiecte:
        if get_locatie(obiect) == locatie1:
            lst.append(creeaza_obiectul(get_id(obiect),get_nume(obiect),get_descriere(obiect),get_pret_achizitie(obiect),locatie2))
        else:
            lst.append(obiect)
    return lst