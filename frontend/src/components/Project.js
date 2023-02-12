import React from 'react'

const ProjectItem = ({ item, deleteProject }) => {
    return (
        <tr>
            <td>
                {item.name}
            </td>
            <td>
                {item.user}
            </td>
            <td>
                <button onClick={()=>deleteProject(item.name)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({ items, deleteProject }) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                User
            </th>
            <th></th>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList