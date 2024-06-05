from .agent_node import AgentNode
from .task_node import TaskNode
from .crew_node import CrewNode
from .list_task_node import TaskList
from .list_agent_node import AgentList

NODE_CLASS_MAPPINGS = {
    "📎CrewAI Agent": AgentNode,
    "📎CrewAI Task": TaskNode,
    "📎CrewAI Crew": CrewNode,
    "📎CrewAI Task List": TaskList,
    "📎CrewAI Agent List": AgentList,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS"]