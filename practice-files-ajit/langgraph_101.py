from dotenv import load_dotenv
load_dotenv(".env")

from langchain_openai import ChatOpenAI, AzureChatOpenAI
llm = ChatOpenAI(model="gpt-4.1")

from langgraph.graph import MessagesState, StateGraph, END, START

def call_llm(state: MessagesState) -> MessagesState:
    """Run LLM"""
    output = llm.invoke(state["messages"])
    return {"messages": [output]}

workflow = StateGraph(MessagesState)
workflow.add_node("call_llm", call_llm)
workflow.add_edge(START, "call_llm")
workflow.add_edge("call_llm", END)
app = workflow.compile()