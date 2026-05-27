const express = require("express");
const { traduzirHandler } = require("./controller");

const router = express.Router();

router.post("/", traduzirHandler);

module.exports = router;