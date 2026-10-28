from typing import Any, Dict, List, Optional
from ttoken import Token
from token_types import TokenType
from Traductor.Error.error_handler import ErrorHandler
from Traductor.table_symbol import TablaSimbolos


class Scanner:
    def __init__(self, fuente: str, error_handler: Optional[ErrorHandler] = None, tabla_simbolos: Optional[TablaSimbolos] = None):
        self.fuente = fuente
        self.tokens: List[Token] = []
        self.inicio = 0
        self.actual = 0
        self.linea = 1
        self.columna = 1
        self.posicion = 0

        # Inyección del manejador de errores
        self.error_handler = error_handler if error_handler is not None else ErrorHandler()

        # Tabla de símbolos
        self.tabla_simbolos = tabla_simbolos if tabla_simbolos is not None else TablaSimbolos()

        # Palabras clave y sus correspondientes tipos de token
        self.keywords: Dict[str, TokenType] = {
            'si': TokenType.SI,
            'entonces': TokenType.ENTONCES,
            'sino': TokenType.SINO,
            'fin_si': TokenType.FIN_SI,
            'mientras': TokenType.MIENTRAS,
            'fin_mientras': TokenType.FIN_MIENTRAS,
            'para': TokenType.PARA,
            'fin_para': TokenType.FIN_PARA,
            'repetir': TokenType.REPETIR,
            'fin_repetir': TokenType.FIN_REPETIR,
            'funcion': TokenType.FUNCION,
            'verdadero': TokenType.BOOLEANO,
            'falso': TokenType.BOOLEANO,
            'y': TokenType.AND,
            'o': TokenType.OR,
            '!': TokenType.NOT,
        }

        # Instrucciones específicas de turtle
        self.turtle_instructions = {
            'avanzar',
            'retroceder',
            'derecha',
            'izquierda',
            'posicionar',
            'poner_x',
            'poner_y',
            'circulo',
            'velocidad',
            'bajar_lapiz',
            'levantar_lapiz',
            'grosor_lapiz',
            'color_lapiz',
            'rellenar_color',
            'comenzar_relleno',
            'terminar_relleno',
            'reiniciar',
            'limpiar',
            'escribir',
            'mostrar_tortuga',
            'ocultar_tortuga',
            'forma',
            'posicion',
            'coord_x',
            'coord_y',
            'direccion',
            'distancia',
            'grados',
            'radianes',
            'esta_bajado',
            'color',
            'es_visible',
            'girar',
            'grosor',
            'rotulo',
        }

        # Colores predefinidos
        self.colors = {
            'rojo',
            'azul',
            'verde',
            'amarillo',
            'negro',
            'blanco',
            'naranja',
            'morado',
            'rosa',
            'gris',
            'marron',
            'cyan',
        }

        # Direcciones predefinidas
        self.directions = {'norte', 'sur', 'este', 'oeste'}

    def scan_tokens(self) -> List[Token]:
        """Escanea todo el código fuente y devuelve una lista de tokens"""
        while not self.is_at_end():
            self.inicio = self.actual
            self.scan_token()

        # Añadir token de fin de archivo
        self.add_token(TokenType.EOF, "")
        return self.tokens

    def scan_token(self):
        """Procesa el siguiente simbolo"""
        c = self.advance()

        # Tokens de un solo caracter
        if c == '(':
            self.add_token(TokenType.PAREN_IZQ)
        elif c == ')':
            self.add_token(TokenType.PAREN_DER)
        elif c == '{':
            self.add_token(TokenType.LLAVE_IZQ)
        elif c == '}':
            self.add_token(TokenType.LLAVE_DER)
        elif c == '[':
            self.add_token(TokenType.CORCHETE_IZQ)
        elif c == ']':
            self.add_token(TokenType.CORCHETE_DER)
        elif c == ',':
            self.add_token(TokenType.COMA)
        elif c == '.':
            self.add_token(TokenType.PUNTO)
        elif c == ';':
            self.add_token(TokenType.PUNTO_COMA)
        elif c == ':':
            self.add_token(TokenType.DOS_PUNTOS)
        elif c == '?':
            self.add_token(TokenType.PREGUNTA)
        elif c == '&':
            self.add_token(TokenType.AMPERSAND)

        # Operadores de uno o dos caracteres
        elif c == '=':
            self.add_token(
                TokenType.IGUAL if self.match('=') else TokenType.ASIGNACION
            )
        elif c == '!':
            self.add_token(
                TokenType.DIFERENTE if self.match('=') else TokenType.NOT
            )
        elif c == '<':
            self.add_token(
                TokenType.MENOR_IGUAL if self.match('=') else TokenType.MENOR
            )
        elif c == '>':
            self.add_token(
                TokenType.MAYOR_IGUAL if self.match('=') else TokenType.MAYOR
            )
        elif c == '+':
            self.add_token(TokenType.SUMA)
        elif c == '-':
            self.add_token(TokenType.RESTA)
        elif c == '*':
            self.add_token(TokenType.MULTIPLICACION)
        elif c == '/':
            self.add_token(TokenType.DIVISION)
        elif c == '%':
            self.add_token(TokenType.MODULO)

        # Espacios en blanco
        elif c in ' \t\r':
            pass  # Ignorar espacios en blanco

        # Nueva línea
        elif c == '\n':
            self.add_token(TokenType.NUEVA_LINEA)
            self.linea += 1
            self.columna = 0

        # Cadenas de texto
        elif c == '"':
            self.string()

        # Números
        elif c.isdigit():
            self.number()

        # Identificadores y palabras clave
        elif c.isalpha() or c == '_':
            self.identifier()

        else:
            '''
            # Carácter no reconocido, por el momento el error lo gestionara el scanner
            raise Exception(
                f"Carácter no reconocido '{c}' en línea {self.linea}, columna {self.columna}"
            )
            '''

            # En lugar de lanzar una excepción, se reporta al error_handler
            col_error = max(1, self.columna - 1)
            # self.error_handler.report_unknown_char(c, self.linea, col_error, self.columna)
            self.error_handler.report_unknown_char(c, self.linea, col_error, self.columna)

    def identifier(self):
        """Procesa un identificador o palabra clave"""
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()

        text = self.fuente[self.inicio:self.actual]

        # Verificar si es una palabra clave
        if text in self.keywords:
            token_type = self.keywords[text]
            self.add_token(token_type, text)
        # Verificar si es una instrucción de turtle
        elif text in self.turtle_instructions:
            self.add_token(TokenType.SENTENCIA, text)
        # Verificar si es un color
        elif text in self.colors:
            self.add_token(TokenType.COLOR, text)
        # Verificar si es una dirección
        elif text in self.directions:
            self.add_token(TokenType.DIRECCION, text)
        # Es un identificador regular
        else:
            columna_inicio = self.columna - (self.actual - self.inicio)
            posicion_inicio = self.inicio

            simbolo_ref = self.tabla_simbolos.registrar_o_recuperar(
                nombre=text,
                linea=self.linea,
                columna=columna_inicio,
                posicion=posicion_inicio
            )
            self.add_token(TokenType.ID, simbolo_ref)

    def number(self):
        """Procesa un número (entero o decimal)"""
        while self.peek().isdigit():
            self.advance()

        # Parte decimal
        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()  # Consume el punto
            while self.peek().isdigit():
                self.advance()

        text = self.fuente[self.inicio:self.actual]
        value = float(text) if "." in text else int(text)
        self.add_token(TokenType.NUMERO, value)

    def string(self):
        linea_inicio = self.linea
        col_inicio = max(1, self.columna - 1)
        pos_inicio = self.inicio
        """Procesa una cadena de texto entre comillas"""
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.linea += 1
                self.columna = 0
            self.advance()

        if self.is_at_end():
            self.error_handler.report_unterminated_string(
                linea=linea_inicio,
                columna=col_inicio,
                posicion=pos_inicio
            )
            return
        self.advance()  # Consume la comilla de cierre
        # Extrae el valor sin las comillas
        value = self.fuente[self.inicio + 1:self.actual - 1]
        self.add_token(TokenType.CADENA, value)

    def add_token(self, token_type: TokenType, value: Any = None):
        """Añade un nuevo token a la lista"""
        if value is None:
            value = self.fuente[self.inicio: self.actual]

        # Calcular la columna exacta de inicio del lexema
        columna = self.columna - (self.actual - self.inicio)

        self.tokens.append(
            Token(
                type=token_type,
                value=value,
                linea=self.linea,
                columna=columna,
                posicion=self.inicio,
            )
        )

    def advance(self) -> str:
        """Devuelve el siguiente carácter a analizar y avanza la posición"""
        if self.is_at_end():
            return '\0'

        c = self.fuente[self.actual]
        self.actual += 1
        self.columna += 1
        self.posicion += 1
        return c

    def peek(self) -> str:
        """Mira el siguiente carácter sin consumirlo"""
        if self.is_at_end():
            return '\0'
        return self.fuente[self.actual]

    def peek_next(self) -> str:
        """Mira el carácter después del siguiente sin consumirlo"""
        if self.actual + 1 >= len(self.fuente):
            return '\0'
        return self.fuente[self.actual + 1]

    def is_at_end(self) -> bool:
        """Verifica si se ha llegado al final del código fuente"""
        return self.actual >= len(self.fuente)

    def match(self, expected: str) -> bool:
        """Verifica si el siguiente carácter coincide con el esperado"""
        if self.is_at_end():
            return False
        if self.fuente[self.actual] != expected:
            return False

        self.actual += 1
        self.columna += 1
        self.posicion += 1
        return True
