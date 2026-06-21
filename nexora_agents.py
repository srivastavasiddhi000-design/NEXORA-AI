import os
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage


load_dotenv()
print("KEY LOADED:", os.getenv("MISTRAL_API_KEY")[:5])

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.3,
    api_key=os.getenv("MISTRAL_API_KEY")
)



# ================= RESEARCH AGENT =================

def research_agent(query):

    response = model.invoke(
        [
            HumanMessage(
                content=f"""
You are Research Agent.

Research and explain:

{query}


Give:
- facts
- latest information
- explanation
- important points

"""
            )
        ]
    )

    return response.content





# ================= SUMMARY AGENT =================


def summary_agent(text):

    response = model.invoke(
        [
            HumanMessage(
                content=f"""
You are Summary Agent.

Summarize this:

{text}


Give:
- short summary
- key points
- important details

"""
            )
        ]
    )

    return response.content






# ================= PLANNER AGENT =================


def planner_agent(task):

    response = model.invoke(
        [
            HumanMessage(
                content=f"""
You are Planner Agent.

Create an execution plan for:

{task}


Give:

1. Steps
2. Timeline
3. Suggestions

"""
            )
        ]
    )

    return response.content