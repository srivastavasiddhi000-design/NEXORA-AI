from agents.research_agent import research_agent
from agents.summary_agent import summary_agent
from agents.planner_agent import planner_agent



def router_agent(model, query, context=""):


    query_lower = query.lower()



    if "summary" in query_lower or "summarize" in query_lower:

        return summary_agent(
            model,
            context
        )



    elif "plan" in query_lower or "schedule" in query_lower:

        return planner_agent(
            model,
            query
        )



    else:

        return research_agent(
            model,
            query,
            context
        )