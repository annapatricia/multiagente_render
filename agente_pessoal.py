from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agente Pessoal")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

@app.post("/agente_pessoal")
def responder(p: Pergunta):
    return {"resposta": f"{p.usuario}, sobre você: gosto de estudar IA e resolver quebra-cabeças!"}
