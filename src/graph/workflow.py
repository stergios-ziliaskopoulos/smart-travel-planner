from langgraph.graph import StateGraph, START, END
from src.graph.state import AgentState
from src.agents.planner import planner_node
from src.agents.researcher import researcher_node
from src.agents.itinerary import itinerary_node
from src.agents.reviewer import reviewer_node

# --- GRAPH ---

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("planner", planner_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("itinerary_generator", itinerary_node)
workflow.add_node("reviewer", reviewer_node)

# Add Edges
workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "itinerary_generator")
workflow.add_edge("itinerary_generator", "reviewer")
workflow.add_edge("reviewer", END)

# Compile
app = workflow.compile()
