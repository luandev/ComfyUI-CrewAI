class TextViewNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ()
    FUNCTION = "display_text"
    CATEGORY = "📎CrewAi"

    def display_text(self, text):
        self["widgets_values"] = [text]
        return {"ui": {"text": text}, "result": (text,)}