from .base_node import BaseNode
from crewai import Crew, Process

class TaskList(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        # Generate a dictionary for up to n agents dynamically
        inputs = {"required": {"task-1": ("TASK",)}}
        # for i in range(2, 101):  # Adjust the range as needed
        #     inputs["optional"] = inputs.get("optional", {})
        #     inputs["optional"][f"agent{i}"] = ("AGENT",)
        return inputs


    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("TASK",)
    FUNCTION = "create_list"

    def create_list(self, **kwargs):
        task = []

        for k, v in kwargs.items():
            task.append(v)

        return (task, )
