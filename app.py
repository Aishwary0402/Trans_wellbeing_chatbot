from graph_builder import build_graph
from langchain_core.messages import HumanMessage

def main():
    print("🌈 Trans Mental Well-being Chatbot")
    print("Type 'exit' to quit\n")

    graph = build_graph()

    state = {
        "messages": [],
        "user_emotion": ""
    }

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        state["messages"].append(HumanMessage(content=user_input))

        result = graph.invoke(state)

        ai_message = result["messages"][-1]

        print("\nTherapist:", ai_message.content, "\n")

        state = result


if __name__ == "__main__":
    main()
