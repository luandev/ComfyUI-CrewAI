from crewai import Crew, Process

class CrewNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "agents": ("AGENT", {"default": []}),
                "tasks": ("TASK", {"default": []}),
                "process": ("STRING", {"default": "sequential", "choices": ["sequential", "hierarchical"]}),
                "topic": ("STRING", {"default": ""}),
            },
        }
    INPUT_IS_LIST = (True, True, False, False)
    RETURN_TYPES = ("STRING",)
    FUNCTION = "create_crew"
    CATEGORY = "📎CrewAi"

    def create_crew(self, agents, tasks, process, topic):
        process_type = Process.sequential if process == "sequential" else Process.hierarchical
        print("\n\n📎Crew AI - input", agents, tasks, process, topic)
        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=process_type
        )
        result = crew.kickoff(inputs={'topic': topic})
        print("\n\n📎Crew AI - result", result)       
        return (result,)

