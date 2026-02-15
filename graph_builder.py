import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from state import TherapyState
from therapy_prompts import THERAPY_SYSTEM_PROMPT

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

# Therapy Node
def therapy_node(state: TherapyState):
    messages = state["messages"]

    response = llm.invoke(
        [SystemMessage(content=THERAPY_SYSTEM_PROMPT)] + messages
    )

    return {
        "messages": messages + [response]
    }

# Build Graph
def build_graph():
    builder = StateGraph(TherapyState)

    builder.add_node("therapy", therapy_node)

    builder.set_entry_point("therapy")
    builder.add_edge("therapy", END)

    return builder.compile()
