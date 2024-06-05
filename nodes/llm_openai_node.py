from .base_node import BaseNode
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "NA"


class LlmOpenai(BaseNode):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("STRING", {
                    "forceInput": True, "default": "crewai-llama3"
                }),
                "base_url": ("STRING", {
                    "forceInput": True,
                    "default": "http://localhost:11434/v1"
                }),
            },
            "optional": {
                "api_key": ("STRING", {
                    "forceInput": True,
                    "default": "http://localhost:11434/v1"
                }),
            }
        }

    RETURN_TYPES = ("CAI_LLM",)
    FUNCTION = "create_task"

    def create_task(self, model, base_url, api_key):
        llm = ChatOpenAI(model=model, base_url=base_url, api_key=api_key)
        return (llm,)
