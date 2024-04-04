const express = require('express');
const app = express();
const port = 3000; // Choose any available port

// Middleware to parse JSON request bodies
app.use(express.json());

// API endpoint to handle POST requests
app.post('/api/progress', (req, res) => {
  // Access the request data from req.body
  const requestData = req.body;

  // Process the request data as needed
  console.log('Received data:', requestData);

  // Send a response back to the client
  res.json({ message: 'Data received successfully' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});