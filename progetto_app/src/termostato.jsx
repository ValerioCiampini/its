import React, { useState } from 'react'

const Termostato = () => {

    const [temp, setTemp] = useState(0);

    return (
        <div>
            <h1>{temp}</h1>
            <button onClick={() => setTemp(temp + 1)}>incrementa</button>
            <button onClick={() => setTemp(temp - 1)}>decrementa</button>
        </div>
    )
}

export default Termostato