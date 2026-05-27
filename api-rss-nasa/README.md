-----------------------------------------------------------------------------------------------
# 🛰️ Projeto API de Notícias da NASA
 
Grupo: Carolina Perdigão, Caroline e Juan
Entrega da Avaliação das Sprints 2 e 3 - Programa de Bolsas Compass UOL / AWS - turma marco/2025
------------------------------------------------------------------

Este projeto tem como objetivo democratizar o acesso às notícias científicas da NASA, tornando-as mais acessíveis para públicos que não compreendem o inglês. A aplicação coleta e processa dados de um feed RSS oficial da NASA, armazenando as informações em um bucket Amazon S3. Cada notícia é tratada para extrair título, data, imagem e uma breve descrição.

Com o uso do Amazon Translate, a aplicação traduz automaticamente os textos principais para o português, permitindo que usuários de diferentes contextos tenham acesso facilitado a conteúdos científicos. Os dados são consumidos por uma interface web simples e responsiva, desenvolvida com foco na clareza da informação e na usabilidade.

Como próximo passo, o projeto prevê a tradução completa dos conteúdos vinculados às notícias, de forma a ampliar ainda mais seu potencial educativo.


###  📁 Estrutura de Pastas
```bash
├──  public/  # Arquivos estáticos (CSS, JS, imagens)
│  ├──  styles/  # Estilos da aplicação
│  │  ├──  main.css
│  │  └──  responsive.css
│  ├──  scripts/  # Scripts JS
│  │  └──  app.js
│  └──  index.html  # Página principal do front-end
├──  src/
│  ├──  config/  # Arquivos de configuração (ex: S3, variáveis de ambiente)
│  ├──  rss/  # Lógica da API de notícias
│  │  ├──  controller.js  # Controladores para manipulação das rotas
│  │  ├──  routes.js  # Rotas da API
│  │  ├──  service.js  # Funções para consumo do RSS e armazenamento no S3
├──  .gitignore  # Arquivos e pastas a serem ignorados pelo Git
├──  .env  # Variáveis de ambiente
├──  index.js  # Servidor da API
├──  package.json  # Dependências do projeto
└──  README.md  # Documentação do projeto

```

### 📦 Justificativa da Estrutura Modular

A  estrutura  do  projeto  foi  organizada  de  forma  modular,  com  base  em  funcionalidades.  Isso  significa  que  cada  feature (neste caso,  o  módulo  de  RSS) tem seu próprio conjunto de arquivos (`controller`,  `service`,  `routes`), isolando responsabilidades e facilitando a leitura, manutenção e escalabilidade do sistema.  

Essa  abordagem  é  recomendada  para  projetos  que  possam  evoluir,  pois  permite:

-  Separação  clara  de  responsabilidades
-  Melhor  reaproveitamento  de  código
-  Facilidade  na  adição  de  novas  funcionalidades


## Otimização 15/04/25

O JSON passou a ser armazenado no S3 tanto com o conteúdo original em inglês quanto o traduzido em português, no lugar de fazer traduções em tempo real na rota /noticia/:id.

- O que foi otimizado?
1. Evita chamadas desnecessárias à API da AWS Translate

Antes:
- Cada vez que alguém acessava /noticia/:id, o NodeJS fazia uma nova chamada para a AWS Translate, traduzindo novamente o mesmo título e descrição.
- Isso causa lentidão e consome mais créditos/custos da AWS.

Agora:
- A tradução é feita apenas uma vez, no momento do fetchRSS.
- Quando o front acessa /noticia/:id, ele só lê os dados já traduzidos, sem pedir à AWS Translate novamente.

Resultado: Menos latência, menos custo e mais controle.


## 🚀 Como Executar (auxílio para colaboradores)

Com o uso do Docker, rode na pasta raiz, através do terminal:

```
docker build -t nasa-rss-app -f docker/Dockerfile .
```

Em seguida, inicie o container.


### Pré-requisitos
...

### Instalação
...  

## 📡 Funcionalidades

- Busca de notícias atualizadas do feed RSS da NASA
- Processamento e armazenamento das notícias em JSON no S3
- Exibição das notícias via front-end com título, data, imagem e descrição

  

## 🌐 Tecnologias Utilizadas
- Node.js
- Express.js
- AWS SDK (S3)
- RSS Parser
- HTML/CSS/JS vanilla no front-end
 

## 🛡️ Boas Práticas
- Arquivos sensíveis como `.env` estão ignorados via `.gitignore`
- Projeto organizado por funcionalidade
- Uso de commits semânticos para versionamento claro das alterações