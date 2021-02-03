const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const passport = require("passport");
const path = require("path");
const cors = require('cors')

const users = require("./routes/api/users");

const app = express();

app.use(
    bodyParser.urlencoded({
      extended: false
    })
  );

app.use(bodyParser.json());

app.use(
  cors({
    origin: "http://localhost:3000",
  })
);

const dbURL =  "mongodb://localhost:27017/unique";

mongoose
    .connect(process.env.MONGODB_URI || dbURL,
    { useUnifiedTopology:true, useNewUrlParser: true }
    )
    .then(() => console.log("MongoDB successfully connected"))
    .catch(err => console.log(err));

app.use(passport.initialize());

require("./config/passport")(passport);

app.use("/api/users", users);

const port = process.env.PORT || 5000;

app.listen(port,()=>console.log(`Server up and running on port ${port}`));