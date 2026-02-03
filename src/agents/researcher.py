from langchain_core.messages import AIMessage
from src.graph.state import AgentState
from src.tools.mocks import search_flights, search_hotels, search_activities

def researcher_node(state: AgentState):
    """
    Researcher executes tools to gather data based on the plan.
    """
    print("--- RESEARCHER ---")
    
    # Extract destination from state
    # Fallback to Rome if not found (though UI ensures it)
    destination = state.get("destination", "Rome")
    print(f"Researching for: {destination}")
    
    flights = search_flights.invoke({"origin": "New York", "destination": destination, "date": "2024-06-01"})
    hotels = search_hotels.invoke({"location": destination})
    activities = search_activities.invoke({"location": destination})
    
    research_data = {
        "flights": flights,
        "hotels": hotels,
        "activities": activities
    }
    return {"research_data": research_data, "messages": [AIMessage(content="Research complete.")]}
