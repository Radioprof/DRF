import React from 'react'

const TodoItem = ({ item, deleteTodo }) => {
    return (
        <tr>
            <td>
                {item.name}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.create}
            </td>
            <td>
                {item.update}
            </td>
            <td>
                <button onClick={()=>deleteTodo(item.name)} type='button'>Delete</button>
            </td>

        </tr>
    )
}

const TodoList = ({ items, deleteTodo }) => {
    return (
        <table>
            <th>
                Name Project
            </th>
            <th>
                Text
            </th>
            <th>
                Create
            </th>
            <th>
                Update
            </th>
            <th></th>

            {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo}/>)}
        </table>
    )
}
export default TodoList