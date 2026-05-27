const { fetchRSS } = require("./service");

async function handleGetNoticias(req, res) {
  console.log("🛰️  Rota /noticias foi chamada");
  try {
    const noticias = await fetchRSS();
    res.json(noticias);
  } catch (error) {
    console.error("❌ Erro ao buscar notícias:", error);
    res.status(500).json({ error: "Erro ao buscar notícias" });
  }
}

module.exports = { handleGetNoticias };