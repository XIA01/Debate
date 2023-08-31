import reflex as rx



class State(rx.State):
    """El estado de la aplicación."""
    year: int = 2023
    bienvenido: str = "Bienvenidos a Debate "
    input_titulo: str = "Bienvenidos a Juego Debate. Ingrese su nombre y haga click en comenzar."
    nombre: str = ""
    msj_footer: str = "Juego para practicar Python y Reflex"
    
    """"Estados de pagina princ"""
    principaltitulo: str = "Preparate para debatir "
    seleccion: str = ""
    
    def cambiarnombre(self, nombre: str):
        self.nombre = nombre
    
    def selecion(self, candidato):
        self.seleccion = candidato
        self.nombre = self.seleccion