"""
Test: Game CG generation pipeline (storyboard → clip → compose)
"""

import sys
sys.path.insert(0, ".")

from PIL import Image
from operators.gen_game_cg.operator import GameCGOperator

CFG = {
    "reasoning_model": "Qwen/Qwen3.5-9B",
    "gen_video_model": "Lightricks/LTX-2.3",
    "device":          "cuda",
}

if __name__ == "__main__":
    script    = "A straw hat pirate charges through a storm, unleashing a powerful gear attack."
    character = Image.open("assets/luffy.jpg")

    op = GameCGOperator(CFG)

    # Step-by-step
    board = op.gen_storyboard(script)
    print(f"Storyboard: {board}")

    clips = [op.gen_cg_video(shot, character) for shot in board]
    final = op.compose_cg(clips, output_path="output/luffy_cg.mp4")
    print(f"Final CG: {final}")

    # Or run full pipeline at once
    # final = op.run(script, character, output_path="output/luffy_cg.mp4")
