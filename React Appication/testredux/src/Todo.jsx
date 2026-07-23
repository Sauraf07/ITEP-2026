function ToDo(){
    let {Todos} = useSelector((store)=>store.Todos)
    return <>
        <h1>ToDO component</h1>
        <table>
            <tr>
                <td>ID</td>
                <td>TODO</td>
                <td>Completed</td>
                <td>User ID</td>
            </tr>
        </table>

    </>

}
export default ToDo