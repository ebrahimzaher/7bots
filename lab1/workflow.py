from langgraph.graph import StateGraph, START, END
from .state import State
from .nodes import node_a

builder = StateGraph(State)

builder.add_node("a", node_a)

builder.add_edge(START, "a")
builder.add_edge("a", END)

graph = builder.compile()