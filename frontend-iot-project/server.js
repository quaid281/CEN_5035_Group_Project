const express = require("express");
const bodyParser = require("body-parser");

const path = __dirname + '/app/views/';

const app = express();

app.use(express.static(path));

// parse requests of content-type - application/json
app.use(bodyParser.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req,res) {
  res.sendFile(path + "index.html");
});

require("./app/routes/datasetimages.routes")(app);
app.all('/*', function(req, res, next) {
    res.sendFile(path + "index.html");
});
// set port, listen for requests
const PORT = 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
