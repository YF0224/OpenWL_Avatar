"""
gen_storyboard.py — Generate a storyboard from a script or scene description.

Input:
    script      : str          — text script or scene description
    model       : ReasoningModel — loaded reasoning/LLM model

Output:
    storyboard  : list[dict]   — list of shots, each with keys:
                                 {"shot_id", "description", "duration_sec"}
"""


def gen_storyboard(script: str, model) -> list:
    """
    Generate a shot-by-shot storyboard from a script.

    Args:
        script: Text script or scene description.
        model:  Loaded ReasoningModel instance.

    Returns:
        List of shot dicts: [{"shot_id": 0, "description": "...", "duration_sec": 3}, ...]
    """
    raise NotImplementedError
