import React from 'react';
import './TableOption.css'

const TableOption = ({subject, text}) => {

    return (
        <>
            <h4>{subject}</h4>
            <small>{text}</small>
        </>
    );
};

export default TableOption;

