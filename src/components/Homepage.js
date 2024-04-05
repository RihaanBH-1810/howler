import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

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
    const response = await fetch('http://127.0.0.1:8000/scanner/scan_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        url: url,
        config: {
          // limit: crawlerLimit,
          // CrawlerRecurse: CrawlerRecurse,
          // FuzzerRecurse : FuzzerRecurse,
          // generatePDF: generatePDF,
        }
      })
    });
    
    
    const data = await response.json().then(()=>getReport())
    // getReport()

    
  }

  const getReport = async () => {
    const response = await fetch("http://127.0.0.1:8000/scanner/report");
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
    <div className="bg-dark text-white min-vh-100 d-flex justify-content-center align-items-center">
      <div className="me-5">
        <h1 className="mb-5 display-1">Auto Web Pentesting Tool</h1>
        <div className="mb-5">
          <h4 className="mb-4">Enter the URL</h4>
          <input
            type="text"
            className="form-control bg-secondary text-white fs-3 px-3 py-2"
            onChange={handleUrlChange}
            placeholder="https://example.com"
          />
        </div>
        <button className="btn btn-warning btn-lg px-5 py-3" onClick={handleScanClick}>
          Scan
        </button>
      </div>
      <div className="bg-dark border border-light rounded p-4">
        <h4 className="mb-4">Configure</h4>
        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className={`form-check-input ${FuzzerRecurse ? 'bg-orange border-orange' : ''}`}
            id="FuzzerRecurseCheckbox"
            checked={FuzzerRecurse}
            onChange={handleFuzzerRecurseChange}
          />
          <label className="form-check-label" htmlFor="FuzzerRecurseCheckbox">
            Generate HTML
          </label>
        </div>
        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className={`form-check-input ${generatePDF ? 'bg-orange border-orange' : ''}`}
            id="generatePDFCheckbox"
            checked={generatePDF}
            onChange={handleGeneratePDFChange}
          />
          <label className="form-check-label" htmlFor="generatePDFCheckbox">
            Generate PDF
          </label>
        </div>
        <div className="mb-3">
          <label htmlFor="crawlerLimitInput" className="form-label">
            Limit for Crawler
          </label>
          <input
            type="number"
            className="form-control bg-secondary text-white"
            id="crawlerLimitInput"
            value={crawlerLimit}
            onChange={handleCrawlerLimitChange}
          />
        </div>
        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className={`form-check-input ${CrawlerRecurse ? 'bg-orange border-orange' : ''}`}
            id="CrawlerRecurseCheckbox"
            checked={CrawlerRecurse}
            onChange={handleCrawlerRecurseChange}
          />
          <label className="form-check-label" htmlFor="CrawlerRecurseCheckbox">
            Do Recurse
          </label>
        </div>
      </div>
    </div>
  );
}

export default Homepage;