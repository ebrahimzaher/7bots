from .state import State

def node_a(state: State) -> State:
    print(f"Adding 'A' to {state['nlist']}")
    return State(nlist=["A"])

def node_b(state: State) -> State:
    print(f"Adding 'B' to {state['nlist']}")
    return State(nlist=["B"])

def node_c(state: State) -> State:
    print(f"Adding 'C' to {state['nlist']}")
    return State(nlist=["C"])

def node_bb(state: State) -> State:
    print(f"Adding 'BB' to {state['nlist']}")
    return State(nlist=["BB"])

def node_cc(state: State) -> State:
    print(f"Adding 'CC' to {state['nlist']}")
    return State(nlist=["CC"])

def node_d(state: State) -> State:
    print(f"Adding 'D' to {state['nlist']}")
    return State(nlist=["D"])