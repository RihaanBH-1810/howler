import Sidebar from "./Sidebar";
import React, { useRef } from 'react';
import { useLocation } from 'react-router-dom';

const Report = ({ url, rangeValue, doRecurse, selectValue, cookie, workerInt, setRangeValue, setDoRecurse, setSelectValue, setCookie, setWorkerInt,setUrl,isReported, setIsReported }) =>{
  

  
  return (
    isReported ? (
    <div class="grid-container">
        <Sidebar/>
      <main class="main-container">
        <div class="main-title">
          <p class="font-weight-bold">DASHBOARD</p>
        </div>

        <div class="main-cards">

          <div class="card">
            <div class="card-inner">
              <p class="text-primary">PRODUCTS</p>
              <span class="material-icons-outlined text-blue">inventory_2</span>
            </div>
            <span class="text-primary font-weight-bold">249</span>
          </div>

          <div class="card">
            <div class="card-inner">
              <p class="text-primary">PURCHASE ORDERS</p>
              <span class="material-icons-outlined text-orange">add_shopping_cart</span>
            </div>
            <span class="text-primary font-weight-bold">83</span>
          </div>

          <div class="card">
            <div class="card-inner">
              <p class="text-primary">SALES ORDERS</p>
              <span class="material-icons-outlined text-green">shopping_cart</span>
            </div>
            <span class="text-primary font-weight-bold">79</span>
          </div>

          <div class="card">
            <div class="card-inner">
              <p class="text-primary">INVENTORY ALERTS</p>
              <span class="material-icons-outlined text-red">notification_important</span>
            </div>
            <span class="text-primary font-weight-bold">56</span>
          </div>

        </div>

        <div class="charts">

          <div class="charts-card">
            <p class="chart-title">Top 5 Products</p>
            <div id="bar-chart"></div>
          </div>

          <div class="charts-card">
            <p class="chart-title">Purchase and Sales Orders</p>
            <div id="area-chart"></div>
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