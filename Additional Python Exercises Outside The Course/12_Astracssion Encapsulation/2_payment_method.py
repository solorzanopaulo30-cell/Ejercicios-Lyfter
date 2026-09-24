#`@property`, `@setter`, atributos privados (`_algo`), `ABC`, `@abstractmethod`.
#2. Cree una clase abstracta `MetodoPago` con un método abstracto `procesar_pago()`, y clases hijas `PagoTarjeta` y `PagoEfectivo`.

from abc import ABC, abstractmethod


class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass


class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta, fecha_expiracion, cvv):
        self._numero_tarjeta = numero_tarjeta
        self._fecha_expiracion = fecha_expiracion
        self._cvv = cvv

    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta

    @property
    def fecha_expiracion(self):
        return self._fecha_expiracion

    @property
    def cvv(self):
        return self._cvv

    def procesar_pago(self):
        print(f"Procesando pago con tarjeta: {self.numero_tarjeta}")


class PagoEfectivo(MetodoPago):
    def __init__(self, monto):
        self._monto = monto

    @property
    def monto(self):
        return self._monto

    def procesar_pago(self):
        print(f"Procesando pago en efectivo por un monto de: {self.monto}")