from crewai import Agent

class AgentNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "role": ("STRING", {"default": ""}),
                "goal": ("STRING", {"default": ""}),
                "backstory": ("STRING", {"default": ""}),
                "verbose": ("BOOL", {"default": False}),
                "allow_delegation": ("BOOL", {"default": False}),
            },
        }

    RETURN_TYPES = ("AGENT",)
    FUNCTION = "create_agent"
    CATEGORY = "📎CrewAi"

    def create_agent(self, role, goal, backstory, verbose, allow_delegation):
       
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=verbose,
            allow_delegation=allow_delegation
        )
        return (agent,)
