class BaseNode:
    CATEGORY = "📎CrewAI"

    def create_list(self, **kwargs):
        list = []

        # Collect all agents from kwargs dynamically
        for _k, v in kwargs.items():
            if v is not None:
                list.append(v)

        return (list,)
