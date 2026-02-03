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
    ### ✈️ Your Trip to {hotel['location']}
    
    Get ready! We found a great **{flight['airline']}** flight for you, departing at **{flight['departure_time']}**. The ticket is a steal at **${flight['price']}**.
    
    You'll be staying at the **{hotel['name']}** ({hotel['rating']} stars). It's a wonderful spot to relax, costing **${hotel['price_per_night']} per night**.
    
    ### 🌟 Things to Do
    We've lined up some amazing activities:
    """
    
    for activity in activities:
        itinerary_text += f"- Enjoy the **{activity['name']}**.\n"
        
    itinerary_text += "\nHave a safe and wonderful trip! 🌍"
    return {"itinerary": itinerary_text, "messages": [AIMessage(content="Itinerary generated.")]}
