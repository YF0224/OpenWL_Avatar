"""
compose_cg.py — Compose individual CG video clips into a final sequence.

Input:
    clip_paths  : list[str]    — ordered list of video clip paths
    output_path : str          — output path for the final video (.mp4)

Output:
    output_path : str          — path to the composed final video
"""


def compose_cg(clip_paths: list, output_path: str) -> str:
    """
    Concatenate CG video clips into a single final sequence.

    Args:
        clip_paths:  Ordered list of .mp4 clip paths.
        output_path: Destination path for the final composed video.

    Returns:
        Path to the final composed video.
    """
    raise NotImplementedError
