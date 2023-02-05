import React from 'react'

const TodoItem = ({ todo }) => {
    return (
        <tr>
            <td>
                {todo.name}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.create}
            </td>
            <td>
                {todo.update}
            </td>

        </tr>
    )
}

const TodoList = ({ todolist }) => {
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

            {todolist.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}
export default TodoList