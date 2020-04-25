import React, {Component} from 'react'
import Button from "../Utils/Button";
import Input from "../Utils/Input";
import Select from "../Utils/Select";

export default class EditUser extends Component {

    render() {
        const {username, email, role} = this.props.user;
        return (
            <>
                <div className={"container"}>
                    <div className={"modal-header"}>
                        <h5 className="modal-title">Edit User</h5>
                    </div>
                    <form onSubmit={this.props.update}>
                        <Input
                            label="Username"
                            type="username"
                            name="username"
                            value={username ? username : ''}
                            change={this.props.handleCurrentUser}
                        />
                        <Input
                            label="Email"
                            type="email"
                            name="email"
                            value={email ? email : ''}
                            change={this.props.handleCurrentUser}
                        />
                        <Select
                            label="Role"
                            options={[
                                {key: "0", value: "Admin"},
                                {key: "1", value: "Read Only"}
                            ]}
                            name="role"
                            defaultValue={role ? role : "0"}
                            className="form-control"
                            onChange={this.props.handleCurrentUser}/>
                    </form>
                </div>
                <div className="modal-footer">
                    <Button
                        type={"button"}
                        value={"Close"}
                        className={"btn btn-secondary"}
                        onClick={this.props.handleClose}/>
                    <Button
                        type={"button"}
                        value={"Delete"}
                        className={"btn btn-danger"}
                        onClick={this.props.delete}/>
                    <Button
                        type={"button"}
                        value={"Update"}
                        className={"btn btn-primary"}
                        onClick={this.props.update}/>
                </div>
            </>
        );
    }
}




