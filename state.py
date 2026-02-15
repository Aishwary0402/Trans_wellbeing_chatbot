from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class TherapyState(TypedDict):
    messages: List[BaseMessage]
    user_emotion: str