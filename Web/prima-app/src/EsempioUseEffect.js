import React, {useEffect, useState} from "react";

const EsempioUseEffect = () => {
    const [count, setCount] = useState(0);
  useEffect(() => {
    console.log("Ho chiamato useEffect");
    if(count<1){
        document.title="nessun titolo"
    }else{
          document.title="Ho trovato qualcosa"
    }
  });
  console.log("Sono fuori dallo useEffect");
  return (
    <>
      <div>EsempioUseEffect: {count}</div>
      <button onClick={() => setCount(count + 1)}>Incrementa</button>
    </>
  );
}

export default EsempioUseEffect