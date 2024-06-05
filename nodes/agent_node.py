from crewai import Agent


class AgentNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "role": ("STRING", {
                    "forceInput": True, "multiline": True, "default": ""
                }),
                "goal": ("STRING", {
                    "forceInput": True, "multiline": True, "default": ""
                }),
                "backstory": ("STRING", {
                    "forceInput": True, "multiline": True, "default": ""
                }),
            },
            "optional": {
                "LLM": ("CAI_LLM",),
                "verbose": ("BOOL", {"default": False}),
                "allow_delegation": ("BOOL", {"default": True}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("CAI_AGENT",)
    FUNCTION = "create_agent"
    CATEGORY = "📎CrewAi"

    def create_agent(
                    self,
                    role,
                    goal,
                    backstory,
                    llm=None,
                    verbose=False,
                    allow_delegation=True,
    ):
        agent_kwargs = {
            "role": role,
            "goal": goal,
            "backstory": backstory,
            "verbose": verbose,
            "allow_delegation": allow_delegation,
        }

        if llm is not None:
            agent_kwargs["llm"] = llm

        print("\n\n📎", agent_kwargs, "\n\n")
        agent = Agent(**agent_kwargs)
        return (agent,)
