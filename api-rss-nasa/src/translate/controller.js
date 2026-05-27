const { traduzirTexto } = require("./service");

async function traduzirHandler(req, res) {
  const { texto, from = "en", to = "pt" } = req.body;

  if (!texto) {
    return res.status(400).json({ erro: "Texto é obrigatório para tradução." });
  }

  try {
    const traduzido = await traduzirTexto(texto, from, to);
    res.json({ traduzido });
  } catch (error) {
    res.status(500).json({ erro: "Erro ao traduzir texto." });
  }
}

module.exports = { traduzirHandler };