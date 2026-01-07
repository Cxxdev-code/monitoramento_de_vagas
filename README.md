# 🚀 Monitor de Vagas 99Freelas para Discord

Este projeto é uma ferramenta de automação robusta desenvolvida em Python para monitorar oportunidades de trabalho na plataforma **99Freelas**. [cite_start]Ele captura novas vagas em tempo real, gerencia a persistência de dados para evitar duplicidade e envia notificações ricas (Embeds) para um servidor no Discord[cite: 2].

## ✨ Funcionalidades

- **Web Scraping Inteligente**: Captura dados dinâmicos utilizando Selenium em modo `headless` com bloqueio de imagens para otimização de banda e CPU.
- **Fila de Mensagens (Queue)**: Implementação de `collections.deque` para garantir que as notificações sejam entregues de forma ordenada e respeitando os limites da API do Discord[cite: 2].
- **Arquitetura Multithread**: O bot do Discord e o motor de monitoramento rodam simultaneamente, garantindo que o sistema nunca pare.
- **Persistência em Banco de Dados**: Utiliza SQLite para registrar projetos já enviados, garantindo que o usuário não receba notificações repetidas.
- **Embeds Customizados**: Notificações formatadas com título, link, categoria, nível de experiência e descrição resumida[cite: 2].

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.x**
- **Selenium**: Automação de navegador.
- **BeautifulSoup4**: Extração e parse de dados HTML.
- **Discord.py**: Integração com a API do Discord[cite: 2].
- **SQLite3**: Armazenamento local leve.
- **Python-dotenv**: Gerenciamento de variáveis de ambiente seguras[cite: 2].

## 📂 Estrutura do Projeto

```text
├── data/               # Arquivos de banco de dados (.db)
├── src/                # Código fonte organizado por módulos
│   ├── bot/            # Lógica de conexão e envio para o Discord
│   ├── core/           # Orquestrador do loop de monitoramento
│   ├── database/       # Scripts de criação e manipulação do banco
│   └── scrapers/       # Motores de busca (Selenium) e Parser (BS4)
├── .env                # Variáveis sensíveis (Tokens e IDs)
├── .gitignore          # Proteção de arquivos privados
├── main.py             # Arquivo principal de inicialização
└── requirements.txt    # Lista de dependências do sistema
```

**Como Configurar e Rodar**
1. Clonar o Repositório
Bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

**Configurar Variáveis de Ambiente**
Crie um arquivo .env na raiz do projeto conforme o exemplo abaixo:

Snippet de código

DISCORD_TOKEN=seu_token_aqui
DISCORD_CHANNEL_ID=id_do_canal_aqui

**Instalar Dependências**
Bash

pip install -r requirements.txt

**Executar**
Bash

python main.py
