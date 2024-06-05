from .base_node import BaseNode


class AgentList(BaseNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"agent-1": ("CAI_AGENT",)}}

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("CAI_AGENT",)
    FUNCTION = "create_list"
