import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';

/*function getDate(date)
{
  return date.toLocaleDateString() + " " + date.toLocaleTimeString();
}*/

function App() {

  let nome = "Valerio"
  return(
    <div className='App'>
      <h1>Primo Elemento {nome}</h1>
      <Componente1>Valerio</Componente1>
      <Componente1/>
      <h2>
        {
        new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()
        }
      </h2>
      <Clock timezone = "0" country = "Italy"></Clock>
      <Clock timezone = "8" country = "Japan"></Clock>
    </div>
  );
}

export default App;
