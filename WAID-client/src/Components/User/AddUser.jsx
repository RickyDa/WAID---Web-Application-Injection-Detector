import React, {Component} from 'react'
import userAxios from './userAxios'
import Input from '../Utils/Input'
import Select from '../Utils/Select'
import Button from "../Utils/Button";

const passwordRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})");
const emailRegex = new RegExp(/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,15}/);
export default class AddUser extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            email: "",
            role: "",
            password: "",
            status: "",
            wrongEmailFormatMessage: false,
            wrongPasswordFormatMessage: false,
            missingFields: false,
            userAdded:false,
            duplicateEmail:false
        }
    }

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    };

    handleAdd = async () => {
        this.setState({
            wrongEmailFormatMessage: false,
            wrongPasswordFormatMessage: false,
            missingFields: false,
            userAdded:false,
            duplicateEmail:false
        });

        let isValid = true;

        if (this.state.username !== "" && this.state.email !== "" && this.state.password !== "" && this.state.role !== "") {
            if (!this.validateEmail()) {
                isValid = false;
                this.setState({wrongEmailFormatMessage: true})
            }
            if (!this.validatePassword()) {
                isValid = false;
                this.setState({wrongPasswordFormatMessage: true});
            }
            if (isValid) {
                let intRole = this.convertRoleToInt();
                let data = {
                    username: this.state.username,
                    password: this.state.password,
                    mail: this.state.email,
                    role: intRole
                };
                try {
                    await userAxios.post('adduser', data);
                    this.setState({userAdded:true});
                    this.props.handleAdd(data);
                } catch (error) {
                    if(error.response.status ===409)
                        this.setState({duplicateEmail:true});
                    console.log('error on add user', error);
                }
            }
        } else
            this.setState({missingFields: true})

    };

    validateEmail = () => {
        return emailRegex.test(this.state.email);
    };

    validatePassword = () => {
        return passwordRegex.test(this.state.password);
    };

    clearState = () => {
        this.setState({
            ...this.state,
            username: "",
            email: "",
            role: "",
            password: "",
            wrongEmailFormatMessage: false,
            wrongPasswordFormatMessage: false,
            missingFields: false,
            duplicateEmail:false
        });
    };

    convertRoleToInt = () => {
        let role = this.state.role;
        if (role === "admin")
            return 0;
        else
            return 1;
    };

    render() {
        const showHideEmailError = this.state.wrongEmailFormatMessage ? "text-danger display-block" : "display-none";
        const showHidePasswordError = this.state.wrongPasswordFormatMessage ? "text-danger display-block" : "display-none";
        const showHideFieldsMissing = this.state.missingFields ? "text-danger display-block" : "display-none";
        const userAdded = this.state.userAdded ? "text-success display-block bold" : "display-none";
        const duplicateEmail = this.state.duplicateEmail ? "text-danger display-block" : "display-none";
        return (
            <div className='container'>
                <h1 className="text-center mb-3">Add New User</h1>
                <form className="container form-inline">
                    <Input
                        label="Username"
                        type="username"
                        name="username"
                        change={this.handleChange}
                    />
                    <Input
                        label="Email"
                        type="email"
                        name="email"
                        change={this.handleChange}
                    />
                    <small className={showHideEmailError}>Email not in the right format</small>
                    <Input
                        label="Password"
                        type="password"
                        name="password"
                        change={this.handleChange}
                        tooltip={"For a valid password:\n" +
                        "\t*The password must contain at least 1 lowercase alphabetical character\n" +
                        "\t*The password must contain at least 1 uppercase alphabetical character\n" +
                        "\t*The password must contain at least 1 numeric character\n" +
                        "\t*The password must contain at least one special character\n" +
                        "\t*The password must be eight characters or longer"}
                    />
                    <small className={showHidePasswordError}>password not in the right format</small>
                    <Select
                        label="Role"
                        options={[
                            {key: "Empty", value: ""},
                            {key: "admin", value: "Admin"},
                            {key: "readonly",value: "Read Only"}
                            ]}
                        name="role"
                        defaultValue={this.state.role ? this.state.role : "empty"}
                        className="form-control rounded"
                        onChange={this.handleChange}/>
                    <p className={showHideFieldsMissing}>Please fill All Fields!</p>
                    <p className={duplicateEmail}>A User With this Email is already in the system!</p>
                    <p className={userAdded}>User Added Successfully!</p>
                    <Button
                        type={"button"}
                        onClick={this.handleAdd}
                        value={"Add"}
                        className={"btn btn-info btn-rounded btn-sm mr-2 ml-2 z-depth-0 my-4 waves-effect"}
                    />
                </form>
            </div>
        )
    }
}
