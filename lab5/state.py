from typing import Annotated, TypedDict
import operator

class State(TypedDict):
    nlist: Annotated[list[str], operator.add]