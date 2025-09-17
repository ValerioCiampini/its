const CardUtente = (props) => {
    console.log(props)
    return(
        <div>
            <h2>{props.name}</h2>
            <p>{props.email}</p>
            <img src={props.imgUrl} alt="Avatar Utente"></img>
        </div>
    );
}

export default CardUtente;