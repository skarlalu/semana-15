class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str, clave: str = ""):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.clave = clave

    def a_diccionario(self) -> dict:
        """Convierte el objeto Usuario en un diccionario para la persistencia o manejo de datos."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "clave": self.clave
        }