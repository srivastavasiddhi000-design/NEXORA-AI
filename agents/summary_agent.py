from langchain_core.messages import HumanMessage


def summary_agent(model, pdf_text):

    prompt = f"""
You are a document summary agent.

Summarize the given document clearly.

Document:

{pdf_text}

Include:
- Main points
- Important concepts
- Key information
"""


    response = model.invoke(
        [
            HumanMessage(
                content=prompt
            )
        ]
    )


    return response.content