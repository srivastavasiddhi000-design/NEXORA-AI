from langchain_core.messages import HumanMessage


def planner_agent(model, query):


    prompt = f"""
You are a planning agent.

Create a detailed step-by-step plan.

User request:

{query}


Give:
- Steps
- Timeline
- Tips
"""


    response = model.invoke(
        [
            HumanMessage(
                content=prompt
            )
        ]
    )


    return response.content