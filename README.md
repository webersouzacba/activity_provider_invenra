# 📘 Activity Provider – Inven!RA
### 🧩 Jogo Sopa de Letras
### UC: Arquitetura e Padrões de Software (APSI) – MEIW – UAb/UTAD
### Autor: **Weber Marcelo Guirra de Souza**

---

## 📌 Objetivo do Projeto

Este projeto implementa um **Activity Provider** compatível com a plataforma **Inven!RA**, seguindo rigorosamente:

- A especificação oficial *«Activity Providers na Inven!RA»*
- A atividade **“Implementando um servidor com Web services RESTful”**
- A proposta do projeto **Sopa de Letras**, com parâmetros configuráveis e analytics definidos no escopo do trabalho

O Activity Provider permite que a plataforma Inven!RA:

✔ Renderize a página de configuração da atividade  
✔ Obtenha a lista de parâmetros configuráveis  
✔ Realize o *deploy* da instância da atividade  
✔ Consulte analytics por aluno  
✔ Obtenha a lista de analytics disponíveis  

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI** – Framework moderno para APIs REST
- **Uvicorn** – Servidor ASGI
- **Render.com** – Hospedagem e deploy da API
- **Git/GitHub** – Versionamento e trabalho colaborativo

---

# 🌐 URL de Produção (Render)

O serviço está disponível publicamente em:

🔗 **https://activity-provider-invenra.onrender.com/**

---

# 📡 Endpoints Implementados (versão final)

Todos os serviços seguem estritamente a especificação da Inven!RA.

---

## 1. **Página de configuração da atividade**
### `GET /config`

Retorna **HTML** contendo os campos preenchidos pelo professor.

📌 URL:  
https://activity-provider-invenra.onrender.com/config

---

## 2. **Lista de parâmetros configuráveis**
### `GET /params`

📌 URL:  
https://activity-provider-invenra.onrender.com/params

---

## 3. **Deploy da atividade (primeira fase)**
### `GET /deploy?activityID=XXXX`

📌 URL de exemplo:  
https://activity-provider-invenra.onrender.com/deploy?activityID=TESTE123

---

## 4. **Analytics da atividade**
### `POST /analytics`

📌 URL:  
https://activity-provider-invenra.onrender.com/analytics

---

## 🔍 **Página de teste do POST `/analytics`**

Para testar o endpoint sem Postman, use o HTML interativo:

👉 **https://activity-provider-invenra.onrender.com/static/teste_analytics_POST.html**

---

## 5. **Lista de analytics disponíveis**
### `GET /analytics/available`

📌 URL:  
https://activity-provider-invenra.onrender.com/analytics/available

---

# 📂 Estrutura do Projeto

```
activity_provider_invenra/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── static/
      └── teste_analytics_POST.html
```

---

# ▶️ Executando Localmente

```
python -m venv venv
venv\Scripts\activate     # Windows
# ou source venv/bin/activate (Linux/macOS)

pip install -r requirements.txt
uvicorn main:app --reload
```

---

# 🌐 Deploy no Render – Configuração

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# 🔗 Repositório no GitHub
https://github.com/webersouzacba/activity_provider_invenra

---

# ✉️ Contato

**Weber Marcelo Guirra de Souza**  
MEIW – Universidade Aberta / UTAD