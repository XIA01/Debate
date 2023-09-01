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
    pregunta_actual: str = ""
    
    puntuacion: int = 0
    num_pregunta_actual: int = 0
    
    candidatoelegido: str = ""
    preguntas = [
        "Pregunta 1: ¿Cuál es la capital de Francia?",
        "Pregunta 2: ¿Cuánto es 2 + 2?",
        # Agrega más preguntas aquí
        ]
    respuestas = {
        "Milei": [
            ["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"],
            ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"],
            # ... y así sucesivamente para cada pregunta
        ],
        "Masa": [
            ["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"],
            ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"],
            # ... y así sucesivamente para cada pregunta
        ],
        "Bullrich": [
            ["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"],
            ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"],
            # ... y así sucesivamente para cada pregunta
        ],
        # ... y así sucesivamente para cada candidato
                }
    
    

    
    
    def respondio(self, respuesta: str):
        if respuesta == "Bien":
            self.puntuacion_increment()
        elif respuesta == "Mal":
            self.puntuacion -= 1
        elif respuesta == "Nulo":
            self.puntuacion += 0 
        self.preg_actual()
    
    def cambiarnombre(self, nombre: str):
        self.nombre = nombre
    
    def selecion(self, candidato):
        self.seleccion = candidato
        self.preg_actual()
        
    def preg_actual(self):
        self.pregunta_actual= self.preguntas[self.num_pregunta_actual]
        self.num_pregunta_actual += 1
        
    def puntuacion_increment(self):
        self.puntuacion +=1
    