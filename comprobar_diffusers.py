from diffusers import StableDiffusionPipeline

model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
print("Modelo cargado con éxito")
