document.addEventListener("DOMContentLoaded", () => {
  fetch("/noticias")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("news-list");
      data.forEach((article, index) => {
        const li = document.createElement("li");
      
        li.innerHTML = `
          <div class="post-card" style="animation-delay: ${index * 100}ms">
            <div class="avatar"></div>
            <a href="${article.link}" class="title" target="_blank">${article.title}</a>
            <span class="datetime">${new Date(article.date).toLocaleDateString("pt-BR")}</span>
            ${article.image ? `<img src="${article.image}" alt="Imagem da notícia" class="image-preview"/>` : ""}
            <p>${article.description.substring(0, 150)}...</p>
          </div>
        `;
        list.appendChild(li);
      });
    })
    .catch(err => {
      console.error("Erro ao carregar notícias:", err);
    });
});