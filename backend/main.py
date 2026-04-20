from fastapi import FastAPI
from agents.sarpanch_agent import sarpanch_agent
from agents.learning_agent import learning_agent
from orchestrator.panchayat_graph import create_panchayat_graph 

app = FastAPI()
graph = create_panchayat_graph()

@app.get("/")
def home():
    return {"message": "Panchayat AI Running"}

@app.post("/panchayat")
def panchayat(goal: str):
    result = graph.invoke({
        "goal": goal
    })
    return result 
