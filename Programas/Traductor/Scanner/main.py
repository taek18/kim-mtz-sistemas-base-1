from scanner import Scanner


def main():
    pseudocode = '''
    avanzar 100
    girar 90
    si verdadero entonces
        rotulo "Hola Mundo"
    fin_si
    '''

    scanner = Scanner(pseudocode)
    tokens = scanner.scan_tokens()

    # Mostrar tokens
    for token in tokens:
        print(token)


if __name__ == '__main__':
    main()
