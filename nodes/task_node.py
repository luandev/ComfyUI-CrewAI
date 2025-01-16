from .base_node import BaseNode
from crewai import Task
from pydantic import BaseModel


class PromptOutput(BaseModel):
    positive_prompt: str
    negative_prompt: str


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
                "agent": ("CREWAI_AGENT", {"forceInput": False}),
            }
        }

    RETURN_TYPES = ("CREWAI_TASK",)
    RETURN_NAMES = ("task",)
    FUNCTION = "create_task"

    def create_task(self, description, expected_output="", agent=None):
        # Create the Task object, only setting the agent if provided
        task_kwargs = {
            "description": description,
            "expected_output": expected_output,
            "output_json": PromptOutput
        }
        if agent is not None:
            task_kwargs["agent"] = agent

        print("\n\n📎", task_kwargs, "\n\n")

        task = Task(**task_kwargs)
        return (task,)
