from typing import List, Optional, Any
from Traductor.Error.error_types import CompilerError, NivelError, ErrorCode, ERRORES_LEXICOS
from Traductor.Scanner.ttoken import Token


class ErrorHandler:
    def __init__(self):
        self.errores: List[CompilerError] = []
        self.warnings: List[CompilerError] = []
        self.has_errores: bool = False
        self.has_warnings: bool = False

    def add_error(self, error: CompilerError):
        self.errores.append(error)
        self.has_errores = True
        if error.error_codigo.nivel == NivelError.FATAL:
            raise Exception(str(error))

    def add_warning(self, warning: CompilerError):
        self.warnings.append(warning)
        self.has_warnings = True

    def report(
            self,
            error_codigo: ErrorCode,
            mensaje: str,
            linea: int,
            columna: int,
            posicion: int = 0,
            token: Optional[Token] = None,
            contexto: Any = None,
    ):
        """Método principal para registrar errores o advertencias."""
        error = CompilerError(
            error_codigo=error_codigo,
            mensaje=mensaje,
            linea=linea,
            columna=columna,
            posicion=posicion,
            token=token,
            contexto=contexto,
        )

        if error_codigo.nivel == NivelError.WARNING:
            self.add_warning(error)
        else:
            self.add_error(error)

    # Métodos utilitarios para el Scanner
    def report_unknown_char(self, char: str, linea: int, columna: int, posicion: int):
        self.report(
            ERRORES_LEXICOS["UNKNOWN_CHAR"],
            f"Carácter no reconocido: '{char}'",
            linea,
            columna,
            posicion
        )

    def report_unterminated_string(self, linea: int, columna: int, posicion: int):
        self.report(
            ERRORES_LEXICOS["UNTERMINATED_STRING"],
            "Cadena de texto sin cerrar (falta comilla de cierre)",
            linea,
            columna,
            posicion,
        )

    def report_invalid_number(self, text: str, linea: int, columna: int, posicion: int):
        self.report(
            ERRORES_LEXICOS["INVALID_NUMBER"],
            f"Formato numérico inválido: '{text}'",
            linea,
            columna,
            posicion,
        )

    def report_invalid_escape(self, text: str, linea: int, columna: int, posicion: int):
        self.report(
            ERRORES_LEXICOS["INVALID_ESCAPE"],
            f"Secuencia de escape inválida: '{text}'",
            linea,
            columna,
            posicion,
        )

    def clear(self):
        """Limpia la colección de errores y advertencias."""
        self.errores.clear()
        self.warnings.clear()
        self.has_errores = False
        self.has_warnings = False

    def get_error_count(self) -> int:
        return len(self.errores)

    def get_warning_count(self) -> int:
        return len(self.warnings)
