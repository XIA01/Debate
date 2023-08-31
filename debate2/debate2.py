"""Bienvenido a Reflex! Este archivo describe los pasos para crear una aplicación básica."""
from anyio import Event
from rxconfig import config
import reflex as rx

class State(rx.State):
    """El estado de la aplicación."""
    year: int = 2023
    bienvenido: str = "Bienvenidos a State "
    principaltitulo: str = "Página principal"
    input_titulo: str = "Bienvenidos a Juego Debate. Ingrese su nombre y haga click en comenzar."
    nombre: str = ""
    msj_footer: str = "Juego para practicar Python y Reflex"
    
    def pasaryear(self):
        self.year += 1
    
    def cambiarnombre(self, nombre: str):
        self.nombre = nombre
    

style = {
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "height": "10vh",
    "font_size": "2em",
    "text_align": "center"
}

def principal() -> rx.Container:
    return rx.container(
        rx.hstack(
            rx.text(State.principaltitulo+" "+State.nombre, style=style),
        )
    )

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text(f"{State.bienvenido} {State.year} Señor: {State.nombre}", style=style, on_click=State.pasaryear),  # Usar f-string para interpolar las variables
            rx.box(
                rx.text(State.input_titulo),
                rx.input(
                    placeholder="Nombre...",
                    on_blur=State.cambiarnombre,
                ),
                rx.link(
                    rx.button("Comenzar", color_scheme="twitter", size="md"), href='/princ'),
                rx.text(State.msj_footer),
            )
        )
    )
# Crear una instancia de la aplicación y agregar las páginas a la app.
app = rx.App()
app.add_page(index)
app.add_page(principal, route= '/princ')
app.compile()
