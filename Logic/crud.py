from copy import deepcopy

from Domain.obiect import creeaza_obiectul, get_id, set_nume, set_descriere, set_pret_achizitie, set_locatie


def edit_obiect(obiecte, id, nume_nou, descriere_noua, pret_achizitie_nou, locatie_noua):
    '''
    Editarea obiectelor cu idul id si aruncarea unei erori ValueError in cazul in care fieldurile nu sunt corecte
    :param obiecte: 
    :param id: 
    :param nume_nou: 
    :param descriere_noua: 
    :param pret_achizitie_nou: 
    :param locatie_noua: 
    :return: 
    '''
    updated_list = deepcopy(obiecte)
    for obiect in updated_list:
        if get_id(obiect) == id:
            set_nume(obiect, nume_nou)
            set_descriere(obiect, descriere_noua)
            set_pret_achizitie(obiect, pret_achizitie_nou)
            set_locatie(obiect, locatie_noua)
    return updated_list

def find_obiect(obiecte, id):
    '''
    Gaseste obiecyul in obicte cu id
    :param obiecte:
    :param id:
    :return:
    '''
    for obiect in obiecte:
        if get_id(obiect) == id:
            return obiect
    return None

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
    obiecte.append(obiect)