"""
GameCGOperator — top-level operator for the game CG generation pipeline.

Loads all required models once and exposes high-level pipeline methods.
Internal logic is delegated to funcs/*.py.

Typical usage:
    op    = GameCGOperator(cfg)
    board = op.gen_storyboard(script)
    clips = [op.gen_cg_video(shot, character) for shot in board]
    final = op.compose_cg(clips, output_path="output/final.mp4")
"""

from models.reasoning.base import ReasoningModel
from models.gen_video.base import GenVideoModel
from operators.gen_game_cg.funcs.gen_storyboard import gen_storyboard
from operators.gen_game_cg.funcs.gen_cg_video import gen_cg_video
from operators.gen_game_cg.funcs.compose_cg import compose_cg


class GameCGOperator:
    """Orchestrates the full game CG generation pipeline."""

    def __init__(self, cfg: dict):
        """
        Args:
            cfg: Config dict with model paths, e.g.
                 {
                   "reasoning_model":  "/path/to/qwen-vl",
                   "gen_video_model":  "/path/to/video-gen",
                   "device":           "cuda",
                 }
        """
        self.cfg = cfg
        self.reasoning_model = ReasoningModel(cfg["reasoning_model"], device=cfg.get("device", "cuda"))
        self.gen_video_model = GenVideoModel(cfg["gen_video_model"], device=cfg.get("device", "cuda"))

    def gen_storyboard(self, script: str) -> list:
        """Step 1: Generate storyboard from script."""
        return gen_storyboard(script, self.reasoning_model)

    def gen_cg_video(self, shot: dict, character) -> str:
        """Step 2: Generate CG clip for one shot."""
        return gen_cg_video(shot, character, self.gen_video_model)

    def compose_cg(self, clip_paths: list, output_path: str) -> str:
        """Step 3: Compose clips into final video."""
        return compose_cg(clip_paths, output_path)

    def run(self, script: str, character, output_path: str = "output/cg_final.mp4") -> str:
        """Run full pipeline end-to-end."""
        board = self.gen_storyboard(script)
        clips = [self.gen_cg_video(shot, character) for shot in board]
        return self.compose_cg(clips, output_path)
