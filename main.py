from lab3 import graph, State

def main():
    png_bytes = graph.get_graph().draw_mermaid_png()
    
    with open("lab3/lab3_graph.png", "wb") as f:
        f.write(png_bytes)
    print("✅ Graph image saved successfully as 'lab3_graph.png'")

    while True:
        user = input("b, c, or q to quite:")
        print(user)
        input_state = State(
            nlist = [user]
        )
        result = graph.invoke(input_state)
        print(result)
        if result["nlist"][-1]=="q":
            print("Quit")
            break

if __name__ == "__main__":
    main()