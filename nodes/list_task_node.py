from .base_node import BaseNode


class TaskList(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"task-1": ("CREWAI_TASK",)}}

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("CREWAI_TASK",)
    RETURN_NAMES = ("task",)

    FUNCTION = "create_list"
