from .nodes.llm_ollama_node import LlmOllama
from .nodes.llm_chatGpt_node import LlmChatGpt
from .nodes.llm_huggingface_node import LlmHuggingFace
from .nodes.llm_openai_node import LlmOpenai
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
    "📎CrewAI LLM OpenAI": LlmOpenai,
    "📎CrewAI LLM Hugging Face": LlmHuggingFace,
    "📎CrewAI LLM Chat GPT": LlmChatGpt,
    "📎CrewAI LLM Ollama": LlmOllama,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS"]
