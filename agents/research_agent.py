from langchain_core.messages import HumanMessage


def research_agent(model, query, context=""):


    prompt = f"""
You are a research agent.

Answer using the given context.

Context:
{context}

Question:
{query}

Give a clear answer.
"""


    response = model.invoke(
        [
            HumanMessage(
                content=prompt
            )
        ]
    )


    return response.content