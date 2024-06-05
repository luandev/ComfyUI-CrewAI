from crewai import Task

class TaskNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "description": ("STRING", {"default": ""}),
                "expected_output": ("STRING", {"default": ""}),
                "agent": ("AGENT",),
            },
        }

    RETURN_TYPES = ("TASK",)
    FUNCTION = "create_task"
    CATEGORY = "📎CrewAi"

    def create_task(self, description, expected_output, agent):
        task = Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )
        return (task,)

