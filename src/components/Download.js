import Sidebar from './Sidebar';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
const Download = ({ url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt ,isReported, setIsReported,html,setHtml}) => {
    const navigate = useNavigate();
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
        navigate("/report")
        
        
      };
  
    return (
        
        <div class="grid-container">
          <Sidebar/>
            <div class="ag-format-container">
            <div class="ag-courses_box">
                <div class="ag-courses_item">
                <a onClick={getHtml} class="ag-courses-item_link">
                    <div class="ag-courses-item_bg"></div>

                    <div class="ag-courses-item_title">
                    For Comprehensive Report in PDF<br></br> form click here to download
                    </div>

                </a>
                </div>

                <div class="ag-courses_item">
                <a href="#" class="ag-courses-item_link">
                    <div class="ag-courses-item_bg"></div>

                    <div class="ag-courses-item_title">
                    For Comprehensive Report in PDF<br></br> form click here to download
                    </div>
                </a>
                </div>

                <div class="ag-courses_item">
                <a href="#" class="ag-courses-item_link">
                    <div class="ag-courses-item_bg"></div>

                    <div class="ag-courses-item_title">
                    For Comprehensive Report in PDF<br></br> form click here to download
                    </div>

                </a>
                </div>


            </div>
            </div>


        </div>
      
      );
}
export default Download;