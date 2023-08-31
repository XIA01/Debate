from typing import Self
import reflex as rx
from debate2.state import *

def titulo():
    return rx.container(
        rx.hstack(
            rx.text(State.principaltitulo+" "+State.nombre, color_scheme="twitter"),
        )
    )

def seleccionar() -> rx.Container:
    candidatos = ["Milei", "Masa", "Bullrich"]

    foto_style = {
        "width": "50%",
        "height": "100%",
        "background-color": "lightgray"
    }

    boton_style = {
        "margin": "10px",
        "padding": "10px",
        "background-color": "blue",
        "color": "white",
        "border": "none",
        "cursor": "pointer",
        "border-radius": "5px"
    }

    boton_milei = rx.button("Milei", style=boton_style, on_click=State.selecion("Milei"))
    boton_masa = rx.button("Masa", style=boton_style, on_click=State.selecion("Masa"))
    boton_bullrich = rx.button("Bullrich", style=boton_style, on_click=State.selecion("Bullrich"))

    return rx.container(
        rx.hstack(
            rx.box(style=foto_style),  # Espacio para la foto
            rx.vstack(
                boton_milei,
                boton_masa,
                boton_bullrich
            )
        )
    )

