import React, {Component} from 'react';
import Button from '../Utils/Button'


class User extends Component {
    handleEdit = () => {
        const {edit} = this.props;
        edit(this.props)

    };

    replaceIntToStr = (roleId) => {
        if (roleId === 1)
            return "Read Only";
        else
            return "Admin";
    };

    render() {
        const {id, username, email, role} = this.props;
        let roleStr = this.replaceIntToStr(role);

        return (
            <tr>
                <td>{id}</td>
                <td>{username}</td>
                <td>{email}</td>
                <td>{roleStr}</td>
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


export default User;