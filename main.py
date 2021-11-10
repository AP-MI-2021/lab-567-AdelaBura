from Tests.run_all_tests import run_all_tests
from Tests.test_operatii import test_operatii
from UserInterface.consola import run_console

def main():
    test_operatii()
    obiecte = []
    run_console(obiecte)

main()