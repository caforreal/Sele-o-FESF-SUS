const express = require("express");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

app.set("trust proxy", 1);
app.use(express.json());
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

const rssRoutes = require("./src/rss/routes");
app.use("/", rssRoutes);

const rateLimiter = require("./src/middleware/rateLimiter");
const speedLimiter = require("./src/middleware/speedLimiter");
app.use("/traduzir", rateLimiter, speedLimiter);

const translateRoutes = require("./src/translate/routes");
app.use("/traduzir", translateRoutes);

app.listen(PORT, () => console.log(`🚀 Servidor rodando na porta ${PORT}`));
