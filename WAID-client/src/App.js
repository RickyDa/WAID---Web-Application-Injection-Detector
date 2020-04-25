import React, {Component} from "react";
import Users from "./Components/User/Users";
import Rules from "./Components/Rule/Rules";
import Navbar from "./Components/Navbar";
import Login from "./Components/Login/Login";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Settings from "./Components/Settings/Settings";
import "./App.css";
import Demo from "./Components/Demo/Demo";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLogin: false,
            user: ""
        };

    }

    handleLogin = (data) => {
        console.log("LOGIN!")
        this.setState({isLogin: true, user: data});
    };
    handleLogOut = () => {
        console.log("LOGOUT!")
        console.log(this.state);
        this.setState({isLogin: false, user: ""});
    };

    render() {
        return (
            <Router>
                <div className="App">
                    <header className="App-header">
                        <Navbar logout={this.handleLogOut}/>
                    </header>
                    <div className="App-body">
                        <Switch>
                            <Route path="/demo">
                                <Demo />
                            </Route>
                            <Route path="/rules">
                                <Rules state={this.state}/>
                            </Route>
                            <Route path="/users">
                                <Users state={this.state}/>
                            </Route>
                            <Route path="/control-panel">
                                <Settings state={this.state}/>
                            </Route>
                            <Route path="/">
                                <Login handleLogin={this.handleLogin}/>
                            </Route>
                        </Switch>
                    </div>
                </div>
            </Router>
        );
    }
}

export default App;
