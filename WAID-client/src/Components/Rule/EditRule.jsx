import React, {Component} from 'react'
import Button from "../Utils/Button";
import Input from "../Utils/Input";
import Select from "../Utils/Select";

export default class EditRule extends Component {

    render() {
        const {rule, type, action} = this.props.rule;

        return (
            <>
                <div className={"container"}>
                    <div className={"modal-header"}>
                        <h5 className="modal-title">Edit Rule</h5>
                    </div>
                    <form onSubmit={this.props.update}>
                        <Input
                            label="Rule"
                            type="text"
                            name="rule"
                            value={rule ? rule : ''}
                            change={this.props.handleCurrentRule}
                        />
                        <Select
                            label="Type"
                            options={[
                                {key: "0", value: "SQL Injection"},
                                {key: "1", value: "XSS"}
                            ]}
                            name="type"
                            defaultValue={type ? type : "0"}
                            className="form-control"
                            onChange={this.props.handleCurrentRule}/>
                        <Select
                            label="Action"
                            options={[
                                {key: "0", value: "Allow"},
                                {key: "1", value: "Blocked"}
                            ]}
                            name="action"
                            defaultValue={action ? action : "0"}
                            className="form-control"
                            onChange={this.props.handleCurrentRule}/>
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




