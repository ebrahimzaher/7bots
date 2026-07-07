from lab2 import graph, State

def main():
    png_bytes = graph.get_graph().draw_mermaid_png()
    
    with open("lab2/lab2_graph.png", "wb") as f:
        f.write(png_bytes)
    print("✅ Graph image saved successfully as 'lab2_graph.png'")

    initial_state = State(
        nlist = ["Initial state:"]
    )
    
    print("\n🚀 Starting Graph Execution...")
    result = graph.invoke(initial_state)

    print("\n✅ Final Output:")
    print(result)

if __name__ == "__main__":
    main()