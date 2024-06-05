import os
from .agent_node import AgentNode
from .task_node import TaskNode
from .crew_node import CrewNode
from .list_task_node import TaskList
from .list_agent_node import AgentList

NODE_CLASS_MAPPINGS = {
    "CrewAI Agent Node": AgentNode,
    "CrewAI Task Node": TaskNode,
    "CrewAI Crew Node": CrewNode,
    "CrewAI TaskList Node": TaskList,
    "CrewAI AgentList Node": AgentList,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS"]