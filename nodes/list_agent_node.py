from .base_node import BaseNode


class AgentList(BaseNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"agent-1": ("CREWAI_AGENT",)}}

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("CREWAI_AGENT",)
    RETURN_NAMES = ("agent",)

    FUNCTION = "create_list"
