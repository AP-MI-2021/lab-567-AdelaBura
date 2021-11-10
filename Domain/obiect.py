def creeaza_obiectul(id_obiect, nume, descriere, pret_achizitie, locatie):
    '''
    Creeaza un obiect.
    :param id_obiect: id-ul obiectului, trebuie sa fie unic
    :param nume: numele obiectului, nenul
    :param descriere: descrierea obiectului, nenul
    :param pret_achizitie: pretul achizitiei
    :param locatie: locatia
    :return: un obiect
    '''
    return [id_obiect, nume, descriere, pret_achizitie, locatie]

  # return {
  #      "id_obiect": id_obiect,
  #      "nume": nume,
  #     "descriere": descriere,
  #      "pret_achizitie": pret_achizitie,
  #     "locatie": locatie
  #  }

def get_id(obiect):
    '''
    Getter pentru Id-ul obiectului
    :param obiect: Dict
    :return: id - string
    '''
    return obiect[0]
    #return obiect['id_obiect']

def set_id(obiect, id):
    '''
    Setter pentru Id-ul obiectului
    :param obiect:
    :return:
    '''
    obiect['id'] = id

def get_nume(obiect):
    '''
    Getter pentru numele obiectului
    :param obiect: Dict
    :return: nume - string
    '''
    return obiect[1]
    #return obiect['nume']

def set_nume(obiect, nume):
    '''
    Setter pentru numele obiectului
    :param obiect:
    :return:
    '''
    obiect['nume'] = nume

def get_descriere(obiect):
    '''
    Getter pentru descrierea obiectului
    :param obiect: Dict
    :return: descriere - string
    '''
    return obiect[2]
    #return obiect['descriere']

def set_descriere(obiect, descriere):
    '''
    Setter pentru descrierea obiectului
    :param obiect:
    :return:
    '''
    obiect['descriere'] = descriere

def get_pret_achizitie(obiect):
    '''
    Getter pentru pretul achizitiei
    :param obiect: Dict
    :return: pret - float
    '''
    return obiect[3]
    #return obiect['pret_achizitie']

def set_pret_achizitie(obiect, pret_achizitie):
    '''
    Setter pentru pretul achizitiei
    :param obiect:
    :return:
    '''
    obiect['pret_achizitie'] = pret_achizitie

def get_locatie(obiect):
    '''
    Getter pentru locatie
    :param obiect: Dict
    :return: locatie
    '''
    return obiect[4]
    #return obiect['locatie']

def set_locatie(obiect, locatie):
    '''
    Setter pentru locatie
    :param obiect:
    :return:
    '''
    obiect['locatie'] = locatie

def  get_str(obiect):
    return f'Obiect cu id-ul {get_id(obiect)}, cu numele {get_nume(obiect)}, la pretul de {get_pret_achizitie(obiect)}, descriere: {get_descriere(obiect)}, si localizat: {get_locatie(obiect)}'