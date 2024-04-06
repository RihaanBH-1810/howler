// import '../App.css';
import CottageOutlinedIcon from '@mui/icons-material/CottageOutlined';
import ArticleIcon from '@mui/icons-material/Article';
import DownloadIcon from '@mui/icons-material/Download';
import SettingsIcon from '@mui/icons-material/Settings';
import { useNavigate } from 'react-router-dom';
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import Sidebar from './Sidebar';
const MainDashboard = ({url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt,setUrl, sentRequest, setSentRequest}
) =>{
  const navigate = useNavigate();

  const handleScan = () => {
    if(url === ''){
      console.log("Please enter a URL");
    } else {
    setSentRequest(true);
    setUrl(url);
    console.log("Scanning...")
    console.log(JSON.stringify({ url ,
      config: {
        rangeValue: rangeValue,
        doRecurse: doRecurse,
        selectValue: selectValue,
        cookie: cookie,
        workerInt: workerInt
      }}))
    navigate('/report');}
  }
  const handleConfig = () => {
    setUrl(url);
    console.log("Configuring...")
    navigate('/setting');
  }
  const handleUrl = (e) => {
    setUrl(e.target.value);
  }
  

  return (
    <div class="grid-container">
      <Sidebar/>
      <main class="main-container">
        <div class="main-title">
          <h1>HOWLER </h1>
          <p>Discovers vulnerabilities that are yet unidentified by humanity.</p>
          <p>Out of the world Technology with MultiProcessing...</p>
        </div>
        <div class="main-input">
          <input type="text" placeholder="Search for something..." value={url} onChange={handleUrl}/>
          <button onClick = {handleScan} >SCAN</button>
        </div>
        <div class="main-config">
          <div class="config-thing" onClick={handleConfig}>
            <SettingsIcon/>
            </div>
            <div class = "config-item">
            <p>Configure Settings here.</p>
            </div>
        </div>
      </main>
    </div>
      
  );
}
export default MainDashboard;