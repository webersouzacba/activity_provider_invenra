from datetime import datetime
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(
    title="Activity Provider – Sopa de Letras – Inven!RA",
    version="1.0.0",
    description=(
        "Activity Provider de exemplo para a plataforma Inven!RA, "
        "implementando os serviços RESTful exigidos na atividade "
        "«Activity Providers na Inven!RA – Implementando um servidor com Web services RESTful»."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://127.0.0.1:5500"]
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
async def home():
    return FileResponse("static/index.html")


# Definições de parâmetros e analytics conforme proposta do projeto


PARAM_DEFS = [
    {"name": "nome", "type": "text/plain"},
    {"name": "orientacoes", "type": "text/plain"},
    {"name": "tempoLimiteSegundos", "type": "integer"},
    {"name": "tamanhoQuadro", "type": "integer"},
    {"name": "sensivelMaiusculas", "type": "boolean"},
    {"name": "permitirDiagonais", "type": "boolean"},
    {"name": "parametrosPalavras", "type": "json"},
]

# Analytics disponíveis

ANALYTICS_DEFS = {
    "qualAnalytics": [
        {"name": "ultima_palavra_encontrada", "type": "text/plain"},
        {"name": "sequencia_cliques", "type": "array/string"},
    ],
    "quantAnalytics": [
        {"name": "tentativas_total", "type": "integer"},
        {"name": "tentativas_corretas", "type": "integer"},
        {"name": "tentativas_erradas", "type": "integer"},
        {"name": "tempo_medio_por_acerto_s", "type": "number"},
        {"name": "percentual_acertos", "type": "number"},
        {"name": "percentual_erros", "type": "number"},
    ],
}

# Armazenamento em memória para instâncias e analytics simulados

DEPLOYED_ACTIVITIES = {}  # activityID -> user_url (e, no futuro, config, etc.)


# Modelos Pydantic para pedidos/respostas

class AnalyticsRequest(BaseModel):
    activityID: str


class QuantRecord(BaseModel):
    name: str
    value: Union[int, float, bool]


class QualRecord(BaseModel):
    name: str
    value: Union[str, List[str]]


class StudentAnalytics(BaseModel):
    inveniraStdID: int
    quantAnalytics: List[QuantRecord]
    qualAnalytics: List[QualRecord]


# Página de configuração (config_url) – GET /config
#    Devolve HTML, não JSON

@app.get("/config", response_class=HTMLResponse)
async def get_config():
    """
    Página de configuração da atividade (config_url).

    Devolve um bloco HTML com os campos de configuração.
    A Inven!RA irá usar este HTML para apresentar a página de configuração
    ao professor/formador e recolher os valores dos campos.
    """
    html = """
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8" />
        <title>Configuração – Sopa de Letras</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 1.5rem; }
            h1 { font-size: 1.4rem; }
            label { display: block; margin-top: 0.8rem; font-weight: bold; }
            input[type="text"], input[type="number"], textarea, select {
                width: 100%; max-width: 600px; padding: 0.3rem; margin-top: 0.2rem;
            }
            small { color: #555; display: block; margin-top: 0.15rem; }
            .checkbox-group { margin-top: 0.5rem; }
        </style>
    </head>
    <body>
        <h1>Configuração da Atividade – Jogo Sopa de Letras</h1>

        <label for="nome">Nome da atividade</label>
        <input id="nome" name="nome" type="text" value="Sopa de Letras – Vocabulário" />
        <small>Identificação da atividade para o professor.</small>

        <label for="orientacoes">Orientações para o aluno</label>
        <textarea id="orientacoes" name="orientacoes" rows="4">
Encontre todas as palavras relacionadas ao tema proposto, no idioma alvo, dentro do tempo limite.
        </textarea>
        <small>Texto exibido aos alunos com instruções da atividade.</small>

        <label for="tempoLimiteSegundos">Tempo limite por tentativa (segundos)</label>
        <input id="tempoLimiteSegundos" name="tempoLimiteSegundos" type="number" value="300" min="30" max="3600" />
        <small>Tempo máximo para o aluno completar uma tentativa.</small>

        <label for="tamanhoQuadro">Tamanho do quadro (linhas/colunas)</label>
        <input id="tamanhoQuadro" name="tamanhoQuadro" type="number" value="12" min="6" max="20" />
        <small>Define o tamanho da grelha de letras.</small>

        <div class="checkbox-group">
            <input id="sensivelMaiusculas" name="sensivelMaiusculas" type="checkbox" />
            <label for="sensivelMaiusculas" style="display:inline; font-weight:normal;">
                Diferenciar maiúsculas e minúsculas
            </label>
        </div>

        <div class="checkbox-group">
            <input id="permitirDiagonais" name="permitirDiagonais" type="checkbox" checked />
            <label for="permitirDiagonais" style="display:inline; font-weight:normal;">
                Permitir palavras na diagonal
            </label>
        </div>

        <label for="parametrosPalavras">Parâmetros de palavras (JSON)</label>
        <textarea id="parametrosPalavras" name="parametrosPalavras" rows="6">
{
  "idioma_nativo": ["cachorro", "gato", "casa"],
  "idioma_alvo": ["dog", "cat", "house"]
}
        </textarea>
        <small>JSON com listas de palavras no idioma nativo e no idioma de aprendizagem.</small>

        <!--
            Não há botão "Guardar" ou "OK": a Inven!RA recolhe os valores
            diretamente dos campos desta página.
        -->
    </body>
    </html>
    """
    return HTMLResponse(content=html)


# Lista de parâmetros (json_params_url) – GET /params

@app.get("/params")
async def get_params():
    """
    json_params_url – devolve a lista de parâmetros configuráveis,
    conforme a proposta do Activity Provider.
    """
    return PARAM_DEFS


# Deploy de atividade (user_url) – GET /deploy
#    Primeira fase do deploy

def _get_base_url() -> str:
    """
    Tenta descobrir a BASE_URL a partir de variável de ambiente.
    Se não existir, usa localhost. No Render, defina BASE_URL
    como https://activity-provider-invenra.onrender.com
    """
    return os.getenv("BASE_URL", "http://127.0.0.1:8000")


@app.get("/deploy")
async def deploy_activity(
    activityID: str = Query(...,
                            description="ID da instância da atividade na Inven!RA")
):
    """
    Serviço de deploy (user_url) – primeira fase.
    A Inven!RA faz um GET com o parâmetro activityID.
    O Activity Provider prepara-se para guardar analytics e devolve
    o URL que os alunos irão usar para aceder à atividade.
    """
    base_url = _get_base_url()
    user_url = f"{base_url}/play?activityID={activityID}"

    # Regista em memória (simulação) que esta atividade foi "deployada"
    DEPLOYED_ACTIVITIES[activityID] = {
        "user_url": user_url,
        "created_at": datetime.utcnow().isoformat(),
    }

    return {
        "activityID": activityID,
        "user_url": user_url,
    }


# Lista de analytics disponíveis (analytics_list_url) – GET

@app.get("/analytics/available")
async def get_available_analytics():
    """
    analytics_list_url – devolve lista de analytics disponíveis
    (qualitativos e quantitativos), conforme a proposta.
    """
    return ANALYTICS_DEFS


# Analytics de atividade (analytics_url) – POST /analytics

@app.post("/analytics", response_model=List[StudentAnalytics])
async def get_analytics(payload: AnalyticsRequest):
    """
    analytics_url – a Inven!RA envia um JSON com { "activityID": "..." }.
    Devolve uma lista com os dados analíticos de todos os alunos que
    realizaram a atividade, usando os nomes de métricas definidos na proposta.

    Nesta fase do projeto, os dados são simulados.
    """
    activity_id = payload.activityID

    # Exemplo de dados simulados para dois alunos
    now = datetime.utcnow().isoformat()

    aluno1 = StudentAnalytics(
        inveniraStdID=1001,
        quantAnalytics=[
            QuantRecord(name="tentativas_total", value=5),
            QuantRecord(name="tentativas_corretas", value=4),
            QuantRecord(name="tentativas_erradas", value=1),
            QuantRecord(name="tempo_medio_por_acerto_s", value=42.5),
            QuantRecord(name="percentual_acertos", value=80.0),
            QuantRecord(name="percentual_erros", value=20.0),
        ],
        qualAnalytics=[
            QualRecord(name="ultima_palavra_encontrada", value="house"),
            QualRecord(
                name="sequencia_cliques",
                value=["h(1,1)", "o(1,2)", "u(1,3)", "s(1,4)", "e(1,5)"],
            ),
        ],
    )

    aluno2 = StudentAnalytics(
        inveniraStdID=1002,
        quantAnalytics=[
            QuantRecord(name="tentativas_total", value=3),
            QuantRecord(name="tentativas_corretas", value=1),
            QuantRecord(name="tentativas_erradas", value=2),
            QuantRecord(name="tempo_medio_por_acerto_s", value=60.0),
            QuantRecord(name="percentual_acertos", value=33.3),
            QuantRecord(name="percentual_erros", value=66.7),
        ],
        qualAnalytics=[
            QualRecord(name="ultima_palavra_encontrada", value="cat"),
            QualRecord(
                name="sequencia_cliques",
                value=["c(2,1)", "a(2,2)", "t(2,3)"],
            ),
        ],
    )

    # Aqui poderíamos filtrar por activity_id se tivéssemos persistência real.
    return [aluno1, aluno2]
