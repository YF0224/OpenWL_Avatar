"""
preprocess_image.py — Load, validate, and normalize input images.

Input:
    image_path : str          — path to an input image file

Output:
    PIL.Image (RGB or RGBA)   — preprocessed image ready for downstream models
"""

from PIL import Image


def preprocess_image(image_path: str, size: int = 1024, mode: str = "RGB") -> Image.Image:
    """
    Load and preprocess an input image.

    Args:
        image_path: Path to the input image.
        size:       Target size (both width and height); image is padded to square then resized.
        mode:       Output mode, "RGB" or "RGBA".

    Returns:
        Preprocessed PIL image.
    """
    raise NotImplementedError
