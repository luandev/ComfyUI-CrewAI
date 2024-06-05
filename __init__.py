# from .textview_node import TextViewNode
from .nodes.agent_node import AgentNode
from .nodes.task_node import TaskNode
from .nodes.crew_node import CrewNode
from .nodes.list_task_node import TaskList
from .nodes.list_agent_node import AgentList

NODE_CLASS_MAPPINGS = {
    "📎CrewAI Agent": AgentNode,
    "📎CrewAI Task": TaskNode,
    "📎CrewAI Crew": CrewNode,
    "📎CrewAI Task List": TaskList,
    "📎CrewAI Agent List": AgentList,
    # "📎CrewAI View Text": TextViewNode, (WIP)
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS"]