from typing import List, Optional
from Traductor.Error.error_types import CompilerError


class ErrorReporter:
    @staticmethod
    def format_error_with_context(error: CompilerError, source_code: str) -> str:
        """
        Formatea un error mostrando la línea exacta del código fuente y el puntero '^',
        preservando tabuladores (\t) y limpiando retornos de carro (\r).
        """
        lines = source_code.splitlines()
        if 1 <= error.linea <= len(lines):
            context_line = lines[error.linea - 1]
            prefix_chars = context_line[:max(0, error.columna - 1)]
            pointer_prefix = "".join('\t' if ch == '\t' else ' ' for ch in prefix_chars)
            pointer = pointer_prefix + " ^"
            return f"{error}\n{context_line}\n{pointer}"
        return str(error)

    @staticmethod
    def print_errors(
            errores: List[CompilerError],
            warnings: List[CompilerError],
            show_warnings: bool = True,
            source_code: Optional[str] = None
    ):
        """Imprime todos los errores y advertencias registrados."""
        if errores:
            print("\n=== ERRORES ===")
            for error in errores:
                if source_code:
                    print(ErrorReporter.format_error_with_context(error, source_code))
                else:
                    print(f"X {error}")

        if warnings and show_warnings:
            print("\n=== ADVERTENCIAS ===")
            for warning in warnings:
                if source_code:
                    print(ErrorReporter.format_error_with_context(warning, source_code))
                else:
                    print(f"! {warning}")

        print(f"\nResumen: {len(errores)} error(es), {len(warnings)} advertencia(s).")

    @staticmethod
    def generate_error_report(errores: List[CompilerError], warnings: List[CompilerError]) -> str:
        """Genera un reporte consolidado en formato texto."""
        report = []

        if errores:
            report.append("=== ERRORES ===")
            for error in errores:
                report.append(f"[ERROR] {error}")

        if warnings:
            report.append("\n=== ADVERTENCIAS ===")
            for warning in warnings:
                report.append(f"[WARNING] {warning}")

        report.append(f"\nTotal: {len(errores)} error(es), {len(warnings)} advertencia(s).")
        return "\n".join(report)
