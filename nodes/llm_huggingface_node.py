from .base_node import BaseNode
from crewai import LLM

import os


class LlmHuggingFace(BaseNode):
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
                    "default": os.getenv("OPENAI_API_KEY")
                }),
            }
        }

    RETURN_TYPES = ("CREWAI_LLM",)
    RETURN_NAMES = ("llm",)

    FUNCTION = "create_task"

    def create_task(self, base_url, api_key, task, max_new_tokens):
        llm = LLM(
            endpoint_url=base_url,
            huggingfacehub_api_token=api_key,
            task=task,
            max_new_tokens=max_new_tokens
        )
        return (llm,)
