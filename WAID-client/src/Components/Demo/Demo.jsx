import React, {Component} from 'react';
import Button from "../Utils/Button";
import demoAxios from "./demoAxios";

class Demo extends Component {
    constructor(props) {
        super(props);
        this.state = {
            attack: ""
        };
    }

    handleClick = async () => {
        try {
            let response = demoAxios.get("/?" + this.state.attack);
            console.log("demo response", response);
        } catch (error) {
            console.log('error on demo', error);
        }
    };

    inputChange = ({target: {name, value}}) => {
        this.setState({
            [name]: value,
        });
    };

    render() {
        return (
            <div className={"container"}>
                <h1>Try to attack WAID</h1>
                <input
                    type="text"
                    placeholder={"'DELETE FROM *'"}
                    name={"attack"}
                    onChange={this.inputChange}
                />
                <Button
                    type={"button"}
                    onClick={this.handleClick}
                    value={"Update"}
                    className={"btn btn-info btn-rounded btn-block z-depth-0 my-4 waves-effect"}
                />
            </div>
        );
    }
}

export default Demo;