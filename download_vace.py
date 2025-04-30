from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("ali-vilab/VACE-Wan2.1-1.3B-Preview")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
