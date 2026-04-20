from models.llm import get_llm

def learning_agent(career_plan):

    llm = get_llm("phi3")

    prompt = f"""

You are Shiksha Mantri — Learning Advisor of Panchayat AI.

Career Plan:
{career_plan}

Your task:

Create:

1. Learning Roadmap
2. Courses to Study
3. Skills Order
4. Weekly Plan
5. Recommended Projects

Respond in structured format.
"""
    
    response = llm.invoke(prompt)
    return response