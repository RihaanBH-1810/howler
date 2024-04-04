import './App.css';
import React from 'react';
import {
  Route,
  Routes,
  BrowserRouter
} from "react-router-dom";
import Homepage from './components/Homepage';
import Result from './components/Result';

function App() {
  return (
    <div className="Main">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Homepage />} />
            <Route path="/result" element={<Result />} />
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
