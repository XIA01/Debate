import { createContext } from "react"
import { E } from "/utils/state.js"

export const initialState = {"bienvenido": "Bienvenidos a Debate ", "input_titulo": "Bienvenidos a Juego Debate. Ingrese su nombre y haga click en comenzar.", "is_hydrated": false, "msj_footer": "Juego para practicar Python y Reflex", "nombre": "", "principaltitulo": "Preparate para debatir ", "seleccion": "", "year": 2023}
export const initialEvents = [E('state.hydrate', {})]
export const StateContext = createContext(null);
export const EventLoopContext = createContext(null);