from typing import TypedDict, List, Dict, Any
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    user_request: str
    plan: List[str]
    research_data: Dict[str, Any]
    itinerary: str
    feedback: str
    messages: List[BaseMessage]
    destination: str
