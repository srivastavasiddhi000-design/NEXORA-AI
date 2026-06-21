import nexora_agents as agents
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage



from rag import (
    create_vectorstore,
    search_pdf
)


load_dotenv()
import os


import os

print("KEY LENGTH:", len(os.getenv("MISTRAL_API_KEY")))


model = ChatMistralAI(

    model="mistral-large-latest",

    temperature=0.4

)



pdf_store = None





def ask_ai(question, pdf_text=""):

    global pdf_store



    # PDF MEMORY

    if pdf_text and pdf_store is None:

        pdf_store = create_vectorstore(
            pdf_text
        )





    # PDF QUESTION MODE

    if pdf_store:


        context = search_pdf(
            pdf_store,
            question
        )


        prompt = f"""

You are NEXORA AI.

Answer using this PDF context:

{context}


Question:

{question}

"""


        response = model.invoke(

            [
                HumanMessage(
                    content=prompt
                )
            ]

        )


        return response.content





    # AGENT ROUTER


    q = question.lower()





    # PLANNER AGENT

    if any(

        word in q

        for word in [

            "plan",
            "roadmap",
            "steps",
            "schedule"

        ]

    ):


        return agents.planner_agent(
            question
        )






    # SUMMARY AGENT

    elif any(

        word in q

        for word in [

            "summary",
            "summarize",
            "short"

        ]

    ):


        return agents.summary_agent(
            question
        )






    # RESEARCH AGENT

    elif any(

        word in q

        for word in [

            "research",
            "explain",
            "find",
            "latest"

        ]

    ):


        return agents.research_agent(
            question
        )






    # NORMAL CHAT


    response = model.invoke(

        [

            HumanMessage(
                content=question
            )

        ]

    )


    return response.content