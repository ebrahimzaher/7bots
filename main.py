from lab5 import graph, State
from langgraph.types import Command

def main():
    png_bytes = graph.get_graph().draw_mermaid_png()
    
    with open("lab5/lab5_graph.png", "wb") as f:
        f.write(png_bytes)
    print("✅ Graph image saved successfully as 'lab5_graph.png'")
    
    config = {"configurable": {"thread_id": "1"}}

    while True:
        user = input("b, c, or q to quit: ")
        input_state = State(nlist=[user])

        result = graph.invoke(input_state, config=config)

        if '__interrupt__' in result:
            print(f"Interrupt Triggered: {result}")
            msg = result['__interrupt__'][-1].value

            human = input(f"\n{msg} (type 'continue' or anything else to quit): ")

            human_response = Command(
                resume=human
            )
            result = graph.invoke(human_response, config=config)

        print(result)

        if result.get("nlist") and result["nlist"][-1] == "q":
            print("Quit")
            break

if __name__ == "__main__":
    main()