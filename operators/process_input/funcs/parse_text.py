"""
parse_text.py — Parse and normalize user text input (character description, script, etc.)

Input:
    raw_text : str   — raw user input string

Output:
    dict with keys:
        "description"  : str  — cleaned character description
        "style"        : str  — detected art style (anime / realistic / game-art)
        "extra_props"  : list — extra props / objects mentioned (e.g. ["sword", "cape"])
"""


def parse_text(raw_text: str) -> dict:
    """
    Parse and normalize a raw user text input.

    Args:
        raw_text: Raw user-provided text (character description or script).

    Returns:
        Dict with keys: description, style, extra_props.
    """
    raise NotImplementedError
