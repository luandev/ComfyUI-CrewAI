class AgentList:
    @classmethod
    def INPUT_TYPES(cls):
        # Generate a dictionary for up to n agents dynamically
        inputs = {"required": {"agent-1": ("AGENT",)}}
        # for i in range(2, 101):  # Adjust the range as needed
        #     inputs["optional"] = inputs.get("optional", {})
        #     inputs["optional"][f"agent{i}"] = ("AGENT",)
        return inputs

    OUTPUT_IS_LIST = (True,)
    RETURN_TYPES = ("AGENT",)
    FUNCTION = "create_list"
    CATEGORY = "📎CrewAi"

    def create_list(self, **kwargs):
        agents = []

        # Collect all agents from kwargs dynamically
        for key, value in kwargs.items():
            if value is not None:
                agents.append(value)

        return (agents,)