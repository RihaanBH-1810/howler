import Sidebar from './Sidebar';
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
const Config = ({ url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt,setUrl }) =>{
   
    const navigate = useNavigate();


    const MAXRange = 10000; 
    const getBackgroundSize = () => { 
    return { backgroundSize: `${(rangeValue * 100) / MAXRange}% 100%` }; }; 
    
    const options = [
        "1","2","3"
    ];
    const onOptionChangeHandler = (event) => {
        setSelectValue(event.target.value);
    };
    const handleRangeChange = (e) => {
        setRangeValue(e.target.value);
    }
    const handleRecurseChange = (e) => {
        setDoRecurse(e.target.checked);
    }
    const handleCookieChange = (e) => {
        setCookie(e.target.value);
    }
    const handleWorkerChange = (e) => {
        setWorkerInt(e.target.value);
    }
    const handleSaveClick = () => {
        setCookie(cookie);
        setRangeValue(rangeValue);
        setSelectValue(selectValue);
        setDoRecurse(doRecurse);
        setWorkerInt(workerInt);
        navigate('/', {
            
          });
    }


  return (
    <div class="grid-container">
      <Sidebar/>
      <div class = "setting-box">
        <h1>SETTING</h1>
        <div class="setting-item">
          <p>Does the fuzzer need to recurse?</p>
          <input class = "recurse-checkbox" type="checkbox" checked = {doRecurse} onChange={handleRecurseChange}/>
        </div>
        <div class="setting-item">
          <p>What should be the fuzzers depth?</p>
          <select class = "fuzz-option" onChange={onOptionChangeHandler} value={selectValue}>
                {options.map((option, index) => {
                    return (
                        <option key={index}>
                            {option}
                        </option>
                    );
                })}
            </select>
        </div>
        <div class="setting-item">
          <p>What should be the crawlers limit?</p><p class="gr">{rangeValue}</p>
          
        </div>
        <input class="range-slider"
            type="range" 
            min="0" 
            value={rangeValue}
            max={MAXRange} 
            onChange={handleRangeChange} 
            style={getBackgroundSize()} 
            />
        <div class="setting-sec">
          <p>Enter session Cookies:</p>
          <textarea rows="2" cols="40" value = {cookie} placeholder='eg: key1=value1;key2=value2;' onChange={handleCookieChange}></textarea>
        </div>
        <div class = "setting-item">
            <p>Enter the number of worker:</p>
            <input class="number" type="number" max = "8" min = "1" value={workerInt} onChange={handleWorkerChange}/>
        </div>
        <button class="setting-button" onClick={handleSaveClick}>SAVE</button>

      </div>
    </div>
  );
}
export default Config;