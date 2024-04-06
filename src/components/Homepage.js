import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import Sidebar from './Sidebar';

function Homepage() {
  const navigate = useNavigate(); 
  const [searchText, setSearchText] = useState('');
  const [CrawlerRecurse, setCrawlerRecurse] = useState(false);
  const [generatePDF, setGeneratePDF] = useState(true);
  const [FuzzerRecurse, setFuzzerRecurse] = useState(false);
  const [crawlerLimit, setCrawlerLimit] = useState(1000);

  const handleUrlChange = (e) => {
    setSearchText(e.target.value);
  };

  const handleScanClick = () => {
    console.log("Button clicked");
    console.log(searchText);
    postUrl(searchText);
  };

  const handleCrawlerRecurseChange = (e) => {
    setCrawlerRecurse(e.target.checked);
  };

  const handleCrawlerLimitChange = (e) => {
    setCrawlerLimit(e.target.value);
  };

  const postUrl = async (url) => {
    const response = await fetch('http://192.168.96.1:9090/scanner/scan_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        url: url,
        config: {
          limit: crawlerLimit,
          CrawlerRecurse: CrawlerRecurse,
          FuzzerRecurse : FuzzerRecurse,
          generatePDF: generatePDF,
          setSearchText: setSearchText,
        }
      })
    });
    
    
    const data = await response.json().then(()=>getReport())
    // getReport()

    
  }

  const getReport = async () => {
    const response = await fetch("http://192.168.96.1:9090/scanner/report");
    const html = await response.text();
    console.log(html)

    // Assuming you have a function renderHtml in report.js that takes HTML string as input
    navigate('/result', {
      state: {
        html: html,
        generatePDF,
        FuzzerRecurse,
        CrawlerRecurse,
      }
    });
  }

  const handleGeneratePDFChange = (e) => {
    setGeneratePDF(e.target.checked);
  }

  const handleFuzzerRecurseChange = (e) => {
    setFuzzerRecurse(e.target.checked);
  }

  return (
    <div class="grid-container">
      <Sidebar/>
      
    </div>
  );
}

export default Homepage;