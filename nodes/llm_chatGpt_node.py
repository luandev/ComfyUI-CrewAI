from .base_node import BaseNode
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "NA"


class LlmChatGpt(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "forceInput": True,
                    "default": "http://localhost:11434/v1"
                }),
            },
            "optional": {
                "model": ("STRING", {
                    "forceInput": True, "default": "gpt-4o"
                }),
            }
        }

    RETURN_TYPES = ("CAI_LLM",)
    FUNCTION = "create_task"

    def create_task(self, model, api_key):
        llm = ChatOpenAI(model=model, api_key=api_key)
        return (llm,)
