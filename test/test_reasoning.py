"""
Test: Input analysis → skill design → T-pose generation

Pipeline:
    1. InputProcessor: parse text description, extract character traits
    2. ReasoningModel: analyze character and design skill/ability set
    3. UEAvatarOperator.gen_tpose: generate T-pose RGBA image
"""

import sys
sys.path.insert(0, ".")

from PIL import Image
from operators.process_input.operator import InputProcessor
from operators.gen_ue_avatar.operator import UEAvatarOperator

INPUT_CFG = {
    "reasoning_model": "Qwen/Qwen3.5-9B",
    "device": "cuda",
}

UE_CFG = {
    "gen_image_model": "Qwen/Qwen-Image-Edit-2509",
    "gen_3d_model":    "microsoft/TRELLIS.2-4B",
    "device":          "cuda",
}

if __name__ == "__main__":
    ref_image   = Image.open("assets/luffy.jpg")
    description = "Monkey D. Luffy, straw hat pirate with rubber powers, can stretch body infinitely"

    # Step 1: Parse and analyze input
    input_processor = InputProcessor(INPUT_CFG)
    parsed = input_processor.run(ref_image, description)
    print(f"Parsed input: {parsed}")

    # Step 2: T-pose generation based on analyzed character
    ue_op = UEAvatarOperator(UE_CFG)
    tpose = ue_op.gen_tpose(ref_image, description=parsed.get("description", description))
    tpose.save("output/luffy_tpose.png")
    print("T-pose saved to output/luffy_tpose.png")
