const express = require("express");
const { handleGetNoticias } = require("./controller");

const router = express.Router();

router.get("/noticias", handleGetNoticias);

module.exports = router;