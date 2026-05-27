const slowDown = require("express-slow-down");

const speedLimiter = slowDown({
  windowMs: 60 * 1000,
  delayAfter: 5,
  delayMs: () => 500
});

module.exports = speedLimiter;