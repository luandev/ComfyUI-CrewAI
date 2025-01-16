from .base_node import BaseNode
from crewai import LLM
import os


class LlmChatGpt(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": os.getenv("OPENAI_API_KEY")}),
            },
            "optional": {
                "model": ("STRING", {
                    "default": "gpt-4o"
                }),
            }
        }

    RETURN_TYPES = ("CREWAI_LLM",)
    RETURN_NAMES = ("llm",)

    FUNCTION = "create_task"

    def create_task(self, model, api_key):
        llm = LLM(model=model, api_key=api_key)
        return (llm,)
