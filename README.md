# 📘 Activity Provider – Inven!RA
### 🧩 Jogo Sopa de Letras
### UC: Arquitetura e Padrões de Software (APSI) – MEIW – UAb/UTAD  
### Autor: **Weber Marcelo Guirra de Souza**

---

## 📌 Objetivo do Projeto

Este projeto implementa um **Activity Provider** integrado à plataforma **Inven!RA**, simulando a atividade educacional **“Jogo Sopa de Letras”**.

A implementação faz parte da unidade curricular **Arquitetura e Padrões de Software (APSI)**, aplicando:

- Arquitetura orientada a serviços  
- Padrões de criação (Factory Method / Simple Factory, descritos no relatório)  
- Web services RESTful  
- Integração com plataforma educativa (Inven!RA)

O Activity Provider disponibiliza um servidor com Web services RESTful acessível publicamente, conforme especificação da atividade **“Activity Providers na Inven!RA – Implementando um servidor com Web services RESTful”**.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**  
- **FastAPI** – Framework para APIs REST  
- **Uvicorn** – Servidor ASGI  
- **Render.com** – Hospedagem e disponibilização online  
- **Git + GitHub** – Versionamento e histórico de evolução do projeto  

---

## 🌐 URL de Produção (Render)

O Activity Provider está disponível publicamente em:

```text
https://activity-provider-invenra.onrender.com/
```

### Endpoints principais (com URL completa)

| Método | Endpoint | URL completa | Descrição |
|--------|----------|-------------|-----------|
| `GET`  | `/config` | `https://activity-provider-invenra.onrender.com/config` | Configuração básica da atividade |
| `GET`  | `/params` | `https://activity-provider-invenra.onrender.com/params` | Lista de parâmetros configuráveis pelo instrutor |
| `POST` | `/deploy` | `https://activity-provider-invenra.onrender.com/deploy` | Criação de uma instância da atividade (usa padrão de criação) |
| `GET`  | `/analytics/available` | `https://activity-provider-invenra.onrender.com/analytics/available` | Tipos de analytics disponíveis |
| `GET`  | `/analytics` | `https://activity-provider-invenra.onrender.com/analytics` | Dados de analytics simulados |

Documentação automática (Swagger UI):

```text
https://activity-provider-invenra.onrender.com/docs
```

---

## 📂 Estrutura do Projeto

```text
activity_provider_invenra/
│
├── main.py                # Código principal da API FastAPI
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação do projeto
└── .gitignore             # Arquivos ignorados pelo Git
```

---

## 🧱 Arquitetura do Activity Provider

A arquitetura adotada considera:

- A plataforma **Inven!RA** como cliente dos serviços REST
- O **Activity Provider** como servidor externo
- Um componente responsável por gerir o **Jogo Sopa de Letras** (instâncias da atividade)
- Um módulo de **Analytics** responsável por enviar dados da atividade
- Um repositório de dados (banco de dados) previsto para fases futuras do projeto

### Diagrama de Componentes

O diagrama abaixo foi produzido na fase de conceção da arquitetura e representa a interação entre:

- Plataforma Inven!RA  
- Activity Provider  
- Componente de Jogos  
- Módulo de Analytics  
- Banco de dados  

Para exibir a imagem corretamente no GitHub, salvar o diagrama na pasta `docs/` com o nome:

```text
docs/diagrama-componentes-sopa-letras-invenra.png
```

E o README referencia a imagem assim:

```markdown
![Diagrama de Componentes – Sopa de Letras / Inven!RA](docs/diagrama-componentes-sopa-letras-invenra.png)
```

---

## ▶️ Como Executar Localmente

### 1. Criar ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o servidor

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

---

## 🌐 Deploy no Render – Configuração Utilizada

No serviço Web do Render, foram definidos:

- **Build Command**

```bash
pip install -r requirements.txt
```

- **Start Command**

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

- **Branch:** `main`  
- **Plano:** Free  
- **Runtime:** Python  

A cada *push* para a branch `main`, o Render pode ser configurado para atualizar automaticamente a aplicação (redeploy automático).

---

## 🏆 Estado Atual do Projeto

- [x] Arquitetura definida (diagrama de componentes)  
- [x] Serviços REST implementados em FastAPI  
- [x] Teste local concluído com sucesso  
- [x] Deploy realizado no Render (URL pública disponível)  
- [ ] Integração e testes finais com a plataforma Inven!RA  
- [ ] Documentação detalhada do padrão de criação no relatório da UC APSI  

---

## 🧾 Versões e Entregas (Git/GitHub)

Este repositório será utilizado para controlar a evolução do projeto, permitindo:

- Marcação da versão correspondente à entrega **“Activity Providers na Inven!RA – Implementando um servidor com Web services RESTful”** através de *tags* no Git.  
- Manter um histórico de melhorias e refatorações posteriores à entrega.

Exemplo de tag sugerida para a versão de entrega:

```bash
git tag -a v1.0-entrega-apsi -m "Entrega APSI - Activity Provider InvenRA (servidor RESTful implementado)"
git push origin v1.0-entrega-apsi
```

---

## 📄 Licença

Projeto acadêmico desenvolvido para a unidade curricular **Arquitetura e Padrões de Software (APSI)** do Mestrado em Tecnologias e Sistemas Informáticos Web (MEIW) – Universidade Aberta / UTAD.

---

## 🔗 Contato

**Weber Marcelo Guirra de Souza**  
Mestrado em Tecnologias e Sistemas Informáticos Web (MEIW)  
Universidade Aberta / UTAD
