import Sidebar from './Sidebar';
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
const Download = ({ url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt ,isReported, setIsReported}) => {

  
    return (
        
        <div class="grid-container">
          <Sidebar/>
            <div class="ag-format-container">
            <div class="ag-courses_box">
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