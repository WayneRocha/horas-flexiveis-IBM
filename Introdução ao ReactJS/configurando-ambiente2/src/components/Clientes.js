function clientes(props) {
    const renderClients = ({id, nome}) => {
        return (
            <ul type="square">
                <li key={`client-${id}`}>cliente {id}</li>
                <li key={`client-${id}`}>nome {nome}</li>
            </ul>
        );
    }
    
    return (
        props.clientes.map(renderClients)
    );
}

export default clientes;