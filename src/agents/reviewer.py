from src.graph.state import AgentState

def reviewer_node(state: AgentState):
    """
    Reviewer checks if the itinerary meets the budget and constraints.
    """
    print("--- REVIEWER ---")
    # Mock review logic
    return {"feedback": "Approved"}
