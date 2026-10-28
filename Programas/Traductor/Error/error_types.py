from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Any
from Traductor.Scanner.ttoken import Token


class NivelError(Enum):
    WARNING = auto()
    ERROR = auto()
    FATAL = auto()


class FaseError(Enum):
    LEXICO = 'Léxico'
    SINTAXIS = 'Sintáctico'
    SEMANTICO = 'Semántico'
    RUNTIME = 'Ejecución'


@dataclass
class ErrorCode:
    codigo: str
    descripcion: str
    nivel: NivelError
    fase: FaseError


# Catálogo de errores léxicos
ERRORES_LEXICOS = {
    "UNKNOWN_CHAR": ErrorCode('L001', 'Caracter desconocido', NivelError.ERROR, FaseError.LEXICO),
    "UNTERMINATED_STRING": ErrorCode('L002', 'Cadena sin terminar', NivelError.ERROR, FaseError.LEXICO),
    "INVALID_NUMBER": ErrorCode('L003', 'Número inválido', NivelError.ERROR, FaseError.LEXICO),
    "INVALID_ESCAPE": ErrorCode('L004', 'Secuencia de escape inválida', NivelError.ERROR, FaseError.LEXICO),
}

# Catálogo de errores sintácticos (preparando para la siguiente fase)
ERRORES_SINTAXIS = {
    "UNEXPECTED_TOKEN": ErrorCode('S001', 'Token inesperado', NivelError.ERROR, FaseError.SINTAXIS),
    "MISSING_TOKEN": ErrorCode('S002', 'Token esperado no encontraado', NivelError.ERROR, FaseError.SINTAXIS),
    "INCOMPLETE_EXPRESSION": ErrorCode('S003', 'Expresión incompleta', NivelError.ERROR, FaseError.SINTAXIS),
}

# Catálogo de errores semánticos
ERRORES_SEMANTICOS = {
    "UNDEFINED_VARIABLE": ErrorCode('E001', 'Variable no definida', NivelError.ERROR, FaseError.SEMANTICO),
    "TYPE_MISMATCH": ErrorCode('E002', 'Incompatibilidad de tipos', NivelError.ERROR, FaseError.SEMANTICO),
    "DIVISION_BY_ZERO": ErrorCode('E003', 'División por cero', NivelError.FATAL, FaseError.SEMANTICO),
    "USE_BEFORE_INICIALIZATION": ErrorCode('E004', 'Variable usada sin inicializar', NivelError.ERROR,
                                           FaseError.SEMANTICO),
}


@dataclass
class CompilerError:
    error_codigo: ErrorCode
    mensaje: str
    linea: int
    columna: int
    posicion: int = 0
    token: Optional[Token] = None
    contexto: Optional[Any] = None

    def __str__(self) -> str:
        return (f"[{self.error_codigo.fase.value} | Error {self.error_codigo.codigo}: "
                f"{self.mensaje} (Línea {self.linea}, Columna {self.columna})")
