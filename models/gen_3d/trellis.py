"""
TrellisModel — wrapper for Trellis image-to-3D model.
"""

from PIL import Image


class TrellisModel:
    """Thin wrapper around Trellis image-to-3D pipeline."""

    def __init__(self, model_path: str, device: str = "cuda"):
        self.model_path = model_path
        self.device = device
        self.pipeline = None  # lazy-load on first call

    def _load(self):
        if self.pipeline is None:
            # TODO: replace with actual Trellis pipeline import
            raise NotImplementedError("Trellis pipeline import not yet configured.")

    def image_to_3d(self, image: Image.Image, output_path: str) -> str:
        """
        Run image-to-3D inference and export mesh.

        Args:
            image:       RGBA PIL image (1024x1024, transparent background).
            output_path: Path to save the output .glb mesh.

        Returns:
            Path to the saved .glb mesh.
        """
        self._load()
        raise NotImplementedError
