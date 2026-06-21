from langchain_core.messages import HumanMessage


def summary_agent(model, context):

    prompt = f"""
You are Nexora AI.

Create a concise and well-structured summary
of the following document.

Document:

{context}

Give:
1. Main Topics
2. Important Concepts
3. Key Takeaways
"""

    response = model.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content