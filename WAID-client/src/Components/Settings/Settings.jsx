import React, {Component} from 'react'
import confAxios from "./confAxios";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faToggleOn, faToggleOff} from '@fortawesome/free-solid-svg-icons'
import './settings.css'
import Select from "../Utils/Select";
import Input from "../Utils/Input";
import Button from "../Utils/Button";
import {Redirect} from "react-router-dom";
import TableOption from "./TableOption";
import https from 'https';

const agent = new https.Agent({
    rejectUnauthorized: false
});

class Settings extends Component {
    _isMounted = false;

    constructor(props) {
        super(props);
        this.state = {
            isActive: '',
            isClient: '',
            serverIP: '',
            siteAddress: '',
            isAnalyzer: '',
            isClassifier: ''
        };

    }


    componentWillUnmount() {
        this._isMounted = false;
    }

    componentDidMount = async () => {
        this._isMounted = true;
        try {
            const {data} = await confAxios.get(`/get_all`, {
                headers: {
                    'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                    'Content-Type': 'application/json'
                },
                httpsAgent: agent
            });
            if (this._isMounted) {
                this.setState({
                    isActive: data["is_active"] === 'True',
                    isClient: data["is_client"] === 'True',
                    serverIP: data["server_ip"],
                    siteAddress: data['site_address'],
                    isAnalyzer: data["is_analyzer"] === 'True',
                    isClassifier: data["is_classifier"] === 'True',

                });
            }

        } catch (error) {
            console.log('error on getting is active', error);
        }

    };


    handleGetConfig = async () => {
        try {
            const {data} = await confAxios.get(`/get_all`, {
                headers: {
                    'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                    'Content-Type': 'application/json'
                },
                httpsAgent: agent
            });
            this.setState({
                isActive: data["is_active"] === 'True',
                isClient: data["is_client"] === 'True',
                serverIP: data["server_ip"],
                siteAddress: data['site_address'],
                isAnalyzer: data["is_analyzer"] === 'True',
                isClassifier: data["is_classifier"] === 'True',
            })
        } catch (error) {
            console.log('error on updating state', error);
        }
    };


    handleInput = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    };

    handleServeClient = (e) => {
        let value = e.target.value === '1';
        this.setState({
            [e.target.name]: value
        }, async () => {
            let newValue = (this.state.isClient).toString();
            let data = {is_client: newValue.replace(/^\w/, c => c.toUpperCase())}
            try {
                const {status} = await confAxios.post('/set_is_client', data, {
                    headers: {
                        'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                        'Content-Type': 'application/json'
                    },
                    httpsAgent: agent
                });
                if (status === 200)
                    this.handleGetConfig()
            } catch (error) {
                console.log('error on setting is client', error);
            }
        })
    };

    handleIsActive = () => {
        let value = !this.state.isActive;
        this.setState({
            isActive: value
        }, async () => {
            let newValue = (this.state.isActive).toString();
            let data = {is_active: newValue.replace(/^\w/, c => c.toUpperCase())};
            try {
                const {status} = await confAxios.post('/set_is_active', data, {
                    headers: {
                        'Authorization': 'Bearer ' + JSON.parse(sessionStorage.getItem('user'))['access_token'],
                    },
                    httpsAgent: agent
                });
                if (status === 200)
                    this.handleGetConfig()
            } catch (error) {
                console.log('error on setting is client', error);
            }
        })
    };
    handleIsClassifier = () => {
        let value = !this.state.isClassifier;
        this.setState({
                isClassifier: value
            }, async () => {
                let newValue = (this.state.isClassifier).toString();
                let data = {is_classifier: newValue.replace(/^\w/, c => c.toUpperCase())};
                try {
                    const {status} = await confAxios.post('/set_is_classifier', data,
                        {
                            headers: {
                                'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                                'Content-Type': 'application/json'
                            },
                            httpsAgent: agent
                        });
                    if (status === 200)
                        this.handleGetConfig()
                } catch (error) {
                    console.log('error on setting is classifier', error);
                }
            }
        )
    }
    ;

    handleIsAnalyzer = () => {
        let value = !this.state.isAnalyzer;
        this.setState({
            isAnalyzer: value
        }, async () => {
            let newValue = (this.state.isAnalyzer).toString();
            let data = {is_analyzer: newValue.replace(/^\w/, c => c.toUpperCase())};
            try {
                const {status} = await confAxios.post('/set_is_analyzer', data,
                    {
                        headers: {
                            'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`
                        },
                        httpsAgent: agent
                    });
                if (status === 200)
                    this.handleGetConfig()
            } catch (error) {
                console.log('error on setting is analyzer', error);
            }
        })
    };


    handleServerUrlSend = async () => {
        try {
            let data = {server_ip: this.state.serverUrl};
            const {status} = await confAxios.post('/set_server_ip', data,
                {
                    headers: {
                        'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                    },
                    httpsAgent: agent
                });
            if (status === 200)
                this.handleGetConfig()
        } catch (error) {
            console.log('error on setting is active', error);
        }
    };

    handleSiteAddress = async () => {
        try {
            let data = {site_address: this.state.siteAddress};
            const {status} = await confAxios.post('/set_site_address', data,
                {
                    headers: {
                        'Authorization': `Bearer ${JSON.parse(sessionStorage.getItem('user'))['access_token']}`,
                    },
                    httpsAgent: agent
                });
            if (status === 200)
                this.handleGetConfig()
        } catch (error) {
            console.log('error on setting is active', error);
        }
    };

    render() {

        if (!sessionStorage.getItem('user')) {
            return <Redirect to={'./'}/>
        }

        const showServerUrl = !this.state.isClient;
        const isActiveIcon = this.state.isActive ? faToggleOn : faToggleOff;
        const isClassifierIcon = this.state.isClassifier ? faToggleOn : faToggleOff;
        const isAnalyzerIcon = this.state.isAnalyzer ? faToggleOn : faToggleOff;
        return (
            <div>
                <div className="text-center">
                    <h1>WAID - Web Application Intrusion Detector</h1>
                </div>
                <table className="container table text-left table-striped table-dark mt-5">
                    <thead className="thead-dark">
                    <tr>
                        <th>Option</th>
                        <th>Choice</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td><TableOption subject={"WAID Functionality"}
                                         text={"Here you can set WAID to be ON or OFF"}/>
                        </td>
                        <td id={'fontawesome'}>
                            <FontAwesomeIcon size={'2x'} icon={isActiveIcon}
                                             onClick={this.handleIsActive}/>
                        </td>
                    </tr>
                    {
                        this.state.isActive &&
                        <tr>
                            <td>
                                <TableOption subject={"Site Address"}
                                             text={"Here you put the address for the site that WAID will protect "}/>
                            </td>
                            <td>
                                <Input
                                    label={""}
                                    type={"text"}
                                    name={"siteAddress"}
                                    value={this.state.siteAddress}
                                    tooltip={"Enter site address here"}
                                    change={this.handleInput}
                                />
                                <Button
                                    type={"button"}
                                    onClick={this.handleSiteAddress}
                                    value={"Update"}
                                    className={"btn btn-danger btn-rounded z-depth-0 my-4 waves-effect"}
                                />
                            </td>
                        </tr>
                    }
                    {
                        this.state.isActive &&
                        <tr>
                            <td>
                                <TableOption subject={"Server or Client"}
                                             text={"Here you can set if you are in Client mode or Server mode"}/>
                            </td>
                            <td>
                                <Select
                                    label=""
                                    options={[
                                        {key: "0", value: "Server"},
                                        {key: "1", value: "Client"}
                                    ]}
                                    name="isClient"
                                    defaultValue={this.state.isClient ? 1 : 0}
                                    className="custom-select custom-select-sm"
                                    onChange={this.handleServeClient}/>
                            </td>
                        </tr>
                    }
                    {
                        this.state.isActive &&
                        !this.state.isClient &&
                        <tr>
                            <td>
                                <TableOption subject={"Classifier"}
                                             text={"Here you can decide if WAID will use the Classifier"}/>
                            </td>
                            <td id={'fontawesome'}>
                                <FontAwesomeIcon size={'2x'} icon={isClassifierIcon}
                                                 onClick={this.handleIsClassifier}/>
                            </td>
                        </tr>
                    }
                    {
                        this.state.isActive &&
                        !this.state.isClient &&
                        <tr>
                            <td>
                                <TableOption subject={"Analyzer"}
                                             text={"Here you can decide if WAID will use the Analyzer"}/>
                            </td>
                            <td id={'fontawesome'}>
                                <FontAwesomeIcon size={'2x'} icon={isAnalyzerIcon}
                                                 onClick={this.handleIsAnalyzer}/>
                            </td>
                        </tr>
                    }
                    {
                        this.state.isActive &&
                        this.state.isClient &&
                        <tr>
                            <td>
                                <TableOption subject={"Server Address"}
                                             text={"Put here the IP of the server"}/>
                            </td>
                            <td>
                                <Input
                                    label={""}
                                    type={"text"}
                                    name={"serverUrl"}
                                    value={this.state.serverUrl}
                                    tooltip={"Enter server address here"}
                                    change={this.handleInput}
                                    disabled={showServerUrl}
                                />
                                <Button
                                    type={"button"}
                                    onClick={this.handleServerUrlSend}
                                    value={"Update"}
                                    className={"btn btn-danger btn-rounded z-depth-0 my-4 waves-effect"}
                                />
                            </td>
                        </tr>
                    }
                    </tbody>
                </table>
            </div>
        )
    }
}

export default Settings