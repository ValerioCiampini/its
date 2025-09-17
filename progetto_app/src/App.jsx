import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import CardUtente from './CardUtente'
import Termostato from './termostato'

function App(){

  return (
    <div>
      <CardUtente name="VAlerio" email="c" imgUrl=""></CardUtente>
      <Termostato></Termostato>
    </div>
  )
}

export default App
