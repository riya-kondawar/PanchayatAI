from models.llm import get_llm

def sarpanch_agent(user_goal):
    llm = get_llm("qwen2.5:3b-instruct")

    prompt = f"""
You are Sarpanch AI — a wise career advisor.

User Goal: {user_goal}

Your task:
Analyze and provide:

1. Career Path
2. Skills Required
3. Learning Roadmap
4. Projects to Build
5. Timeline

Respond in structured format.
"""
    response = llm.invoke(prompt)
    return response