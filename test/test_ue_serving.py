"""
Test: UE avatar generation pipeline (gen_tpose → gen_3d_avatar → import_to_ue)
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
    ref_image   = Image.open("assets/luffy.jpg")
    description = "Monkey D. Luffy, straw hat pirate with rubber powers"

    op = UEAvatarOperator(CFG)

    # Step-by-step
    tpose  = op.gen_tpose(ref_image, description)
    tpose.save("output/luffy_tpose.png")
    print("T-pose saved.")

    mesh = op.gen_3d_avatar(tpose)
    print(f"3D mesh: {mesh}")

    # Or run full pipeline at once
    # result = op.run(ref_image, description, motion_desc="walk forward")
