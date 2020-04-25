import React, {Component} from 'react';
import Button from '../Utils/Button'


const ACTION = {
    0: "Allow",
    1: "Blocked"
};

const TYPE = {
    0: "SQL Injection",
    1: "XSS"
};

class Rule extends Component {
    handleEdit = () => {
        const {edit} = this.props;
        edit(this.props)

    };

    render() {
        const {id, rule, type, action} = this.props;
        let actionName = ACTION[action];
        let typeName = TYPE[type];
        return (
            <tr>
                <td>{id}</td>
                <td>{rule}</td>
                <td>{typeName}</td>
                <td>{actionName}</td>
                <td>
                    <Button
                        type={"button"}
                        value={"Edit"}
                        className={"btn btn-primary btn-rounded"}
                        dataToggle={"modal"}
                        dataTarget={"#staticBackdrop"}
                        onClick={this.handleEdit}/>
                </td>
            </tr>
        );
    }
}


export default Rule;