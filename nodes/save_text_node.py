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
                "text": ("STRING", {"multiline": True}),
                "filename_prefix": ("STRING", {"default": "output"}),
                "save_metadata": (["disabled", "enabled"], {"default": "enabled"}),
            }
        }

    RETURN_TYPES = ("STRING",)  # Indicates the node outputs text to the UI
    FUNCTION = "save_and_display_text"
    OUTPUT_NODE = True
    CATEGORY = "Custom Nodes"

    def save_and_display_text(self, text, filename_prefix, save_metadata):
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.txt"

        # Save text to file
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

        # Return text for display in the UI
        return (f"Saved Text:\n{text}",)  # Display the full text or a preview


# Register the node in ComfyUI
NODE_CLASS_MAPPINGS = {
    "SaveAndDisplayTextNode": DisplayText,
}
