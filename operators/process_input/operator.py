"""
InputProcessor — top-level operator for user input preprocessing.

Typical usage:
    proc   = InputProcessor(cfg)
    result = proc.process(image_path, raw_text)
    # result = {"image": PIL.Image, "character": {...}}
"""

from models.reasoning.base import ReasoningModel
from operators.process_input.funcs.parse_text import parse_text
from operators.process_input.funcs.preprocess_image import preprocess_image
from operators.process_input.funcs.extract_character import extract_character


class InputProcessor:
    """Preprocesses user inputs (image + text) for downstream operators."""

    def __init__(self, cfg: dict):
        """
        Args:
            cfg: {
                   "reasoning_model": "/path/to/qwen-vl",
                   "device": "cuda",
                 }
        """
        self.cfg = cfg
        self.reasoning_model = ReasoningModel(cfg["reasoning_model"], device=cfg.get("device", "cuda"))

    def process(self, image_path: str, raw_text: str = "") -> dict:
        """
        Full preprocessing pipeline.

        Returns:
            {
              "image":     PIL.Image,         # preprocessed image
              "character": dict,              # structured character attributes
            }
        """
        image = preprocess_image(image_path)
        text_info = parse_text(raw_text) if raw_text else {}
        description = text_info.get("description", raw_text)
        character = extract_character(image, description, self.reasoning_model)
        return {"image": image, "character": character}
