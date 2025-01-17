import os
import json
from datetime import datetime


class DisplayText:
    def __init__(self):
        self.output_dir = "outputs/text_outputs"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "output": ("STRING", {
                    "multiline": True, "default": ""
                }),
                "filename_prefix": ("STRING", {"default": "output"}),
                "save_metadata": (["disabled", "enabled"], {"default": "enabled"}),
                "save_file": (["disabled", "enabled"], {"default": "enabled"}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ("STRING",)  # Indicates the node outputs text to the UI
    FUNCTION = "save_and_display_text"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    INPUT_IS_LIST = True
    CATEGORY = "Custom Nodes"

    def save_and_display_text(self,
                              text,
                              output,
                              filename_prefix,
                              save_metadata,
                              save_file,
                              unique_id=None,
                              extra_pnginfo=None):
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.txt"

        # Save text to file
        if save_file == "enabled":
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)

        # Optionally save metadata
        if save_metadata == "enabled":
            metadata_path = os.path.join(self.output_dir, f"{filename}_metadata.json")
            metadata = {
                "timestamp": timestamp,
                "filename_prefix": filename_prefix,
                "text_preview": text[:50] + "..." if len(text) > 50 else text,
            }
            with open(metadata_path, "w", encoding="utf-8") as meta_file:
                json.dump(metadata, meta_file, indent=4)

        # Update the UI
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = text

        return {"ui": {"text": text}, "result": (text,)}


# Register the node in ComfyUI
NODE_CLASS_MAPPINGS = {
    "DisplayText": DisplayText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DisplayText": "Display and save text",
}
