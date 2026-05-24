from langchain_community.agent_toolkits import GmailToolkit
from langchain.tools import tool

toolkit = GmailToolkit()
gmail_tools = toolkit.get_tools()

search_tool = next(t for t in gmail_tools if t.name == "search_gmail")
draft_tool = next(t for t in gmail_tools if t.name == "create_gmail_draft")


@tool
def search_email_subjects(query: str) -> str:
    """Search Gmail and return email snippets."""

    emails = search_tool.invoke({"query": query})

    cleaned = []

    for email in emails[:10]:
        cleaned.append(email.get("snippet", "No snippet"))

    return "\n".join(cleaned)


@tool
def create_draft(to: str, subject: str, message: str) -> str:
    """Create Gmail draft."""

    result = draft_tool.invoke({
        "to": [to],
        "subject": subject,
        "message": message
    })

    return str(result)


tools = [
    search_email_subjects,
    create_draft
]