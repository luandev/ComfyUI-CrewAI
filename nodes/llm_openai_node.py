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
                    "default": "crewai-llama3"
                }),
                "base_url": ("STRING", {
                    "default": "http://localhost:11434/v1"
                }),
            },
            "optional": {
                "api_key": ("STRING", {
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("CREWAI_LLM",)
    RETURN_NAMES = ("llm",)

    FUNCTION = "create_task"

    def create_task(self, model, base_url, api_key):
        llm = ChatOpenAI(model=model, base_url=base_url, api_key=api_key)
        return (llm,)
