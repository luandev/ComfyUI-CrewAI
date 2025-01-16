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
                "topic": ("STRING", {
                    "forceInput": False, "multiline": True, "default": ""
                }),
                "process": ("STRING", {
                    "default": "sequential",
                    "choices": ["sequential", "hierarchical"]
                }),
            },
        }
    INPUT_IS_LIST = (True, True, False, False)
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("postive", "negative")
    FUNCTION = "create_crew"

    def create_crew(self, tasks, process, topic="", agents=[], verbose=False):
        # Determine the process type
        isSequential: bool = process[0] == "sequential"
        process_type = Process.sequential if isSequential else Process.hierarchical
        result = ""
        print("\n\n📎", verbose, "\n\n")
        # Create the Crew instance
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=process_type,
            topic=topic,
        )

        if verbose:
            print("\n\n📎", crew, "\n\n")

        # Kick off the process and capture the result
        try:
            result = crew.kickoff(inputs={'topic': topic})
            positive_prompt = result["positive_prompt"]
            negative_prompt = result["negative_prompt"]

            if verbose:
                print("Positive prompt:", positive_prompt)
                print("Negative prompt:", negative_prompt)

        except IndexError as e:
            print("Error during processing:", e)

        return (positive_prompt, negative_prompt)
