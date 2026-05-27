const { TranslateClient, TranslateTextCommand } = require("@aws-sdk/client-translate");

const translateClient = new TranslateClient({ region: "us-east-1" });

async function traduzirTexto(texto, sourceLang = "en", targetLang = "pt") {
  const params = {
    Text: texto,
    SourceLanguageCode: sourceLang,
    TargetLanguageCode: targetLang,
  };

  try {
    const command = new TranslateTextCommand(params);
    const response = await translateClient.send(command);
    return response.TranslatedText;
  } catch (error) {
    console.error("Erro ao traduzir texto:", error.message);
    return texto;
  }
}

module.exports = { traduzirTexto };