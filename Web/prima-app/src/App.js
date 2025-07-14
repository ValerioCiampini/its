import { useState } from 'react';
import './App.css';
//import Clock from './Clock';
//import Componente1 from './Componente1';
import {anagrafica} from "./data/dati";
import Contatore from './Contatore';
import EsempioUseEffect from './EsempioUseEffect';
import CleanUp from './CleanUp';
import Clock from './Clock';

/*function getDate(date)
{
  return date.toLocaleDateString() + " " + date.toLocaleTimeString();
}*/

function App() {

  let nome = "Valerio";

  const [nome1, setNome1] = useState(nome);

  const [persone, setPersone] =  useState(anagrafica);

  const cambiaNome = () => {
    console.log(nome);
    nome = "Mario";
    setNome1(nome);
    console.log(nome)
  }

  const elimina = (id) => {
    const newAnag = persone.filter(p => p.id !== id);
    setPersone(newAnag)
  }

  const [persona, setPersona] = useState({
    id:"1",
    nome:"Val", 
    cognome:"Ciamp",
    eta:20
  })

  const compleanno = () => {
    let anni = persona.eta + 1;

    setPersona({
      ...persona,
      eta:anni
    })
  }
  const cliccami = (nome, cognome) => {
    alert("Ciao" + nome + " " + cognome);
  }

  return(
    <div className='App'>
       <Clock timezone = "1" country = "Italy"></Clock>
        <Clock timezone = "-6" country = "USA"></Clock>
         <Clock timezone = "8" country = "Japan"></Clock>
      <CleanUp></CleanUp>
      <Contatore></Contatore>
      <EsempioUseEffect></EsempioUseEffect>
      <h1>{nome1}</h1>
      <button onClick={cambiaNome} className='btn btn-primary'>
        Cambia nome
      </button>
<br></br>
<br></br>
<div>{persona.nome}</div>
<div>{persona.cognome}</div>
<div>{persona.eta}</div>
<button onClick={compleanno} className='btn btn-primary'>
  Compleanno
</button>
      
      {
        persone.map((p) => {
          return (
          <div key = {p.id}>
            <span>
              {p.nome} {p.cognome}
            </span>
            &nbsp;&nbsp;
            <button onClick={() => {
              elimina(p.id);
            }}>
            ELimina
            </button>
            </div>)
        })
      }
    </div>
  );
}

export default App;
