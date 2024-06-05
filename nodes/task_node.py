from .base_node import BaseNode
from crewai import Task


class TaskNode(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "description": ("STRING", {
                   "multiline": True, "default": ""
                }),
            },
            "optional": {
                "expected_output": ("STRING", {
                    "multiline": True, "default": ""
                }),
                "agent": ("CREWAI_AGENT",),
            }
        }

    RETURN_TYPES = ("CREWAI_TASK",)
    RETURN_NAMES = ("task",)
    FUNCTION = "create_task"

    def create_task(self, description, expected_output, agent):
        task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )
        return (task,)
