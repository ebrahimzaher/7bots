from .state import State

def node_a(state: State) -> State:
    print(f"node a is receiving {state['nlist']}")
    note = "Hello world from node a"
    return {"nlist": [note]}