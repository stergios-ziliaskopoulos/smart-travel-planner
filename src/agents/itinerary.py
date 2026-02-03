from langchain_core.messages import AIMessage
from src.graph.state import AgentState

def itinerary_node(state: AgentState):
    """
    Itinerary agent compiles the research into a day-by-day plan.
    """
    print("--- ITINERARY ---")
    data = state["research_data"]
    
    # Error handling in case mock data is empty or malformed
    if not data.get("flights") or not data.get("hotels"):
        return {"itinerary": "Could not generate itinerary due to missing data.", "messages": [AIMessage(content="Failed to generate itinerary.")]}

    flight = data["flights"][0]
    hotel = data["hotels"][0]
    activities = data.get("activities", [])
    
    itinerary_text = f"""
    **Travel Itinerary**
    - **Flight**: {flight['airline']}, ${flight['price']}
    - **Hotel**: {hotel['name']}, ${hotel['price_per_night']}/night, {hotel['rating']} stars
    - **Activities**: {', '.join([a['name'] for a in activities])}
    """
    return {"itinerary": itinerary_text, "messages": [AIMessage(content="Itinerary generated.")]}
