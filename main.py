import torch
from torch import autocast
from diffusers.models import AutoencoderKL
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("openjourney/openjourney", use_auth_token=True)


prompt = "painting of a building in a stunning landscape"
prompt = f"mdjrny-v4 style {prompt}"

with autocast("cpu"):
  image = pipe(prompt=prompt, num_inference_steps=100, width=512, height=512, guidance_scale=15).images[0]
  
image.save("image.png")