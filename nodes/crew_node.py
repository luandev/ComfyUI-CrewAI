from .base_node import BaseNode
from crewai import Crew, Process

class CrewNode(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "tasks": ("TASK", {"default": []}),
            },
            "optional": {
                "topic": ("STRING", {"forceInput": False, "multiline": True,"default": ""}),
                "agents": ("AGENT", {"forceInput": False, "default": []}),
                "process": ("STRING", {"default": "sequential", "choices": ["sequential", "hierarchical"]}),
            },
        }
    INPUT_IS_LIST = (True, True, False, False)
    RETURN_TYPES = ("STRING",)
    FUNCTION = "create_crew"

    def create_crew(self, tasks, process, topic="", agents=[],):
        process_type = Process.sequential if process[0] == "sequential"  else Process.hierarchical
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=process_type,
            topic=topic,
        )
        
        result = crew.kickoff(inputs={'topic': topic})
        print("\n\n📎Crew AI - result", result)       
        return (result,)

