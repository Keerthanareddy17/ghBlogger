from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import Runnable
from typing import TypedDict, List, Dict, Optional

from agents import get_ingestor_agent, get_writer_agent, get_reviewer_agent, get_refiner_agent

class GraphState(TypedDict):
    repo_url: str
    files: Optional[List[Dict]]  # from fetcher
    summary: Optional[str]       # from ingestor
    draft_blog: Optional[str]    # from writer
    suggestions: Optional[str]   # from reviewer
    final_blog: Optional[str]    # from refiner

def ingestor_node(state: GraphState) -> GraphState:
    agent = get_ingestor_agent()
    summary = agent.invoke({"input": str(state["files"])})["text"]
    return {**state, "summary": summary}

def writer_node(state: GraphState) -> GraphState:
    agent = get_writer_agent()
    blog = agent.invoke({"summary": state["summary"]})["text"]
    return {**state, "draft_blog": blog}

def reviewer_node(state: GraphState) -> GraphState:
    agent = get_reviewer_agent()
    suggestions = agent.invoke({"blog": state["draft_blog"]})["text"]
    return {**state, "suggestions": suggestions}

def refiner_node(state: GraphState) -> GraphState:
    agent = get_refiner_agent()
    final = agent.invoke({
        "blog": state["draft_blog"],
        "suggestions": state["suggestions"]
    })["text"]
    return {**state, "final_blog": final}

def build_blog_graph() -> Runnable:
    graph = StateGraph(GraphState)

    # Add each step as a node
    graph.add_node("ingestor", ingestor_node)
    graph.add_node("writer", writer_node)
    graph.add_node("reviewer", reviewer_node)
    graph.add_node("refiner", refiner_node)

    # Edges between nodes
    graph.set_entry_point("ingestor")
    graph.add_edge("ingestor", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", "refiner")
    graph.add_edge("refiner", END)

    return graph.compile()

app = build_blog_graph()