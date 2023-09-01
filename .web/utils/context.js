import { createContext } from "react"
import { E } from "/utils/state.js"

export const initialState = {"bienvenido": "Bienvenidos a Debate ", "candidatoelegido": "", "input_titulo": "Bienvenidos a Juego Debate. Ingrese su nombre y haga click en comenzar.", "is_hydrated": false, "msj_footer": "Juego para practicar Python y Reflex", "nombre": "", "num_pregunta_actual": 0, "pregunta_actual": "", "preguntas": ["Pregunta 1: ¿Cuál es la capital de Francia?", "Pregunta 2: ¿Cuánto es 2 + 2?"], "principaltitulo": "Preparate para debatir ", "puntuacion": 0, "respuestas": {"Milei": [["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"], ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"]], "Masa": [["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"], ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"]], "Bullrich": [["Respuesta correcta 1", "Respuesta incorrecta 1", "Respuesta neutra 1"], ["Respuesta correcta 2", "Respuesta incorrecta 2", "Respuesta neutra 2"]]}, "seleccion": "", "year": 2023}
export const initialEvents = [E('state.hydrate', {})]
export const StateContext = createContext(null);
export const EventLoopContext = createContext(null);