from Domain.obiect2 import get_pret_achizitie, get_id, get_nume, get_descriere, get_new_object, get_locatie


def concatenare_string(element1: str, element2: str):
    '''
    Concateneaza doua stringuri
    :param element1: string 1
    :param element2: string 2
    :return: concatenarea elem1 si elem2
    '''
    return element1 + element2

def concatenare(lista, string_citit, pret):
    '''
    Concateneaza un string citit la descrierea obiectelor din lista care au un pret mai mare decat o valoare citita
    :param lista: lista de obiecte
    :param string_citit: stringul de concatenat la descriere
    :param pret: pretul dat
    :return: o noua lista in care elementele cu un pret mai mare decat valoarea data au concatenat la descriere stringul citit
    '''
    if type(pret) is not int:
        raise ValueError('Dati id-ul un numar intreg!')
    rezultat = []
    for element in lista:
        if get_pret_achizitie(element) <= pret:
            rezultat.append(element)
        else:
            id1 = get_id(element)
            nume = get_nume(element)
            descriere = concatenare_string(get_descriere(element), string_citit)
            pret_achizitie = get_pret_achizitie(element)
            locatie = get_locatie(element)
            obiect = get_new_object(id1, nume, descriere, pret_achizitie, locatie)
            rezultat.append(obiect)
    return rezultat