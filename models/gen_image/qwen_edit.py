"""
QwenEditModel — wrapper for Qwen-Image-Edit image editing model.
"""

import torch
from diffusers import QwenImageEditPlusPipeline
from PIL import Image


class QwenEditModel:
    """Thin wrapper around QwenImageEditPlusPipeline."""

    def __init__(self, model_path: str, device: str = "cuda"):
        dtype = torch.bfloat16 if (device == "cuda" and torch.cuda.is_bf16_supported()) else torch.float32
        self.pipe = QwenImageEditPlusPipeline.from_pretrained(model_path, torch_dtype=dtype).to(device)
        self.device = device

    def edit(self, image: Image.Image, prompt: str, seed: int = 42, steps: int = 40) -> Image.Image:
        """Run image editing inference."""
        with torch.inference_mode():
            result = self.pipe(
                image=[image],
                prompt=prompt,
                generator=torch.Generator(device=self.device).manual_seed(seed),
                true_cfg_scale=4.0,
                num_inference_steps=steps,
                guidance_scale=1.0,
                num_images_per_prompt=1,
            ).images[0]
        return result
