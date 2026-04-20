# Panchayat AI

AI-Powered Multi-Agent Career & Life Planning System

---

# 1. Project Overview

Panchayat AI is a **Multi-Agent Generative AI System** designed to simulate a **Village Panchayat Decision Model** where multiple AI agents collaborate to provide structured guidance.

Instead of a single LLM response, Panchayat AI uses:

* Multi-Agent Architecture
* LangGraph Orchestration
* Shared State (MCP-style)
* Local LLMs via Ollama
* FastAPI Backend

---

# 2. Project Vision

Build a **Personal AI Council** that helps users with:

* Career Planning
* Learning Roadmaps
* Productivity Planning
* Risk Analysis
* Health & Lifestyle Planning

Each handled by a **Specialized AI Agent**.

---

# 3. Current Architecture

User Input
↓
FastAPI Endpoint
↓
LangGraph Orchestrator
↓
Sarpanch Agent (Career Strategy)
↓
Shiksha Mantri (Learning Plan)
↓
Final Response

---

# 4. Tech Stack

## Backend

* Python 3.10+
* FastAPI
* LangGraph
* LangChain
* Ollama (Local LLM)

## Models (Local)

* qwen2.5:3b-instruct (Sarpanch)
* phi3 (Shiksha)
* llama3.1:8b (Future heavy model)

## Development Environment

* CPU-based Local Development
* Uvicorn Server

---

# 5. Project Structure

backend/

main.py

agents/
sarpanch_agent.py
learning_agent.py

orchestrator/
panchayat_graph.py

llm.py

requirements.txt

---

# 6. Installation & Setup

## Step 1 — Create Virtual Environment

python -m venv venv

## Step 2 — Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

## Step 3 — Install Dependencies

pip install fastapi
pip install uvicorn
pip install langchain
pip install langgraph
pip install langchain-ollama
pip install typing-extensions

## Step 4 — Install Ollama

Download from:

[https://ollama.com](https://ollama.com)

## Step 5 — Pull Models

ollama pull qwen2.5:3b-instruct
ollama pull phi3
ollama pull llama3.1:8b

Verify:

ollama list

---

# 7. LLM Configuration

File: llm.py

Configuration:

* Temperature: 0.3
* num_predict: 500
* Local Ollama Endpoint

Example:

* Sarpanch → qwen2.5:3b-instruct
* Shiksha → phi3

---

# 8. Agents

## 8.1 Sarpanch Agent

Role:

* Career Planning
* Strategy Creation
* Skill Identification

Input:

* User Goal

Output:

* Career Plan

---

## 8.2 Shiksha Mantri Agent

Role:

* Learning Roadmap
* Courses
* Study Plan

Input:

* Career Plan

Output:

* Learning Roadmap

---

# 9. LangGraph Orchestrator

File:

orchestrator/panchayat_graph.py

State:

PanchayatState

Fields:

* goal
* career_plan
* learning_plan

Workflow:

Sarpanch → Shiksha

---

# 10. FastAPI Endpoint

POST /panchayat

Query Parameter:

goal

Example:

POST /panchayat?goal=I want to become AI engineer

Response:

{
"goal": "...",
"career_plan": "...",
"learning_plan": "..."
}

---

# 11. Running the Project

Start Server:

uvicorn main:app --reload

Open:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Test Endpoint:

POST /panchayat

---

# 12. Performance (CPU)

Current Performance:

* Sarpanch (qwen2.5:3b) → 1-2 min
* Shiksha (phi3) → 30-60 sec

Total Response Time:

2-3 minutes

---

# 13. GenAI Architecture Concepts Used

* Multi-Agent Systems
* LangGraph Orchestration
* Shared State
* Agent Collaboration
* Local LLMs
* Prompt Engineering

---

# 14. Future Agents (Planned)

Productivity Mantri

* Time planning
* Daily schedule

Health Mantri

* Burnout prevention
* Work-life balance

Risk Mantri

* Career risks
* Skill gaps

Finance Mantri

* Salary growth planning

---

# 15. Future Architecture

User
↓
Sarpanch
↓
Shiksha
↓
Productivity
↓
Health
↓
Risk
↓
Final Decision

---

# 16. Future Enhancements

* UI Frontend (React)
* Chat Interface
* Memory System
* User Profiles
* Vector DB (RAG)

---

# 17. Phase-Wise Roadmap

Phase 1

Project Setup

Status: Completed

Phase 2

Multi-Agent Creation

Status: Completed

Phase 3

LangGraph Orchestration

Status: Completed

Phase 4

Add More Agents

Status: Pending

Phase 5

Memory + RAG

Status: Pending

Phase 6

Frontend UI

Status: Pending

Phase 7

Production Deployment

Status: Pending

---

# 18. Learning Outcomes

This project teaches:

* Multi-Agent AI Systems
* LangGraph
* GenAI Architecture
* LLM Optimization
* Prompt Engineering
* Local LLM Deployment

---

# 19. Target Use Cases

* Career Planning
* Student Guidance
* Developer Roadmaps
* Personal AI Assistant

---

# 20. Author

Project Name: Panchayat AI

Type: Multi-Agent GenAI System

Status: In Development

---

# 21. Next Steps

Immediate:

* Add Productivity Agent
* Add Risk Agent

Then:

* Add Memory
* Add UI

---

# 22. Project Status

Current Status:

Multi-Agent System Working
LangGraph Working
Local LLM Working

System is Stable

Ready for Phase 4

---

# End of README
