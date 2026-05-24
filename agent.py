from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from gmail import tools

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=tools
)

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        break

    try:
        response = agent.invoke(
            {
                "messages": [
                    ("user", user_prompt)
                ]
            }
        )

        print("\n===== AGENT RESPONSE =====")

        for msg in response["messages"]:
            print(f"\n[{type(msg).__name__}]")

            if hasattr(msg, "content"):
                print(msg.content)

        print("\n==========================\n")

    except Exception as e:
        print(f"\nError: {e}\n")