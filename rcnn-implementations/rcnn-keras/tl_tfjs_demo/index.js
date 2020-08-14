var express = require("express");
var app = express();
const path = require("path");
const router = express.Router();

app.get("/", function(req, res) {
  res.sendFile(path.join(__dirname + "/home.html"));
});

app.use("/", router);
app.use(express.static("static"));
app.listen(process.env.port || 8081);
