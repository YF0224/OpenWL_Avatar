"""
ReasoningModel — base wrapper for vision-language / reasoning models (e.g. Qwen-VL).
"""

from PIL import Image


class ReasoningModel:
    """Base wrapper for VLM / reasoning models."""

    def __init__(self, model_path: str, device: str = "cuda"):
        self.model_path = model_path
        self.device = device
        self.model = None  # lazy-load

    def _load(self):
        if self.model is None:
            raise NotImplementedError("ReasoningModel pipeline import not yet configured.")

    def infer(self, prompt: str, image: Image.Image = None) -> str:
        """
        Run text (+ optional image) inference.

        Args:
            prompt: Text prompt.
            image:  Optional PIL image input.

        Returns:
            Model response string.
        """
        self._load()
        raise NotImplementedError
