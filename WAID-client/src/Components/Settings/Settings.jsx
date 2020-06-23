import React, { Component } from "react";
import { confAxios } from "../ApiAxios/Axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faToggleOn, faToggleOff } from "@fortawesome/free-solid-svg-icons";
import "./settings.css";
import Select from "../Utils/Select";
import Input from "../Utils/Input";
import Button from "../Utils/Button";
import { Redirect } from "react-router-dom";
import TableOption from "./TableOption";
import https from "https";

const agent = new https.Agent({
  rejectUnauthorized: false,
});

class Settings extends Component {
  _isMounted = false;

  constructor(props) {
    super(props);
    this.state = {
      is_active: "",
      is_client: "",
      server_ip: "",
      site_address: "",
      is_analyzer: "",
      is_classifier: "",
      aws_access_key_id: "",
      aws_secret_access_key: "",
      mail: "",
      mail_password: "",
    };
  }

  componentWillUnmount() {
    this._isMounted = false;
  }

  componentDidMount = async () => {
    this._isMounted = true;
    try {
      const { data } = await confAxios.get(`/get_all`, {
        headers: {
          Authorization: `Bearer ${
            JSON.parse(sessionStorage.getItem("user"))["access_token"]
          }`,
          "Content-Type": "application/json",
        },
        httpsAgent: agent,
      });

      if (this._isMounted) {
        this.setState({
          is_active: data["is_active"] === "True",
          is_client: data["is_client"] === "True",
          server_ip: data["server_ip"],
          site_address: data["site_address"],
          is_analyzer: data["is_analyzer"] === "True",
          is_classifier: data["is_classifier"] === "True",
          aws_access_key_id: data["aws_access_key_id"],
          aws_secret_access_key: data["aws_secret_access_key"],
          mail: data["mail"],
          mail_password: data["mail_password"],
        });
      }
    } catch (error) {
      console.log("error on getting is active", error);
    }
  };

  handleGetConfig = async () => {
    try {
      const { data } = await confAxios.get(`/get_all`, {
        headers: {
          Authorization: `Bearer ${
            JSON.parse(sessionStorage.getItem("user"))["access_token"]
          }`,
          "Content-Type": "application/json",
        },
        httpsAgent: agent,
      });
      this.setState(
        {
          is_active: data["is_active"] === "True",
          is_client: data["is_client"] === "True",
          server_ip: data["server_ip"],
          site_address: data["site_address"],
          is_analyzer: data["is_analyzer"] === "True",
          is_classifier: data["is_classifier"] === "True",
          aws_access_key_id: data["aws_access_key_id"],
          aws_secret_access_key: data["aws_secret_access_key"],
          mail: data["mail"],
          mail_password: data["mail_password"],
        });
    } catch (error) {
      console.log("error on updating state", error);
    }
  };

  handleInput = (e) => {
    this.setState(
      {
        [e.target.name]: e.target.value,
      });
  };

  handleServeClient = (e) => {
    let value = e.target.value === "1";
    this.setState({ [e.target.name]: value });
  };

  handleIsActive = () => {
    let value = !this.state.is_active;
    this.setState({ is_active: value });
  };

  handleIsClassifier = () => {
    let value = !this.state.is_classifier;
    this.setState({ is_classifier: value });
  };

  handleIsAnalyzer = () => {
    let value = !this.state.is_analyzer;
    this.setState({ is_analyzer: value });
  };

   handleUpdateConf = async () => {
    try {
      let stateToServer = this.convertStateToServer();
      const { status } = await confAxios.post("/setall", stateToServer, {
        headers: {
          Authorization: `Bearer ${
            JSON.parse(sessionStorage.getItem("user"))["access_token"]
          }`,
        },
        httpsAgent: agent,
      });
      if (status === 200) this.handleGetConfig();
    } catch (error) {
      console.log("error on setting is active", error);
    }
  };

  convertStateToServer = () => {
    let boolList = ["is_active", "is_client", "is_analyzer", "is_classifier"];
    let toServer = {};

    for (let key in this.state) {
      if (key in boolList) {
        let value = this.state[key].toString();
        toServer[key] = value.replace(/^\w/, (c) => c.toUpperCase());
      } else {
        toServer[key] = this.state[key];
      }
    }
    return toServer;
  };

  render() {
    if (!sessionStorage.getItem("user")) {
      return <Redirect to={"./"} />;
    }

    const showServerUrl = !this.state.is_client;
    const is_activeIcon = this.state.is_active ? faToggleOn : faToggleOff;
    const is_classifierIcon = this.state.is_classifier ? faToggleOn : faToggleOff;
    const is_analyzerIcon = this.state.is_analyzer ? faToggleOn : faToggleOff;
    return (
      <div>
        <div className="text-center">
          <h1>WAID - Web Application Intrusion Detector</h1>
        </div>
        <div className={"container"}>
          <Button
            type={"button"}
            onClick={this.handleUpdateConf}
            value={"Update"}
            className={"btn btn-danger btn-rounded d-block update-btn mt-3"}
          />
          <table className=" table text-left table-striped table-dark mt-3 mb-3 conf-table">
            <thead className="thead-dark">
              <tr>
                <th>Option</th>
                <th>Choice</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <TableOption
                    subject={"WAID Functionality"}
                    text={"Here you can set WAID to be ON or OFF"}
                  />
                </td>
                <td id={"fontawesome"}>
                  <FontAwesomeIcon
                    size={"2x"}
                    icon={is_activeIcon}
                    onClick={this.handleIsActive}
                  />
                </td>
              </tr>
              {this.state.is_active ? (
                <tr>
                  <td>
                    <TableOption
                      subject={"Site Address"}
                      text={
                        "Here you put the address for the site that WAID will protect"
                      }
                    />
                  </td>
                  <td>
                    <Input
                      label={"Site Address"}
                      type={"text"}
                      name={"site_address"}
                      value={this.state.site_address}
                      tooltip={"Enter site address here"}
                      change={this.handleInput}
                    />
                  </td>
                </tr>
              ) : null}
              {this.state.is_active ? (
                <tr>
                  <td>
                    <TableOption
                      subject={"Server or Client"}
                      text={
                        "Here you can set if you are in Client mode or Server mode"
                      }
                    />
                  </td>
                  <td>
                    <Select
                      label="Server/Client"
                      options={[
                        { key: "0", value: "Server" },
                        { key: "1", value: "Client" },
                      ]}
                      name="is_client"
                      defaultValue={this.state.is_client ? 1 : 0}
                      className="custom-select custom-select-sm"
                      onChange={this.handleServeClient}
                    />
                  </td>
                </tr>
              ) : null}
              {this.state.is_active && !this.state.is_client ? (
                <tr>
                  <td>
                    <TableOption
                      subject={"Classifier"}
                      text={
                        "Here you can decide if WAID will use the Classifier"
                      }
                    />
                  </td>
                  <td id={"fontawesome"}>
                    <FontAwesomeIcon
                      size={"2x"}
                      icon={is_classifierIcon}
                      onClick={this.handleIsClassifier}
                    />
                  </td>
                </tr>
              ) : null}
              {this.state.is_active && !this.state.is_client ? (
                <tr>
                  <td>
                    <TableOption
                      subject={"Analyzer"}
                      text={"Here you can decide if WAID will use the Analyzer"}
                    />
                  </td>
                  <td id={"fontawesome"}>
                    <FontAwesomeIcon
                      size={"2x"}
                      icon={is_analyzerIcon}
                      onClick={this.handleIsAnalyzer}
                    />
                  </td>
                </tr>
              ) : null}
              {this.state.is_active && this.state.is_client ? (
                <tr>
                  <td>
                    <TableOption
                      subject={"Server Address"}
                      text={"Put here the IP of the server"}
                    />
                  </td>
                  <td>
                    <Input
                      label={""}
                      type={"text"}
                      name={"server_ip"}
                      value={this.state.server_ip}
                      tooltip={"Enter server address here"}
                      change={this.handleInput}
                      disabled={showServerUrl}
                    />
                  </td>
                </tr>
              ) : null}
              <tr>
                <td>
                  <TableOption
                    subject={"Mail"}
                    text={
                      "Here you put the mail address and Mail password for sending the emails"
                    }
                  />
                </td>
                <td>
                  <Input
                    label={"Mail"}
                    type={"text"}
                    name={"mail"}
                    value={this.state.mail}
                    tooltip={"Enter Mail Address here"}
                    change={this.handleInput}
                  />
                  <Input
                    label={"Mail Password"}
                    type={"password"}
                    name={"mail_password"}
                    value={this.state.mail_password}
                    tooltip={"Enter Mail Password"}
                    change={this.handleInput}
                  />
                </td>
              </tr>
              <tr>
                <td>
                  <TableOption
                    subject={"AWS"}
                    text={
                      "put here the AWS Access Key Id & AWS Secret Access Key for the DB back up"
                    }
                  />
                </td>
                <td>
                  <Input
                    label={"AWS Access Key Id"}
                    type={"password"}
                    name={"aws_access_key_id"}
                    value={this.state.aws_access_key_id}
                    tooltip={"Enter AWS Access Key Id"}
                    change={this.handleInput}
                  />
                  <Input
                    label={"AWS Secret Access Key"}
                    type={"password"}
                    name={"aws_secret_access_key"}
                    value={this.state.aws_secret_access_key}
                    tooltip={"Enter AWS Secret Access Key"}
                    change={this.handleInput}
                  />
                </td>
              </tr>
            </tbody>
          </table>
          <Button
            type={"button"}
            onClick={this.handleUpdateConf}
            value={"Update"}
            className={"btn btn-danger btn-rounded d-block mb-5 update-btn"}
          />
        </div>
      </div>
    );
  }
}

export default Settings;
