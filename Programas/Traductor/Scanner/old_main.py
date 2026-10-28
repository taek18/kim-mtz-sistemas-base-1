from Traductor.Scanner.token_types import TokenType
from Traductor.Scanner.ttoken import Token


def main():
    # Declaración de tokens que emulan la lectura del compilador
    secuencia_tokens = [
        Token(TokenType.SENTENCIA, "avanzar", linea=1, columna=1, posicion=0),
        Token(TokenType.NUMERO, 100, linea=1, columna=9, posicion=8),
        Token(TokenType.NUEVA_LINEA, "\n", linea=1, columna=12, posicion=11),
        Token(TokenType.SI, "si", linea=2, columna=1, posicion=12),
        Token(TokenType.BOOLEANO, True, linea=2, columna=4, posicion=15),
        Token(TokenType.ENTONCES, "entonces", linea=2, columna=14, posicion=25),
        Token(TokenType.NUEVA_LINEA, "\n", linea=2, columna=22, posicion=33),
        Token(TokenType.SENTENCIA, "rotulo", linea=3, columna=5, posicion=38),
        Token(TokenType.CADENA, "Hola Mundo", linea=3, columna=12, posicion=45),
        Token(TokenType.NUEVA_LINEA, "\n", linea=3, columna=24, posicion=57),
        Token(TokenType.FIN_SI, "fin_si", linea=4, columna=1, posicion=58),
        Token(TokenType.EOF, "", linea=4, columna=7, posicion=64),
    ]

    print("=== FLUJO DE TOKENS DEL SCANNER (SIMULADO) ===")
    for token in secuencia_tokens:
        print(token)


if __name__ == "__main__":
    main()