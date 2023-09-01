import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { E, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Container, HStack, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"


export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [Event, notConnected] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
  <Fragment><Fragment>
  <Container>
  <Container>
  <VStack>
  <Text>
  {state.pregunta_actual}
</Text>
  <HStack>
  <Button colorScheme={`twitter`} onClick={_e => Event([E("state.respondio", {respuesta:"Bien"})], _e)}>
  {`Bien`}
</Button>
  <Button colorScheme={`twitter`} onClick={_e => Event([E("state.respondio", {respuesta:"Mal"})], _e)}>
  {`Mal`}
</Button>
  <Button colorScheme={`twitter`} onClick={_e => Event([E("state.respondio", {respuesta:"Nulo"})], _e)}>
  {`Nulo`}
</Button>
</HStack>
</VStack>
</Container>
  <Text>
  {`Puntuacion: ${state.puntuacion}`}
</Text>
</Container>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
    </Fragment>
  )
}
