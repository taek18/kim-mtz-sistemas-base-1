from Traductor.Error.error_handler import ErrorHandler
from Traductor.Error.error_reporter import ErrorReporter
from scanner import Scanner


def main():
    code = '''
    avanzar 100 $
    girar 90
    si verdadero entonces
        rotulo "Hola Mundo
    fin_si
    '''

    error_handler = ErrorHandler()
    scanner = Scanner(code, error_handler)
    tokens = scanner.scan_tokens()

    # Mostrar tokens
    for token in tokens:
        print(token)

    ErrorReporter.print_errors(
        error_handler.errores,
        error_handler.warnings,
        source_code=code
    )


if __name__ == '__main__':
    main()
