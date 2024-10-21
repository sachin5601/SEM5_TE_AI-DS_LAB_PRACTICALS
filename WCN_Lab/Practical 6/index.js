const express = require('express');
const app = express();

// Define a route
app.get('/', (req, res) => {
    res.send('First express program');
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
