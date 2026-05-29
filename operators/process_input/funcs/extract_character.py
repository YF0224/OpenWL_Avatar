"""
extract_character.py — Extract structured character attributes from image + text inputs.

Uses a vision-language model (e.g. Qwen-VL) to infer character attributes
that downstream generation models can use.

Input:
    image       : PIL.Image    — reference character image
    description : str          — optional user-provided text description
    model       : ReasoningModel — loaded VLM

Output:
    dict with keys:
        "name"        : str        — character name (if inferable)
        "description" : str        — enriched character description
        "style"       : str        — art style
        "extra_props" : list[str]  — props / accessories
"""

from PIL import Image


def extract_character(image: Image.Image, description: str, model) -> dict:
    """
    Extract structured character attributes from image and text.

    Args:
        image:       Reference character image.
        description: User-provided text description (can be empty).
        model:       Loaded ReasoningModel (VLM) instance.

    Returns:
        Dict with keys: name, description, style, extra_props.
    """
    raise NotImplementedError
