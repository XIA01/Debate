import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { E, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Container, Input, Link, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
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
  <VStack>
  <Text onClick={_e => Event([E("state.pasaryear", {})], _e)} sx={{"display": "flex", "justify-content": "center", "align-items": "center", "height": "10vh", "fontSize": "2em", "textAlign": "center"}}>
  {`${state.bienvenido} ${state.year} Señor: ${state.nombre}`}
</Text>
  <Box>
  <Text>
  {state.input_titulo}
</Text>
  <Input onBlur={_e => Event([E("state.cambiarnombre", {nombre:_e.target.value})], _e)} placeholder={`Nombre...`} type={`text`}/>
  <Link as={NextLink} href={`/princ`}>
  <Button colorScheme={`twitter`} size={`md`}>
  {`Comenzar`}
</Button>
</Link>
  <Text>
  {state.msj_footer}
</Text>
</Box>
</VStack>
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
