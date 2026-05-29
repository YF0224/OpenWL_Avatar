"""
gen_cg_video.py — Generate a CG video clip for a single storyboard shot.

Input:
    shot        : dict         — shot dict from gen_storyboard()
    character   : PIL.Image    — character reference image
    model       : GenVideoModel — loaded video generation model

Output:
    video_path  : str          — path to the generated video clip (.mp4)
"""

from PIL import Image


def gen_cg_video(shot: dict, character: Image.Image, model) -> str:
    """
    Generate a CG video clip for one storyboard shot.

    Args:
        shot:      Shot dict with keys: shot_id, description, duration_sec.
        character: Character reference PIL image.
        model:     Loaded GenVideoModel instance.

    Returns:
        Path to the generated .mp4 video clip.
    """
    raise NotImplementedError
