from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Orquestrador de Agentes")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

# URLs públicas dos agentes no Render (usar variáveis de ambiente)
AGENTE_PESSOAL = os.environ.get("AGENTE_PESSOAL_URL", "http://localhost:10001/agente_pessoal")
AGENTE_MATEMATICA = os.environ.get("AGENTE_MATEMATICA_URL", "http://localhost:10002/agente_matematica")

@app.post("/perguntar")
def perguntar(p: Pergunta):
    texto = p.pergunta.lower()
    if "hobby" in texto or "nome" in texto:
        url = AGENTE_PESSOAL
    else:
        url = AGENTE_MATEMATICA

    resposta = requests.post(url, json=p.dict()).json()
    return resposta
