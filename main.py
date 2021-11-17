from Domain.obiect2 import get_new_object
from Logic.crud import create
from Tests.test_operatii import test_concatenare
from Tests.test_operatii import test_pret_max_per_location
from Tests.test_operatii import test_change_location
from Tests.test_operatii import test_ordonare
from Tests.test_undo_si_redo import test_undo_redo
from Tests.test_operatii import test_sume_pret
from UserInterface.consola import header


def main():
    lista = []
    lista = header(lista)


def main2():
    lista = []
    obiect1 = get_new_object(1, 'birou', 'desc 1', 450, 'l111')
    lista = create(lista, obiect1)
    obiect2 = get_new_object(2, 'scaun', 'desc 2', 100, 'l111')
    lista = create(lista, obiect2)
    obiect3 = get_new_object(3, 'masa', 'desc 3', 330, 'l121')
    lista = create(lista, obiect3)
    obiect4 = get_new_object(4, 'frigider', 'desc 4', 2900, 'l112')
    lista = create(lista, obiect4)
    obiect5 = get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112')
    lista = create(lista, obiect5)
    obiect6 = get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    lista = create(lista, obiect6)



if __name__ == '__main__':
    test_change_location()
    test_concatenare()
    test_ordonare()
    test_pret_max_per_location()
    test_sume_pret()
    test_undo_redo()
    main()