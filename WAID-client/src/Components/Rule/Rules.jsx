import React, {Component} from 'react'
import Rule from './Rule'
import AddRule from './AddRule'
import ruleAxios from "./ruleAxios";
import Modal from '../Modal/Modal'
import EditRule from "./EditRule";
import {Redirect} from "react-router-dom";
import axios from "axios";
import './Rules.css';
class Rules extends Component {

    constructor(props) {
        super(props);
        this.state = {
            rulesLists: [],
            show: false,
            currentRule: {},
            lastAddedRule: {}
        };

    }

    CancelToken = axios.CancelToken;
    source = this.CancelToken.source();

    componentDidMount = async () => {
        try {
            const {data} = await ruleAxios.get(`/getall`, {
                cancelToken: this.source.token
            });
            this.setState({rulesLists: data})
        } catch (error) {
            console.log('error on getting rule list', error);
        }
    };

    componentWillUnmount() {
        this.source.cancel("Operation canceled by the user.");
    }

    showModal = () => {
        this.setState({show: true});
    };

    hideModal = () => {
        this.setState({show: false, currentRule: {}}, ()=> this.updateTable());
    };

    createTable = (rule) => {
        return (<Rule
            key={rule.id}
            id={rule.id}
            rule={rule.rule}
            type={rule.type}
            action={rule.action}
            edit={this.handleEdit}/>)
    };

    handleEdit = (rule) => {
        this.setState({currentRule: rule});
        this.showModal()
    };

    handleAdd = (data) => {
        this.setState({lastAddedRule: data},()=> this.updateTable());
    };

    updateTable = async () => {
        try {
            const {data} = await ruleAxios.get(`/getall`);
            this.setState({rulesLists: data})
        } catch (error) {
            console.log('error on update table', error);
        }
    };
    handleDelete = async () => {
        try {
            const {status} = await ruleAxios.delete(`/delete/${this.state.currentRule.id}`);
            if (status) {
                this.hideModal()
            } else {
                this.setState({status: 500});
            }
        } catch (error) {
            console.log('error on delete', error);
        }
    };

    handleCurrentRule = (e) => {
        this.setState({
            currentRule: {
                ...this.state.currentRule,
                [e.target.name]: e.target.value
            }
        });
    };

    handleUpdate = async (e) => {
        e.preventDefault();
        try {
            const {status} = await ruleAxios.put(`/update/${this.state.currentRule.id}`, this.state.currentRule);
            if (status) {
                this.hideModal()
            } else {
                this.setState({status: 500});
            }
        } catch (error) {
            console.log('error on delete', error);
        }
    };

    render() {
        if (!this.props.state.isLogin) {
            return <Redirect to={'./'}/>
        }
        return (
            <div>
                <AddRule handleAdd={this.handleAdd}/>
                <table className="container table table-striped table-dark mt-5">
                    <thead className="thead-dark">
                    <tr>
                        <th>Id</th>
                        <th>Rule</th>
                        <th>Type</th>
                        <th>Action</th>
                        <th>Edit</th>
                    </tr>
                    </thead>
                    {this.state.rulesLists && <tbody>{this.state.rulesLists.map(rule => this.createTable(rule))}</tbody>}
                </table>
                <Modal show={this.state.show} handleClose={this.hideModal}>
                    <EditRule handleClose={this.hideModal} handleCurrentRule={this.handleCurrentRule}
                              rule={this.state.currentRule} delete={this.handleDelete} update={this.handleUpdate}/>
                </Modal>
            </div>
        )
    }
}

export default Rules