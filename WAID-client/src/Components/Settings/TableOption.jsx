import React from 'react';
import './TableOption.css'
import {faAngleRight} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

const TableOption = ({subject, text}) => {

    return (
        <>
            <h4>{subject}</h4>
            <FontAwesomeIcon id={"FontAwesomeIcon"} size={'1x'} icon={faAngleRight}/><small>{text}</small>
        </>
    );
};

export default TableOption;

