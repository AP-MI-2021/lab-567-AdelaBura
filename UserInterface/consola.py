from Domain.obiect import get_str
from Logic.crud import add_obiect


def print_meniu():
    print('''
    Meniu
    1.CRUD
    2.Operatiuni
    3.Undo/Redo
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
    Adauga un obiect citit de la tastatura in lista de prajituri
    :param obiecte: lista de obiecte
    :return:
    '''
    id = input('Dati id-ul obiectului: ')
    nume = input('Dati numele obiectului: ')
    descriere = input('Dati descrierea obiectului: ')
    pret = float(input('Dati pretul obiectului: '))
    locatie = input('Dati locatia (formata din patru caractere) obiectului: ')
    add_obiect(obiecte, id, nume, descriere, pret, locatie)
    print('Obiectul a fost adaugat cu succes!')

def handle_show_all(obiecte):
    '''
        Afisare lista de obiecte din memorie
        :param obiecte:  lista de obiecte
        :return:
        '''
    for obiect in obiecte:
        print(get_str(obiect))

def run_crud_ui(obiecte):
    '''

    :param obiecte: lista de obiecte
    :return:
    '''
    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_obiect_ui(obiecte)
        elif cmd == '4':
            handle_show_all(obiecte)
        elif cmd == 'x':
            break
        else:
            print('Comanda invalida!')

def run_operatiuni_ui(obiecte):
    pass

def run_undo_redo_ui(obiecte):
    pass

def run_console(obiecte):
    '''

    :param obiecte: lista de obiecte
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(obiecte)
        if cmd == '2':
            run_operatiuni_ui(obiecte)
        if cmd == '3':
            run_undo_redo_ui(obiecte)
        elif cmd == 'x':
            break
        else:
            print('Comanda invalida!')