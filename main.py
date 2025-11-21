from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Activity Provider - Sopa de Letras - Inven!RA",
    version="1.0.0",
    description="Activity Provider de exemplo para integração com a plataforma Inven!RA."
)

# ---------- MODELOS ----------


class ParameterDefinition(BaseModel):
    name: str
    type: str
    label: str
    default: Optional[str] = None
    required: bool = True
    min: Optional[int] = None
    max: Optional[int] = None
    options: Optional[List[str]] = None  # para listas fechadas


class DeployRequest(BaseModel):
    activity_id: str
    parameters: dict   # valores escolhidos pelo instrutor
    course_id: Optional[str] = None
    teacher_id: Optional[str] = None


class DeployResponse(BaseModel):
    instance_id: str
    activity_launch_url: str
    created_at: datetime
    summary: dict


class AnalyticsMetric(BaseModel):
    id: str
    name: str
    description: str
    type: str    # number, string, event, etc.


class AnalyticsRecord(BaseModel):
    user_id: str
    metric_id: str
    value: float
    timestamp: datetime


class AnalyticsResponse(BaseModel):
    instance_id: str
    records: List[AnalyticsRecord]


# ---------- ENDPOINTS ----------

@app.get("/config")
async def get_config():
    """
    Configuração básica da atividade.
    """
    return {
        "activity_id": "sopa-letras-pt-001",
        "name": "Jogo Sopa de Letras",
        "description": "Atividade de sopa de letras para treino de vocabulário.",
        "version": "1.0.0",
        "author": "Weber Marcelo Guirra de Souza",
        "language": "pt",
        "max_players": 1
    }


@app.get("/params", response_model=List[ParameterDefinition])
async def get_params():
    """
    Parâmetros configuráveis apresentados ao instrutor na Inven!RA.
    """
    return [
        ParameterDefinition(
            name="grid_size",
            type="integer",
            label="Tamanho da grelha (linhas/colunas)",
            default="12",
            min=6,
            max=20,
            required=True
        ),
        ParameterDefinition(
            name="time_limit",
            type="integer",
            label="Tempo limite (segundos)",
            default="300",
            min=60,
            max=1800,
            required=True
        ),
        ParameterDefinition(
            name="difficulty",
            type="string",
            label="Nível de dificuldade",
            default="medio",
            options=["facil", "medio", "dificil"],
            required=True
        )
    ]


@app.post("/deploy", response_model=DeployResponse)
async def deploy_activity(payload: DeployRequest):
    """
    Cria uma instância da atividade com base nos parâmetros recebidos.
    Nesta fase, apenas devolve dados de exemplo.
    """
    # Em produção geraríamos um ID único de verdade (UUID, por ex.)
    instance_id = f"{payload.activity_id}-inst-001"

    launch_url = f"https://seu-dominio-ou-host/sopa-letras?instance_id={instance_id}"

    return DeployResponse(
        instance_id=instance_id,
        activity_launch_url=launch_url,
        created_at=datetime.utcnow(),
        summary={
            "parameters": payload.parameters,
            "course_id": payload.course_id,
            "teacher_id": payload.teacher_id
        }
    )


@app.get("/analytics/available", response_model=List[AnalyticsMetric])
async def get_available_analytics():
    """
    Lista os tipos de analytics que este Activity Provider consegue devolver.
    """
    return [
        AnalyticsMetric(
            id="score",
            name="Pontuação final",
            description="Pontuação total obtida pelo aluno na atividade.",
            type="number"
        ),
        AnalyticsMetric(
            id="time_spent",
            name="Tempo gasto",
            description="Tempo total gasto pelo aluno na atividade (segundos).",
            type="number"
        )
    ]


@app.get("/analytics", response_model=AnalyticsResponse)
async def get_analytics(
    instance_id: str = Query(..., description="ID da instância de atividade")
):
    """
    Devolve dados de analytics (exemplo) para uma instância da atividade.
    Nesta fase, devolvemos dados estáticos/simulados.
    """
    agora = datetime.utcnow()

    records = [
        AnalyticsRecord(
            user_id="aluno1",
            metric_id="score",
            value=85,
            timestamp=agora
        ),
        AnalyticsRecord(
            user_id="aluno1",
            metric_id="time_spent",
            value=240,
            timestamp=agora
        )
    ]

    return AnalyticsResponse(
        instance_id=instance_id,
        records=records
    )
