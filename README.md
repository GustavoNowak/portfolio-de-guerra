# Rick and Morty ETL: Coleta e Processamento de Dados

Este projeto demonstra a construção de um pipeline de **ETL (Extract, Transform, Load)** em Python para interagir com a [API pública de Rick and Morty](https://rickandmortyapi.com/). O script principal extrai dados de personagens de múltiplas páginas, processa as informações e as carrega em um arquivo CSV estruturado.

O repositório também está configurado com ferramentas de qualidade de código e boas práticas de desenvolvimento, utilizando **Husky**, **Commitlint** e **Lint-Staged** para automatizar a verificação de padrões de commits e formatação de código antes que as alterações sejam enviadas ao repositório.

## ✨ Funcionalidades

- **Extração (Extract):** O script navega automaticamente através do sistema de paginação da API para coletar informações de um número definido de páginas.
- **Transformação (Transform):** Extrai e limpa campos específicos de cada personagem, como nome, status, espécie e local de origem.
- **Carregamento (Load):** Salva os dados transformados de forma organizada em um arquivo `characters.csv`.
- **Qualidade de Código Automatizada:**
  - **Husky:** Gerencia os hooks do Git para acionar scripts automaticamente.
  - **Commitlint:** Garante que todas as mensagens de commit sigam o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
  - **Lint-Staged** (implícito pelo uso de Husky e Commitlint): Para rodar linters em arquivos preparados para commit.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas Python:**
  - `requests`: Para realizar requisições HTTP à API.
  - `pandas`: Para manipulação e armazenamento dos dados em formato de DataFrame e CSV.
- **Ferramentas de Desenvolvimento:**
  - [Git](https://git-scm.com/): Sistema de controle de versão.
  - [Node.js](https://nodejs.org/en) e [npm](https://www.npmjs.com/): Para gerenciar as ferramentas de qualidade de código.
  - [Husky](https://typicode.github.io/husky/): Automação de hooks do Git.
  - [Commitlint](https://commitlint.js.org/#/): Análise de mensagens de commit.

## 🚀 Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/GustavoNowak/rickmorty-etl.git](https://github.com/GustavoNowak/rickmorty-etl.git)
    ```
2.  **Acesse o diretório do projeto:**
    ```bash
    cd rickmorty-etl
    ```
3.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Instale as dependências Python:**
    ```bash
    pip install pandas requests
    ```
    *(Ou `pip install -r requirements.txt` se um arquivo for criado)*

5.  **Instale as dependências de desenvolvimento (Node.js):**
    Este passo é necessário para usar as ferramentas de qualidade de código como Husky.
    ```bash
    npm install
    ```

## 🏃 Como Usar

Para executar o pipeline de ETL e gerar o arquivo CSV, execute o seguinte comando no terminal:

```bash
python api_client.py