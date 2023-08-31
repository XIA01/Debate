import reflex as rx
from debate2.state import *

def titulo():
    return rx.container(
        rx.hstack(
            rx.text(State.principaltitulo+" "+State.nombre, color_scheme="twitter"),
        )
    )
    