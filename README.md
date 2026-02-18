# 🤖 Multi-Agent Orchestrator (FastAPI + Render)

A lightweight multi-agent system built with FastAPI, where an orchestrator routes user questions to specialized agents (e.g., personal profile Q&A vs math solver). Designed for simple deployment on Render using multiple services.

---

## 🎯 What this project does

- Exposes a single endpoint (`/perguntar`) for user questions
- Classifies the question with simple routing logic
- Forwards the request to the appropriate agent service
- Returns the selected agent response back to the client

This project demonstrates **agent orchestration**, **microservice-style architecture**, and **cloud deployment** using Render.

---

## 🏗 Architecture

Services:

- **Orchestrator API** (`orquestrador.py`)
  - Receives the user input
  - Routes to the correct agent endpoint

- **Personal Agent** (`agente_pessoal.py`)
  - Handles questions like *name*, *hobby*, personal info patterns

- **Math Agent** (`agente_matematica.py`)
  - Handles math-related questions and computations

Routing is currently rule-based (keyword matching), but can be extended to:
- intent classification
- embeddings-based routing
- LLM-based router

---

## 🔌 API

### POST `/perguntar`

Request:
```json
{
  "usuario": "Anna",
  "pergunta": "Qual é o seu hobby?"
}

Response (example):
{
  "resposta": "..."
}
## ⚙️ Configuration (Environment Variables)

The orchestrator dynamically routes requests to agent services using environment variables:

- `AGENTE_PESSOAL_URL`  
  Default: `http://localhost:10001/agente_pessoal`

- `AGENTE_MATEMATICA_URL`  
  Default: `http://localhost:10002/agente_matematica`

In production (e.g., Render), these variables should point to the public URLs of each deployed agent service.


