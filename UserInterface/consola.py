from Domain.obiect import creeaza_obiectul, get_str
from Logic.crud import add_obiect, delete_obiect, edit_obiect
from Logic.operatii import get_all_locations, get_max_price, muta_obiect


def print_meniu():
    print('''
    Meniu
    1.CRUD
    2.Muta locatia tuturor obiectelor din locatia initiala
    3.Determinarea celui mai mare preț pentru fiecare locație.
    x.Iesire
    ''')

def print_crud_meniu():
    print('''
    Meniu CRUD
    1.Adaugarea de elemente in lista   
    2.Modificarea unui obiect din lista
    3.Stergerea unui obiect din lista
    4.Afisarea unei liste cu toate obiectele
    x.Inapoi la Meniu
    ''')

def handle_add_obiect_ui(obiecte):
    '''
    Adauga un obiect citit de la tastatura in lista de obiecte
    :param obiecte: lista de obiecte
    :return:
    '''
    id = int(input('Dati id-ul obiectului: '))
    nume = input('Dati numele obiectului: ')
    descriere = input('Dati descrierea obiectului: ')
    pret = float(input('Dati pretul obiectului: '))
    locatie = input('Dati locatia (formata din patru caractere) obiectului: ')
    obiecte = add_obiect(obiecte, id, nume, descriere, pret, locatie)
    return obiecte
    print('Obiectul a fost adaugat cu succes!')

def handle_update_obiecte(obiecte):
    '''
    Modifica un obiect identificat din lista de obiecte
    :param obiecte:
    :return:
    '''
    id = int(input('Dati id-ul obiectului: '))
    nume = input('Dati numele obiectului: ')
    descriere = input('Dati descrierea obiectului: ')
    pret = float(input('Dati pretul obiectului: '))
    locatie = input('Dati locatia (formata din patru caractere) obiectului: ')
    return edit_obiect(obiecte,creeaza_obiectul(id, nume, descriere, pret, locatie))

def handle_show_all(obiecte):
    '''
        Afisare lista de obiecte din memorie
        :param obiecte:  lista de obiecte
        :return:
        '''
    for obiect in obiecte:
        print(get_str(obiect))

def handle_delete_obiect(obiecte):
    '''
    Sterge un obiect din lista de obiecte
    :param obiecte:
    :return:
    '''
    id_obiect = int(input('Dati id-ul obiectului pe care doriti sa il stergeti: '))
    return delete_obiect(obiecte, id_obiect)

def handle_move_location(obiecte):
    locatie_initiala = input('Dati locatia initiala: ')
    locatie_noua = input('Dati locatia in care vreti sa mutati obiectele: ')
    obiecte = muta_obiect(obiecte, locatie_initiala, locatie_noua)
    return obiecte

def handle_highest_price(obiecte):
    lista_locatii = get_all_locations(obiecte)
    for locatie in lista_locatii:
        pret_maxim = get_max_price(obiecte, locatie)
        print(f'Pretul maxim pentru locatia {locatie} este {pret_maxim}.')
    
def run_crud_ui(obiecte):
    '''
    :param obiecte: lista de obiecte
    :return:
    '''
    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            obiecte = handle_add_obiect_ui(obiecte)
        elif cmd == '2':
            obiecte = handle_update_obiecte(obiecte)
            print('Obiectul a fost modificat cu succes!')
        elif cmd == '3':
            obiecte = handle_delete_obiect(obiecte)
        elif cmd == '4':
            handle_show_all(obiecte)
        elif cmd == 'x':
            break
        else:
            print('Comanda invalida!')
    return obiecte

def run_console(obiecte):
    '''
    :param obiecte: lista de obiecte
    :return:
    '''

    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            obiecte = run_crud_ui(obiecte)
        if cmd == '2':
            obiecte = handle_move_location(obiecte)
        if cmd == '3':
            handle_highest_price(obiecte)
        elif cmd == 'x':
            break
        else:
            print('Comanda invalida!')