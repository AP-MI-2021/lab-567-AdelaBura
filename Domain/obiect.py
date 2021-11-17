def get_new_object(_id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):
    '''
    Creeaza un obiect
    :param _id: id-ul obiectului, trebuie sa fie unic si int
    :param _nume: numele obiectului, nenul, string
    :param _descriere: descrierea obiectului, string
    :param _pret_achizitie: pretul achizitiei, int
    :param _locatie: locatia obiectului, string de patru caractere
    :return: obiectul
    '''
    #return [id_obiect, nume, descriere, pret_achizitie, locatie]
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret_achizitie': _pret_achizitie,
        'locatie': _locatie.zfill(4)
    }
    return obiect


def get_id(obiect):
    '''
    Getter pentru Id-ul obiectului
    :param obiect:
    :return: id - int
    '''
    return obiect['id']


def get_nume(obiect):
    '''
    Getter pentru numele obiectului
    :param obiect:
    :return: nume - string
    '''
    return obiect['nume']


def get_descriere(obiect):
    '''
    Getter pentru descrierea obiectului
    :param obiect:
    :return: descriere - string
    '''
    return obiect['descriere']


def get_pret_achizitie(obiect):
    '''
    Getter pentru pretul achizitiei
    :param obiect:
    :return: pret
    '''
    return obiect['pret_achizite']


def get_locatie(obiect):
    '''
    Getter pentru locatie
    :param obiect:
    :return: locatie
    '''
    return obiect['locatie']


def get_object_string(obiect):
    return f'Obiect cu ID-ul {get_id(obiect)}, cu numele {get_nume(obiect)}, decrierea {get_descriere(obiect)}, ' \
           f'pretul achizitiei {get_pret_achizitie(obiect)} si locatia {get_locatie(obiect)}'
