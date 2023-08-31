"""Bienvenido a Reflex! Este archivo describe los pasos para crear una aplicación básica."""

from rxconfig import config
import reflex as rx
from debate2.state import *
from debate2.princ import *




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
        titulo(),
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
