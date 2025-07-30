import React, {useEffect, useState} from "react";

const FetchComponent = () => {
    const url = "https://jsonplaceholder.typicode.com/users";
    const [users, setUsers] = useState([]);

    const getUser = async () => {
        const response = await fetch(url);
        const result = await response.json();
        setUsers(result);
    }

    useEffect(() => {
        /*fetch(url)
            .then(res => res.json())
            .then((ris) => setUsers(ris));*/
        getUser()
    },[]);

    return(
        <>
        <h1>Fetch user from jsonplaceholder</h1>
        <div>
            {
                users.map((u) => {
                    return <p key={u.id}>{u.name}</p>
                })}
        </div>
        </>
    );
};

export default FetchComponent;