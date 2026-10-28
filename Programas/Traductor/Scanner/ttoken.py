from dataclasses import dataclass
from typing import Any
from token_types import TokenType

@dataclass
class Token:
    type: TokenType
    value: Any
    linea: int
    columna: int = 1
    posicion: int = 0

    def __str__(self) -> str:
        return f"Token({self.type}, {repr(self.value)}, linea={self.linea}, col={self.columna})"

    def __repr__(self) -> str:
        return (f"Token(type={self.type}, value={self.value!r}, "
                f"linea={self.linea}, columna={self.columna}, posicion={self.posicion})")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Token):
            return False
        return self.type == other.type and self.value == other.value

    # token.is_type(TokenType.NUMERO)
    def is_type(self, token_type: TokenType) -> bool:
        return self.type == token_type

    # token.has_value("avanzar")
    def has_value(self, expected_value: Any) -> bool:
        return self.value == expected_value

    # token.matches(TokenType.NUMERO, 100)
    def matches(self, token_type: TokenType, value: Any = None) -> bool:
        if value is None:
            return self.is_type(token_type)
        return self.is_type(token_type) and self.has_value(value)

    # Métodos específicos para tipos comunes
    def is_sentence(self) -> bool:
        return self.is_type(TokenType.SENTENCIA)

    def is_numeric(self) -> bool:
        return self.is_type(TokenType.NUMERO)

    def is_identifier(self) -> bool:
        return self.is_type(TokenType.ID)

    def is_string(self) -> bool:
        return self.is_type(TokenType.CADENA)

    def is_boolean(self) -> bool:
        return self.is_type(TokenType.BOOLEANO)

    def is_keyword(self) -> bool:
        return self.is_type in [
            TokenType.SI,
            TokenType.ENTONCES,
            TokenType.SINO,
            TokenType.FIN_SI,
            TokenType.MIENTRAS,
            TokenType.FIN_MIENTRAS,
            TokenType.PARA,
            TokenType.FIN_PARA,
            TokenType.REPETIR,
            TokenType.FIN_REPETIR,
            TokenType.FUNCION,
        ]

    def is_operator(self) -> bool:
        return self.is_type in [
            TokenType.ASIGNACION,
            TokenType.SUMA,
            TokenType.RESTA,
            TokenType.MULTIPLICACION,
            TokenType.DIVISION,
            TokenType.MODULO,
            TokenType.IGUAL,
            TokenType.DIFERENTE,
            TokenType.MENOR,
            TokenType.MAYOR,
            TokenType.MENOR_IGUAL,
            TokenType.MAYOR_IGUAL,
            TokenType.AND,
            TokenType.OR,
            TokenType.NOT,
        ]

    def is_comparison_operator(self) -> bool:
        return self.is_type in [
            TokenType.SI,
            TokenType.ENTONCES,
            TokenType.SINO,
            TokenType.FIN_SI,
            TokenType.MIENTRAS,
            TokenType.FIN_MIENTRAS,
            TokenType.PARA,
            TokenType.FIN_PARA,
            TokenType.REPETIR,
            TokenType.FIN_REPETIR,
            TokenType.FUNCION,
        ]

    def is_arithmetic_operator(self) -> bool:
        return self.is_type in [
            TokenType.SUMA,
            TokenType.RESTA,
            TokenType.ASIGNACION,
            TokenType.MULTIPLICACION,
            TokenType.DIVISION,
            TokenType.MODULO,
        ]

    def is_delimiter(self) -> bool:
        return self.is_type in [
            TokenType.DOS_PUNTOS,
            TokenType.COMA,
            TokenType.PUNTO,
            TokenType.PUNTO_COMA,
        ]

    def is_grouping(self) -> bool:
        return self.is_type in [
            TokenType.LLAVE_IZQ,
            TokenType.LLAVE_DER,
            TokenType.CORCHETE_IZQ,
            TokenType.CORCHETE_DER,
            TokenType.PAREN_IZQ,
            TokenType.PAREN_DER,
        ]

    def is_color(self) -> bool:
        return self.is_type(TokenType.COLOR)

    def is_direction(self) -> bool:
        return self.is_type(TokenType.DIRECCION)

    def is_eof(self) -> bool:
        return self.is_type(TokenType.EOF)

    def is_comment(self) -> bool:
        return self.is_type(TokenType.COMENTARIO)

    # Métodos adicionales para estructuras de control específicas
    def is_if(self) -> bool:
        return self.matches(TokenType.SI, "si")

    def is_else(self) -> bool:
        return self.matches(TokenType.SINO, "sino")

    def is_while(self) -> bool:
        return self.matches(TokenType.MIENTRAS, "mientras")

    def is_for(self) -> bool:
        return self.matches(TokenType.PARA, "para")

    def is_repeat(self) -> bool:
        return self.matches(TokenType.REPETIR, "repetir")

    def is_endif(self) -> bool:
        return self.matches(TokenType.FIN_SI, "fin_si")

    def is_endwhile(self) -> bool:
        return self.matches(TokenType.FIN_MIENTRAS, "fin_mientras")

    def is_endfor(self) -> bool:
        return self.matches(TokenType.FIN_PARA, "fin_para")

    def is_endrepeat(self) -> bool:
        return self.matches(TokenType.FIN_REPETIR, "fin_repetir")

    # MATCHES

    #   Operadores
    def is_addition(self) -> bool:
        return self.matches(TokenType.SUMA, "+")

    def is_substraction(self) -> bool:
        return self.matches(TokenType.RESTA, "-")

    def is_multiplication(self) -> bool:
        return self.matches(TokenType.MULTIPLICACION, "*")

    def is_division(self) -> bool:
        return self.matches(TokenType.DIVISION, "/")

    def is_modulo(self) -> bool:
        return self.matches(TokenType.MODULO, "%")

    def is_assign(self) -> bool:
        return self.matches(TokenType.ASIGNACION, "=")

    #   Agrupación
    def is_leftbrace(self) -> bool:
        return self.matches(TokenType.LLAVE_IZQ, "{")

    def is_rightbrace(self) -> bool:
        return self.matches(TokenType.LLAVE_DER, "}")

    def is_leftbracket(self) -> bool:
        return self.matches(TokenType.CORCHETE_IZQ, "[")

    def is_rightbracket(self) -> bool:
        return self.matches(TokenType.CORCHETE_DER, "]")

    def is_leftparenthesis(self) -> bool:
        return self.matches(TokenType.PAREN_IZQ, "(")

    def is_rightparenthesis(self) -> bool:
        return self.matches(TokenType.PAREN_DER, ")")

    # Delimitadores
    def is_coma(self) -> bool:
        return self.matches(TokenType.COMA, ",")

    def is_colon(self) -> bool:
        return self.matches(TokenType.DOS_PUNTOS, ":")

    def is_dot(self) -> bool:
        return self.matches(TokenType.PUNTO, ".")

    def is_semicolon(self) -> bool:
        return self.matches(TokenType.PUNTO_COMA, ";")