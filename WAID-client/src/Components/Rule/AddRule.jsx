import React, {Component} from 'react'
import ruleAxios from './ruleAxios'
import Input from '../Utils/Input'
import Select from '../Utils/Select'
import Button from "../Utils/Button";


export default class AddRule extends Component {
    constructor(props) {
        super(props);
        this.state = {
            rule: "",
            type: "",
            action: "",
            status: "",
            missingFields: false,
            ruleAdded: false
        }
    }

    handleChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    };

    handleAdd = async () => {
        this.setState({
            missingFields: false,
            ruleAdded: false
        });


        if (this.state.rule !== "" && this.state.type !== "" && this.state.action !== "") {
            let data = {
                rule: this.state.rule,
                type: this.state.type,
                action: this.state.action
            };
            try {
                await ruleAxios.post('addrule', data);
                this.setState({ruleAdded: true});
                this.props.handleAdd(data);
            } catch (error) {
                console.log('error on add rule', error);
            }
        } else
            this.setState({missingFields: true})

    };


    render() {
        const showHideFieldsMissing = this.state.missingFields ? "text-danger display-block" : "display-none";
        const ruleAdded = this.state.ruleAdded ? "text-success display-block bold" : "display-none";
        return (
            <div className='container'>
                <h1 className="text-center mb-3">Add New Rule</h1>
                <form className="container form-inline">
                    <Input
                        label="Rule"
                        type="text"
                        name="rule"
                        change={this.handleChange}
                    />
                    <Select
                        label="Type"
                        options={[
                            {key: "", value: ""},
                            {key: "0", value: "SQL Injection"},
                            {key: "1", value: "XSS"}
                        ]}
                        name="type"
                        defaultValue={this.state.type ? this.state.type : ""}
                        className="form-control"
                        onChange={this.handleChange}/>
                    <Select
                        label="Action"
                        options={[
                            {key: "", value: ""},
                            {key: "0", value: "Allow"},
                            {key: "1", value: "Blocked"}
                        ]}
                        name="action"
                        defaultValue={this.state.action ? this.state.action : ""}
                        className="form-control"
                        onChange={this.handleChange}/>
                    <p className={showHideFieldsMissing}>Please fill All Fields!</p>
                    <p className={ruleAdded}>User Added Successfully!</p>
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
