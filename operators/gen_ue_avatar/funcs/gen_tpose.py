"""
gen_tpose.py — Generate a game-CG T-pose RGBA image from a reference character image.

Input:
    ref_image   : PIL.Image  — reference character image (any background)
    description : str        — optional text description of the character
    model       : GenImageModel — loaded image-editing model (e.g. Qwen-Image-Edit)

Output:
    PIL.Image (RGBA, 1024x1024) — character in T-pose, transparent background
"""

from PIL import Image


def gen_tpose(ref_image: Image.Image, description: str, model) -> Image.Image:
    """
    Generate a T-pose RGBA image from a reference character image.

    Args:
        ref_image:   Reference PIL image of the character.
        description: Short text description of the character (can be empty).
        model:       Loaded GenImageModel instance.

    Returns:
        RGBA PIL image (1024x1024) with transparent background.
    """
    raise NotImplementedError
