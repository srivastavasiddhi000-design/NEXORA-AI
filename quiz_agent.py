from langchain_core.messages import HumanMessage


def quiz_agent(model, context):

    prompt = f"""
You are Nexora AI.

Create a quiz from the document.

Document:

{context}

Generate:

1. 5 Multiple Choice Questions
2. 4 Options for each question
3. Correct Answer

Format clearly.
"""

    response = model.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content