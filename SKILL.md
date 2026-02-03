---
name: smart-travel-planner
description: >
  Builds a Multi-Agent AI Travel Planner using LangChain, LangGraph, and Streamlit.
  The app takes a user's travel request and coordinates agents (Planner, Researcher,
  Itinerary, Reviewer) to produce a detailed travel plan.
tags:
  - langchain
  - langgraph
  - streamlit
  - multi-agent
  - python
priority: high
---

# Goal
Create a production-ready, GitHub-friendly repository for a "Smart Travel Planner".
The system must demonstrate complex multi-agent orchestration but remain easy to demo via Streamlit.
Use **Mock Tools** for flights/hotels to ensure the demo works without requiring expensive API keys.

# Project Structure
Ensure the code is organized as follows:
- `src/agents/`: Contains individual agent logic (planner.py, researcher.py, itinerary.py, reviewer.py).
- `src/graph/`: Contains the LangGraph state machine and workflow definition (workflow.py).
- `src/tools/`: Contains mock search tools (e.g., `search_flights`, `search_hotels` returning dummy JSON data).
- `app/`: Contains the Streamlit frontend (`main.py`).
- `main.py`: Entry point for local testing (optional).
- `requirements.txt`: All dependencies (langchain, langgraph, streamlit, openai).

# Instructions

When using this skill to build or update the project:

1.  **Architecture Setup (LangGraph)**
    - Define a `AgentState` TypedDict containing: `user_request`, `plan`, `research_data`, `itinerary`, `feedback`.
    - Create a graph where:
      - **Planner** breaks the request into steps.
      - **Researcher** fetches mock data (flights, hotels, activities).
      - **Itinerary** combines research into a day-by-day schedule.
      - **Reviewer** checks for budget constraints and logic errors.
    - Use a `Supervisor` node or simple conditional edges to manage the flow.

2.  **Implementation Details**
    - **Agents**: Use distinct system prompts for each agent to give them personality.
    - **Mock Tools**: Implement functions that return realistic but fake data (e.g., "Ryanair, €120, 08:00 AM"). This is crucial so the recruiter can run the demo immediately.
    - **Streamlit UI**:
      - Create a chat interface or a form for input (Destination, Budget, Dates).
      - Display the "Agent Thoughts" (e.g., "Researcher is looking for hotels...") using `st.status` or `st.write`.
      - Render the final output in clean Markdown.

3.  **Documentation (Recruiter Friendly)**
    - Generate a `README.md` that explains:
      - What the project is ("Multi-Agent AI that plans your trips").
      - How to run it (`pip install -r requirements.txt` -> `streamlit run app/main.py`).
      - A diagram (mermaid.js) of the agent workflow.

4.  **Refinement**
    - Ensure code is modular. Do not put everything in one file.
    - Add comments explaining *why* LangGraph is used (state management).

# Examples

**User Input:** "I want to go to Rome for 3 days with 500 euros."
**Expected Flow:**
1. Planner creates a plan: Flight -> Hotel -> Colosseum -> Vatican.
2. Researcher returns: "Hotel Artemide (€100/night)", "Ryanair Flight (€80)".
3. Itinerary Builder formats: "Day 1: Arrival & Hotel check-in..."
4. Reviewer checks: Total €380 < €500. Approved.

# Constraints
- Do NOT use real paid APIs (Serper, Amadeus) by default; use Mock classes to ensure the demo never fails.
- Keep the UI clean and visual (use emojis).
- Ensure error handling: If an agent fails, the graph should not crash the Streamlit app.
