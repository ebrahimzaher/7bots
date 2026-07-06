from lab1 import graph, State

def main():
    png_bytes = graph.get_graph().draw_mermaid_png()
    
    with open("lab1/lab1_graph.png", "wb") as f:
        f.write(png_bytes)
    print("✅ Graph image saved successfully as 'lab1_graph.png'")

    initial_state = State(
        nlist=["Hello node a"]
    )
    
    print("\n🚀 Starting Graph Execution...")
    result = graph.invoke(initial_state)

    print("\n✅ Final Output:")
    print(result)

if __name__ == "__main__":
    main()