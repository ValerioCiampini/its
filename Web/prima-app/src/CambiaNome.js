import React, {useState} from "react";

const CambiaNome = () => {
    const [nome, setNome] = useState("Valerio");
    const cambia = () => {
        if (nome === "Valerio"){
            setNome("Mario");
        }
        else{
            setNome("Valerio");
        }
    };

    return(
        <div>
            <h3>{nome}</h3>
            <button className="btn btn-dark" onClick={cambia}>
                Cambia Nome
            </button>
        </div>
    );
};

export default CambiaNome;