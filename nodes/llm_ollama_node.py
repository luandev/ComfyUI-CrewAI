from .base_node import BaseNode
from crewai import LLM


class LlmOllama(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("STRING", {
                    "default": "ollama/llama3.2:3b"
                }),
                "base_url": ("STRING", {
                    "default": "http://localhost:11434"
                }),
            },
        }

    RETURN_TYPES = ("CREWAI_LLM",)
    RETURN_NAMES = ("llm",)

    FUNCTION = "create_task"

    def create_task(self, model, base_url):
        llm = LLM(model=model, base_url=base_url)
        return (llm,)
