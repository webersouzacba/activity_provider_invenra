# 📘 Activity Provider – Inven!RA
### 🧩 Jogo Sopa de Letras
### UC: Arquitetura e Padrões de Software (APSI) – MEIW – UAb/UTAD  
### Autor: **Weber Marcelo Guirra de Souza**

---

## 📌 Objetivo do Projeto

Este projeto implementa um **Activity Provider** totalmente compatível com a plataforma **Inven!RA**, seguindo integralmente:

- A especificação oficial *«Activity Providers na Inven!RA»*  
- As instruções da atividade **“Implementando um servidor com Web services RESTful”**  
- A proposta do projeto **Sopa de Letras**, contendo parâmetros configuráveis e analytics definidos pelo autor.

O objetivo é fornecer um serviço RESTful que permita à Inven!RA:

✔ renderizar a página de configuração da atividade  
✔ obter a lista de parâmetros configuráveis  
✔ realizar o *deploy* de uma instância da atividade  
✔ consultar analytics de alunos  
✔ conhecer os analytics que a atividade disponibiliza  

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**  
- **FastAPI** – Framework moderno para APIs REST  
- **Uvicorn** – Servidor ASGI  
- **Render.com** – Deploy público da API  
- **Git/GitHub** – Versionamento e entrega contínua  

---

# 🌐 URL de Produção (Render)

O serviço está disponível publicamente em:

```
https://activity-provider-invenra.onrender.com/
```

---

# 📡 Endpoints Implementados (versão final)

Todos os serviços abaixo seguem **exatamente** a especificação da Inven!RA.

---

## 1. **Página de configuração da atividade**  
### `GET /config`

Retorna **HTML**, não JSON.

Este HTML contém os campos:

| Campo | Tipo | Descrição |
|-------|-------|-----------|
| nome | text | Nome da atividade |
| orientacoes | textarea | Instruções para o aluno |
| tempoLimiteSegundos | number | Tempo máximo (segundos) |
| tamanhoQuadro | number | Tamanho da grelha (NxN) |
| sensivelMaiusculas | checkbox | Caso sensível |
| permitirDiagonais | checkbox | Permitir diagonais |
| parametrosPalavras | textarea (JSON) | Palavras da atividade |

---

## 2. **Lista de parâmetros configuráveis**  
### `GET /params`

Devolve **JSON**:

```json
[
  {"name": "nome", "type": "text/plain"},
  {"name": "orientacoes", "type": "text/plain"},
  {"name": "tempoLimiteSegundos", "type": "integer"},
  {"name": "tamanhoQuadro", "type": "integer"},
  {"name": "sensivelMaiusculas", "type": "boolean"},
  {"name": "permitirDiagonais", "type": "boolean"},
  {"name": "parametrosPalavras", "type": "json"}
]
```

---

## 3. **Deploy da atividade (primeira fase)**  
### `GET /deploy?activityID=XXXX`

A Inven!RA chama este serviço ao disponibilizar a atividade aos alunos.

Exemplo de resposta:

```json
{
  "activityID": "ABC123",
  "user_url": "https://activity-provider-invenra.onrender.com/play?activityID=ABC123"
}
```

---

## 4. **Analytics de atividade**  
### `POST /analytics`

Entrada:

```json
{ "activityID": "ABC123" }
```

Saída (lista de alunos + analytics):

```json
[
  {
    "inveniraStdID": 1001,
    "quantAnalytics": [
      {"name": "tentativas_total", "value": 5},
      {"name": "tentativas_corretas", "value": 4},
      {"name": "tentativas_erradas", "value": 1},
      {"name": "tempo_medio_por_acerto_s", "value": 42.5},
      {"name": "percentual_acertos", "value": 80.0},
      {"name": "percentual_erros", "value": 20.0}
    ],
    "qualAnalytics": [
      {"name": "ultima_palavra_encontrada", "value": "house"},
      {"name": "sequencia_cliques", "value": ["h(1,1)", "o(1,2)", "u(1,3)", "s(1,4)", "e(1,5)"]}
    ]
  }
]
```

---

## 5. **Lista de analytics disponíveis**  
### `GET /analytics/available`

```json
{
  "qualAnalytics": [
    {"name": "ultima_palavra_encontrada", "type": "text/plain"},
    {"name": "sequencia_cliques", "type": "array/string"}
  ],
  "quantAnalytics": [
    {"name": "tentativas_total", "type": "integer"},
    {"name": "tentativas_corretas", "type": "integer"},
    {"name": "tentativas_erradas", "type": "integer"},
    {"name": "tempo_medio_por_acerto_s", "type": "number"},
    {"name": "percentual_acertos", "type": "number"},
    {"name": "percentual_erros", "type": "number"}
  ]
}
```

---

# 📂 Estrutura do Projeto

```
activity_provider_invenra/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ Executando Localmente

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

# 🌐 Deploy no Render – Configuração

**Build:**  
```
pip install -r requirements.txt
```

**Start:**  
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
---

# 🔗 Contato

**Weber Marcelo Guirra de Souza**  
MEIW – Universidade Aberta / UTAD  
