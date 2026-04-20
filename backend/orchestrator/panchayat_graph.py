from typing import TypedDict

class PanchayatState(TypedDict):
    goal: str
    career_plan: str
    learning_plan: str


from agents.sarpanch_agent import sarpanch_agent
from agents.learning_agent import learning_agent


def sarpanch_node(state):
    goal = state["goal"]
    career_plan = sarpanch_agent(goal)
    return {
        "career_plan": career_plan
    }


def shiksha_node(state):
    career_plan = state["career_plan"]
    learning_plan = learning_agent(career_plan)
    return {
        "learning_plan": learning_plan
    }


from langgraph.graph import StateGraph


def create_panchayat_graph():
    workflow = StateGraph(PanchayatState)
    workflow.add_node("sarpanch", sarpanch_node)
    workflow.add_node("shiksha", shiksha_node)
    workflow.set_entry_point("sarpanch")
    workflow.add_edge("sarpanch", "shiksha")
    workflow.set_finish_point("shiksha")
    return workflow.compile()


