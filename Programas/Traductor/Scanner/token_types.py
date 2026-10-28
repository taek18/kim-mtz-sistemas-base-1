# Vocabulario del código fuente, mediante enumerados.
from enum import Enum, auto


class TokenType(Enum):
    # Instrucciones de Turtle
    SENTENCIA = auto()  # Auto numeración – Empieza por 1

    # DATOS PRIMITIVOS
    NUMERO = auto()
    CADENA = auto()
    BOOLEANO = auto()

    # DELIMITADORES
    COMA = auto()
    DOS_PUNTOS = auto()
    PUNTO = auto()
    PUNTO_COMA = auto()

    # OPERADORES ARITMÉTICOS
    SUMA = auto()
    RESTA = auto()
    MULTIPLICACION = auto()
    DIVISION = auto()
    MODULO = auto()
    ASIGNACION = auto()

    # OPERADORES DE COMPARACIÓN
    IGUAL = auto()
    DIFERENTE = auto()
    MENOR = auto()
    MAYOR = auto()
    MENOR_IGUAL = auto()
    MAYOR_IGUAL = auto()

    # OPERADORES LÓGICOS
    AND = auto()
    OR = auto()
    NOT = auto()

    # ESTRUCTURAS DE CONTROL
    SI = auto()
    ENTONCES = auto()
    SINO = auto()
    FIN_SI = auto()
    MIENTRAS = auto()
    FIN_MIENTRAS = auto()
    PARA = auto()
    FIN_PARA = auto()
    REPETIR = auto()
    FIN_REPETIR = auto()

    # SÍMBOLO DE AGRUPACIÓN
    LLAVE_IZQ = auto()
    LLAVE_DER = auto()
    CORCHETE_IZQ = auto()
    CORCHETE_DER = auto()
    PAREN_IZQ = auto()
    PAREN_DER = auto()

    # IDENTIFICAORES Y FUNCIONES
    ID = auto()
    FUNCION = auto()

    # LITERALES ESPECIALES
    COLOR = auto()
    DIRECCION = auto()

    # ESPECIALES
    COMENTARIO = auto()
    NUEVA_LINEA = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()

    # TOKENS
    PREGUNTA = auto()
    AMPERSAND = auto()
