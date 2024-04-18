const express = require('express');
const { spawn } = require('child_process');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Handle root URLd
app.get('/', (req,d= res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/app', (req, res) => {  
  let largeDataSet = [];
  // spawn new child process to call the python script
  const python = spawn('python', ['script2.py', JSON.stringify(req.query)]); // Pass arguments to the Python script

  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    largeDataSet.push(data);
  });

  // in close event we are sure that stream is from child process is closed
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(largeDataSet.join(''));
  });
});


app.listen(port, () => {
  console.log(`App listening on port ${port}!`);
});
