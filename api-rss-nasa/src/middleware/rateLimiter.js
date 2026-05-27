const rateLimit = require("express-rate-limit");
const express = require("express");

const limiter = rateLimit({
  windowMs: 1 * 60 * 1000, // 1min
  max: 30, // max 10 requisições por ip/min
  message: "🚫 Você está enviando muitas requisições. Tente novamente em alguns minutos."
});

module.exports = limiter;