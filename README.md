# 📘 Activity Provider -- Inven!RA

### 🧩 Jogo Sopa de Letras

### UC: Arquitetura e Padrões de Software (APSI) -- MEIW -- UAb/UTAD

### Autor: **Weber Marcelo Guirra de Souza**

## 📌 Objetivo do Projeto

Este projeto implementa um **Activity Provider** integrado à plataforma
**Inven!RA**, simulando a atividade educacional **"Jogo Sopa de
Letras"**.

A implementação faz parte da unidade curricular **Arquitetura e Padrões
de Software (APSI)**, aplicando:

-   Arquitetura orientada a serviços\
-   Padrões de criação\
-   Web services RESTful\
-   Integração com plataforma educativa

------------------------------------------------------------------------

## 🛠 Tecnologias Utilizadas

-   Python 3.x\
-   FastAPI\
-   Uvicorn\
-   Render.com\
-   Git + GitHub

------------------------------------------------------------------------

## 📡 Endpoints REST

  Método   Endpoint                 Descrição
  -------- ------------------------ ----------------------------------
  GET      `/config`                Configuração básica da atividade
  GET      `/params`                Parâmetros configuráveis
  POST     `/deploy`                Criação de instância do jogo
  GET      `/analytics/available`   Tipos de analytics
  GET      `/analytics`             Dados de analytics

Swagger UI disponível em `/docs`.

------------------------------------------------------------------------

## 📂 Estrutura

    activity_provider_invenra/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## ▶️ Como Executar

### Ambiente virtual

Windows:

    python -m venv venv
    venv\Scripts\activate

Linux/Mac:

    python3 -m venv venv
    source venv/bin/activate

### Instalar dependências

    pip install -r requirements.txt

### Rodar servidor

    uvicorn main:app --reload

------------------------------------------------------------------------

## 🌐 Deploy Render

Build:

    pip install -r requirements.txt

Start:

    uvicorn main:app --host 0.0.0.0 --port $PORT

------------------------------------------------------------------------

## 🏆 Estado Atual

-   [x] Arquitetura definida\
-   [x] Endpoints implementados\
-   [x] Teste local concluído\
-   [ ] Deploy Render\
-   [ ] Integração Inven!RA\
-   [ ] Relatório APSI

------------------------------------------------------------------------

## 🔗 Contato

**Weber Marcelo Guirra de Souza**\
MEIW -- Universidade Aberta / UTAD
