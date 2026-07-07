from langgraph.graph import StateGraph, START, END
from .state import State
from .nodes import node_a, node_b, node_c
from typing import Literal
from langgraph.checkpoint.memory import InMemorySaver

def conditional_edge(state: State) -> Literal["b", "c", END]:
    select = state["nlist"][-1]

    if select == "b":
        return "b"
    elif select == "c":
        return "c"
    elif select == "q":
        return END
    else:
        return END
    
builder = StateGraph(State)

builder.add_node("a", node_a)
builder.add_node("b", node_b)
builder.add_node("c", node_c)

builder.add_edge(START, "a")

builder.add_edge("b", END)
builder.add_edge("c", END)

builder.add_conditional_edges("a", conditional_edge)

memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)

