import React, { useRef } from 'react';
import { useLocation } from 'react-router-dom';
import { pdf } from '@react-pdf/renderer';
import PdfRenderer from './PDFRenderer.js';

function Result() {
  const location = useLocation();
  const { html, generatePDF, FuzzerRecurse, CrawlerRecursel,setHTML} = location.state;
  const htmlRef = useRef(null);

  const handleDownloadPDF = async () => {
    const blob = await pdf(<PdfRenderer html={html} />).toBlob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'report.pdf';
    link.click();
    setHTML(html);
  };

  return (
    <div className="bg-dark text-white min-vh-100 d-flex flex-column justify-content-center align-items-center">
      <div
        ref={htmlRef}
        dangerouslySetInnerHTML={{ __html: html }}
        className="bg-white text-black p-4"
      />
      <button
        className="btn btn-warning mt-3"
        onClick={handleDownloadPDF}
      >
        Download PDF
      </button>
      <div style={{ height: '100px', backgroundColor: 'black' }}></div>
    </div>
  );
}


export default Result;
