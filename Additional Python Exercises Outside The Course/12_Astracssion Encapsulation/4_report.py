#`@property`, `@setter`, atributos privados (`_algo`), `ABC`, `@abstractmethod`.
#4. Cree una clase abstracta `Reporte` con un método abstracto `generar()`, y 2 clases hijas que lo implementen distinto.

from abc import ABC, abstractmethod


class Reporte(ABC):
    @abstractmethod
    def generar(self):
        pass


class ReportePDF(Reporte):
    def generar(self):
        return "Generando reporte en formato PDF"


class ReporteExcel(Reporte):
    def generar(self):
        return "Generando reporte en formato Excel"


pdf = ReportePDF()
excel = ReporteExcel()

print(pdf.generar())
print(excel.generar())


reporte = Reporte()