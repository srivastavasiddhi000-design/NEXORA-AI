def router_agent(question):

    question = question.lower()

    if any(word in question for word in [
        "summary",
        "summarize",
        "summarise"
    ]):
        return "summary"

    elif any(word in question for word in [
        "quiz",
        "mcq",
        "questions"
    ]):
        return "quiz"

    else:
        return "rag"