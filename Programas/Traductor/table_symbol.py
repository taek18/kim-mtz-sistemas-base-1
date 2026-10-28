from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Simbolo:
    nombre: str
    linea_primera_aparicion: int
    columna_primera_aparicion: int
    posicion_fuente: int
    tipo_dato: Optional[Any] = None
    inicializado: bool = False
    valor: Optional[Any] = None

    def __repr__(self) -> str:
        return f"Símbolo(nombre={self.nombre}, primera_vez_en_linea={self.linea_primera_aparicion})"


class TablaSimbolos:
    def __init__(self):
        self.simbolos: Dict[str, Simbolo] = {}

    def registrar_o_recuperar(self, nombre: str, linea: int, columna: int, posicion: int) -> Simbolo:
        if nombre in self.simbolos:
            return self.simbolos[nombre]

        nuevo_simbolo = Simbolo(
            nombre=nombre,
            linea_primera_aparicion=linea,
            columna_primera_aparicion=columna,
            posicion_fuente=posicion,
        )
        self.simbolos[nombre] = nuevo_simbolo
        return nuevo_simbolo

    def buscar(self, nombre: str) -> Optional[Simbolo]:
        return self.simbolos.get(nombre, None)

    def contiene(self, nombre: str) -> bool:
        return nombre in self.simbolos

    def mostrar_tabla(self):
        print("=== CONTENIDO DE LA TABLA DE SÍMBOLOS ===")
        for key, symbol in self.simbolos.items():
            print(f"ID: {key:15} "
                  f"| Declarado en línea: {symbol.linea_primera_aparicion:<3} "
                  f"| Columna: {symbol.columna_primera_aparicion:<3} "
                  f"| Inicializado: {symbol.inicializado}")
