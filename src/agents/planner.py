from langchain_core.messages import AIMessage
from src.graph.state import AgentState

def planner_node(state: AgentState):
    """
    Planner breaks down the user request into a high-level plan.
    """
    print("--- PLANNER ---")
    request = state["user_request"]
    # Mock planning logic
    plan = [
        "Search for flights to the destination.",
        "Search for hotels in the destination.",
        "Identify top 3 attractions.",
        "Compile itinerary."
    ]
    return {"plan": plan, "messages": [AIMessage(content=f"Plan created: {plan}")]}
