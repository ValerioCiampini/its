const rootElement = document.querySelector("#root")

const root = ReactDOM.createRoot(rootElement)

const App = (props) => {
    return(
        <main className="main" id="main">
            <h1>Primo componente</h1>
            {props.children}
        </main>
    )
}

const List = () => {
    return(
        <ul>
            <li>Php</li>
            <li>Js</li>
            <li>Java</li>
        </ul>
    )
}

root.render(
    <>
    <App>
        <h2>Lista Competenze
            
        </h2>
    </App>
    <List></List>
    </>
)