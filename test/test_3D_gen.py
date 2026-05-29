"""
Test: Full 3D avatar + motion generation pipeline

Pipeline:
    1. UEAvatarOperator.gen_3d_avatar: T-pose image → 3D mesh (.glb)
    2. UEAvatarOperator.gen_motion:    3D mesh → skeleton detection + motion generation
"""

import sys
sys.path.insert(0, ".")

from PIL import Image
from operators.gen_ue_avatar.operator import UEAvatarOperator

CFG = {
    "gen_image_model": "Qwen/Qwen-Image-Edit-2509",
    "gen_3d_model":    "microsoft/TRELLIS.2-4B",
    "device":          "cuda",
}

if __name__ == "__main__":
    # Assumes T-pose image already generated (run test_reasoning.py first)
    tpose = Image.open("output/luffy_tpose.png")   # RGBA 1024x1024

    op = UEAvatarOperator(CFG)

    # Step 1: T-pose → 3D mesh
    mesh = op.gen_3d_avatar(tpose)
    print(f"3D mesh: {mesh}")

    # Step 2: 3D mesh → motion
    motion = op.gen_motion(mesh, motion_desc="walk forward, then perform a gear attack")
    print(f"Motion: {motion}")

    # Or run full pipeline at once (includes gen_tpose)
    # ref = Image.open("assets/luffy.jpg")
    # result = op.run(ref, description="straw hat pirate", motion_desc="walk forward")
    # print(result)
