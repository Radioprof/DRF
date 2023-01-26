import React from 'react';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from "./components/Project.js";
import TodoList from "./components/Todo.js";
import axios from 'axios';
// import project from "./components/Project";
import {BrowserRouter, Route, Link, Switch, Redirect} from "react-router-dom";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': ProjectList,
            'todo': TodoList
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
        // axios.get('http://127.0.0.1:8000/api/projects')
        //     .then(response => {
        //         const projects = response.data
        //         this.setState(
        //             {
        //                 'projects': projects
        //             }
        //         )
        //     }).catch(error => console.log(error))
        //  axios.get('http://127.0.0.1:8000/api/todo')
        //     .then(response => {
        //         const todolist = response.data
        //         this.setState(
        //             {
        //                 'todo': todolist
        //             }
        //         )
        //     }).catch(error => console.log(error))


    }
    render() {
        return (
            <div className="App">
                <BrowserRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                         <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                         <li>
                            <Link to='/todo'>ToDo</Link>
                        </li>
                    </ul>
                </nav>
                    <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                    {/*<Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />*/}
                    {/*<Route exact path='/todo' component={() => <TodoList todolist={this.state.todolist} />} />*/}

                </BrowserRouter>
            </div>
        )
    }
}
export default App;
