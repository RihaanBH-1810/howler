import Sidebar from "./Sidebar";
import React, { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';

const Report = ({ url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt,setUrl,isReported, setIsReported,sentRequest,setSentRequest ,html,setHtml}) =>{
  const postUrl = async () => {
    const response = await fetch('http://localhost:8000/scanner/scan_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url ,
      config: {
        // rangeValue: rangeValue,
        // doRecurse: doRecurse,
        // selectValue: selectValue,
        // cookie: cookie,
        // workerInt: workerInt
      }}),
    });
    // const temp = await response;
    if(response.status === 200){
    getHtml();}
    
  }
  const getHtml = async () => {
    const response = await fetch('http://localhost:8000/scanner/report', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      
    });
    html = await response.text();
    console.log(html);
    setHtml(html);
   setIsReported(true);

    
  };
  useEffect(() => {
    if (sentRequest) {
      postUrl();
      setSentRequest(false);
    }
  });

  
  return (
    isReported ? (
    <div class="grid-container">
        <Sidebar/>
      <main class="report-container">
        <div class="report-title">
          <p class="font-weight-bold">DASHBOARD</p>
          <button onClick={getHtml}>Les go</button>
          <div class="report" dangerouslySetInnerHTML={{ __html: html }}>
          </div>
        </div>
      </main>

    </div>
      ) : (
        <div class="grid-container">
            <Sidebar/>
            <div class="main-loader">
            <div class="loader"></div>

            <p>Running Tool and Generating Report...</p>
              </div>
              
        </div>
        )
  );
}
export default Report;