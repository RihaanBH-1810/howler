import './index.css';
import React, { useState } from 'react';
import {
  Route,
  Routes,
  BrowserRouter
} from "react-router-dom";
import MainDashboard from './components/MainDashboard';
import Report from './components/Report.js';
import Config from './components/Config.js';
import Download from './components/Download.js';
// Create the function
export function AddLibrary(urlOfTheLibrary) {
  const script = document.createElement("script");
  script.src = urlOfTheLibrary;
  script.async = true;
  document.body.appendChild(script);
}
function App() {

  const [cookie, setCookie] = useState('');
  const [rangeValue, setRangeValue] = useState(0);
  const [selectValue, setSelectValue] = useState('1');
  const [doRecurse , setDoRecurse] = useState(false);
  const [workerInt, setWorkerInt] = useState(1);
  const [url, setUrl] = useState('');
  const [responseHtml, setResponseHtml] = useState('');
  const [isReported, setIsReported] = useState(false);
  const [sentRequest, setSentRequest] = useState(false);
  const [html, setHtml] = useState('');

  
  return (
    <div className="Main">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<MainDashboard 
            url={url}
            rangeValue={rangeValue}
            doRecurse={doRecurse}
            selectValue={selectValue}
            cookie={cookie}
            workerInt={workerInt}
            setRangeValue={setRangeValue}
            setDoRecurse={setDoRecurse}
            setSelectValue={setSelectValue}
            setCookie={setCookie}
            setWorkerInt={setWorkerInt}
            setUrl={setUrl}
            setSentRequest={setSentRequest}
            sentRequest={sentRequest}

            />} />
            <Route path="/report" element={<Report 
            url={url}
            rangeValue={rangeValue}
            doRecurse={doRecurse}
            selectValue={selectValue}
            cookie={cookie}
            workerInt={workerInt}
            setRangeValue={setRangeValue}
            setDoRecurse={setDoRecurse}
            setSelectValue={setSelectValue}
            setCookie={setCookie}
            setWorkerInt={setWorkerInt}
            setUrl={setUrl}
            isReported={isReported}
            setIsReported={setIsReported}
            responseHtml={responseHtml}
            setResponseHtml={setResponseHtml}
            sentRequest={sentRequest}
            setSentRequest={setSentRequest}
            html={html}
            setHtml={setHtml}
            />} />
            <Route path="/setting" element={<Config 
            url={url}
            rangeValue={rangeValue}
            doRecurse={doRecurse}
            selectValue={selectValue}
            cookie={cookie}
            workerInt={workerInt}
            setRangeValue={setRangeValue}
            setDoRecurse={setDoRecurse}
            setSelectValue={setSelectValue}
            setCookie={setCookie}
            setWorkerInt={setWorkerInt}
            setUrl={setUrl}
            />} />
            <Route path="/download" element={<Download 
            url={url}
            rangeValue={rangeValue}
            doRecurse={doRecurse}
            selectValue={selectValue}
            cookie={cookie}
            workerInt={workerInt}
            setRangeValue={setRangeValue}
            setDoRecurse={setDoRecurse}
            setSelectValue={setSelectValue}
            setCookie={setCookie}
            setWorkerInt={setWorkerInt}
            setUrl={setUrl}
            isReported={isReported}
            setIsReported={setIsReported}
            html={html}
            setHtml={setHtml}

/>} />
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
