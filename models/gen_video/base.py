"""
GenVideoModel — base wrapper for video generation models.
"""

from PIL import Image


class GenVideoModel:
    """Base wrapper for video generation models (e.g. Kling, HunyuanVideo)."""

    def __init__(self, model_path: str, device: str = "cuda"):
        self.model_path = model_path
        self.device = device
        self.pipeline = None  # lazy-load

    def _load(self):
        if self.pipeline is None:
            raise NotImplementedError("GenVideoModel pipeline import not yet configured.")

    def generate(self, prompt: str, reference_image: Image.Image = None,
                 duration_sec: float = 3.0, output_path: str = "output.mp4") -> str:
        """
        Generate a video clip.

        Args:
            prompt:          Text prompt describing the video.
            reference_image: Optional reference character image.
            duration_sec:    Target duration in seconds.
            output_path:     Path to save the output .mp4.

        Returns:
            Path to the saved video file.
        """
        self._load()
        raise NotImplementedError
