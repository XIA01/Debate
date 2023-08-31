import reflex as rx



class State(rx.State):
    """El estado de la aplicación."""
    year: int = 2023
    bienvenido: str = "Bienvenidos a State "
    principaltitulo: str = "Página principal de "
    input_titulo: str = "Bienvenidos a Juego Debate. Ingrese su nombre y haga click en comenzar."
    nombre: str = ""
    msj_footer: str = "Juego para practicar Python y Reflex"
    
    def pasaryear(self):
        self.year += 1
    
    def cambiarnombre(self, nombre: str):
        self.nombre = nombre
    