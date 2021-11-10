from Domain.obiect import creeaza_obiectul, get_id, set_nume, set_descriere, set_pret_achizitie, set_locatie

def add_obiect(obiecte, id_obiect, nume, descriere, pret_achizitie, locatie):
    '''
    Adaugam in memorie, in lista de obiecte un obiect format din: id, nume, descriere, pret si locatie
    :param obiecte: lista de obiecte
    :param id_obiect: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return:
    '''
    obiect = creeaza_obiectul(id_obiect, nume, descriere, pret_achizitie, locatie)
    return obiecte + [obiect]

def edit_obiect(obiecte, obiect_nou):
    '''
    Editarea obiectelor cu idul id si aruncarea unei erori ValueError in cazul in care fieldurile nu sunt corecte
    :param obiecte: 
    :param obiect_nou:
    :return: 
    '''
    lista_noua = []
    for obiect in obiecte:
        if get_id(obiect) == get_id(obiect_nou):
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua

def find_obiect(obiecte, id_obj):
    '''
    Gaseste obiectul in obicte cu id
    :param obiecte:
    :param id:
    :return:
    '''
    for obiect in obiecte:
        if get_id(obiect) == id_obj:
            return obiect
    return None

def delete_obiect(obiecte, id_obj):
    '''
    Sterge obiectul din obiecte cu id
    :param obiecte:
    :param id_obj:
    :return:
    '''
    lista_noua = []
    for obiect in obiecte:
        if get_id(obiect) != id_obj:
            lista_noua.append(obiect)
    return lista_noua


