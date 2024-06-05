from .base_node import BaseNode


class TaskList(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"task-1": ("CAI_TASK",)}}

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("CAI_TASK",)
    FUNCTION = "create_list"
