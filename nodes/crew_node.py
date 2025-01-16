from .base_node import BaseNode
from crewai import Crew, Process


class CrewNode(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "tasks": ("CREWAI_TASK", {"default": []}),
            },
            "optional": {
                "verbose": ("BOOLEAN", {"default": False}),
                "agents": ("CREWAI_AGENT", {"forceInput": False, "default": []}),
                "manager_agent": ("CREWAI_AGENT", {"forceInput": False, "default": []}),
                "topic": ("STRING", {
                    "forceInput": False, "multiline": True, "default": ""
                }),
                "isSequential": ("BOOLEAN", {"default": True}),
            },
        }
    INPUT_IS_LIST = (True, True, False, False)
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "create_crew"

    def create_crew(self,
                    tasks=[],
                    isSequential: bool = True,
                    topic="", agents=[],
                    verbose: bool = False,
                    manager_agent=None):
        # Determine the process type
        process_type = Process.sequential if isSequential[0] else Process.hierarchical

        # Handle manager_agent input
        if isinstance(manager_agent, list) and manager_agent:
            manager_agent = manager_agent[0]  # Take the first element if it's a list
        elif not manager_agent:
            manager_agent = None  # Ensure it's None if empty or not provided

        # Prepare arguments for the Crew instance
        crew_kwargs = {
            "agents": agents,
            "tasks": tasks,
            "process": process_type,
            "topic": topic,
            "verbose": verbose[0],
        }

        # Add manager_agent only if it's valid
        if manager_agent:
            crew_kwargs["manager_agent"] = manager_agent

        if verbose[0]:
            print("\n\n📎", crew_kwargs, "\n\n")

        # Create the Crew instance
        crew = Crew(**crew_kwargs)

        # Kick off the process and capture the result
        try:
            result = crew.kickoff(inputs={'topic': topic})
            positive_prompt = result["positive_prompt"]
            negative_prompt = result["negative_prompt"]

            if verbose[0]:
                print("Positive prompt:", positive_prompt)
                print("Negative prompt:", negative_prompt)

        except IndexError as e:
            print("Error during processing:", e)

        return (positive_prompt, negative_prompt)
