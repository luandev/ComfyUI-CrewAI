from .base_node import BaseNode


class AgentList(BaseNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"agent-1": ("AGENT",)}}

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("AGENT",)
    FUNCTION = "create_list"
