const Parser = require("rss-parser");
const { PutObjectCommand } = require("@aws-sdk/client-s3");
const { TranslateClient, TranslateTextCommand } = require("@aws-sdk/client-translate");
const s3Client = require("../config/s3Client");

const parser = new Parser();
const translateClient = new TranslateClient({ region: "us-east-1" });

async function traduzirTexto(texto, from = "en", to = "pt") {
  try {
    const comando = new TranslateTextCommand({
      Text: texto,
      SourceLanguageCode: from,
      TargetLanguageCode: to,
    });
    const resposta = await translateClient.send(comando);
    return resposta.TranslatedText;
  } catch (err) {
    console.error("Erro ao traduzir:", err.message);
    return texto;
  }
}

async function fetchRSS() {
  const feed = await parser.parseURL("https://www.nasa.gov/rss/dyn/breaking_news.rss");

  const artigosComTitulo = feed.items.filter(item => item.title && item.title.trim() !== "");

  const artigosTraduzidos = await Promise.all(artigosComTitulo.map(async item => {
    const imageMatch = item["content:encoded"] ? item["content:encoded"].match(/<img[^>]+src="([^">]+)"/) : null;
    const image = imageMatch ? imageMatch[1] : null;

    const rawDescription = item.description
      ? item.description.replace(/<[^>]+>/g, '').substring(0, 150)
      : item["content:encoded"]
        ? item["content:encoded"].replace(/<[^>]+>/g, '').substring(0, 150)
        : "Sem descrição disponível";

    const [titlePt, descPt] = await Promise.all([
      traduzirTexto(item.title),
      traduzirTexto(rawDescription)
    ]);

    return {
      title: titlePt,
      title_eng: item.title,
      link: item.link,
      date: item.pubDate,
      description: descPt + "...",
      description_eng: rawDescription,
      image: image,
    };
  }));

  const params = {
    Bucket: process.env.S3_BUCKET_NAME,
    Key: "nasa-news.json",
    Body: JSON.stringify(artigosTraduzidos),
    ContentType: "application/json",
  };

  await s3Client.send(new PutObjectCommand(params));
  return artigosTraduzidos;
}

module.exports = { fetchRSS };
