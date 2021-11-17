from Domain.obiect2 import get_pret_achizitie


def ordonare_lista(lista: list):
    '''
    Ordoneaza lista dupa pretul achizitiei
    :param lista: listaa obicte
    :return: lista cu obicetele ordonate dupa pret
    '''
    return sorted(lista, key=get_pret_achizitie)
