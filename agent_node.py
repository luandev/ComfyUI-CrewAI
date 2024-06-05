from crewai import Agent

class AgentNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "role": ("STRING", {"forceInput": True, "multiline": True, "default": ""}),
                "goal": ("STRING", {"forceInput": True, "multiline": True, "default": ""}),
                "backstory": ("STRING", {"forceInput": True, "multiline": True, "default": ""}),
            },
            "optional": {
                "verbose": ("BOOL", {"default": False}),
                "allow_delegation": ("BOOL", { "default": True}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("AGENT",)
    FUNCTION = "create_agent"
    CATEGORY = "📎CrewAi"

    def create_agent(self, role, goal, backstory, verbose=False, allow_delegation=True):
       
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=verbose,
            allow_delegation=allow_delegation
        )
        return (agent,)
