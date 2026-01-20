from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agente Matemática")

class Pergunta(BaseModel):
    usuario: str
    pergunta: str

@app.post("/agente_matematica")
def responder(p: Pergunta):
    if "derivada" in p.pergunta.lower():
        return {"resposta": "A derivada de x² é 2x."}
    return {"resposta": "Desculpe, não sei essa questão de matemática."}
