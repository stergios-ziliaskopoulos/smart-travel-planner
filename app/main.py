import sys
import os

# Προσθέτει τον κεντρικό φάκελο στο path για να βρει το 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.graph.workflow import app as graph_app

st.title("🌍 Smart Travel Planner")
st.markdown("Plan your next trip with AI agents!")

with st.sidebar:
    st.header("Trip Details")
    origin = st.text_input("From", "New York")
    destination = st.text_input("Destination", "Rome")
    budget = st.number_input("Budget (€)", min_value=100, value=500)
    days = st.number_input("Duration (Days)", min_value=1, value=3)

user_input = st.text_area("Tell us more about your trip (optional)", 
                          f"I want to go to {destination} for {days} days with {budget} euros.")

if st.button("Plan Trip"):
    with st.spinner("Agents are working..."):
        # Initialize state
        initial_state = {
            "user_request": user_input,
            "destination": destination,
            "origin": origin,
            "plan": [],
            "plan": [],
            "research_data": {},
            "itinerary": "",
            "feedback": "",
            "messages": []
        }
        
        # Run the graph
        # Since we are using a sync graph compilation in workflow.py, we can just invoke it.
        # If it was async, we'd need asyncio.
        final_state = graph_app.invoke(initial_state)
        
        st.success("Trip Planned!")
        
        st.subheader("Generated Itinerary")
        st.markdown(final_state["itinerary"])
        
        with st.expander("View Agent Logic"):
            st.json(final_state)
