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


if __name__ == '__main__':
    test_change_location()
    test_concatenare()
    test_ordonare()
    test_pret_max_per_location()
    test_sume_pret()
    test_undo_redo()
    main()