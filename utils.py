from diffusers import StableDiffusionPipeline
from transformers import pipeline
import torch

# Configuración para cargar el modelo de Stable Diffusion
def generate_image(prompt: str, model_name = "CompVis/stable-diffusion-v1-4"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Cargar el modelo de Stable Diffusion
    pipe = StableDiffusionPipeline.from_pretrained(model_name)
    #pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
    pipe = pipe.to(device)
    
    # Generar la imagen
    image = pipe(prompt).images[0]
    return image

def classify_image(image):
    # Cargar el modelo de clasificación
    classifier = pipeline("image-classification", model="microsoft/resnet-50")
    
    # Clasificar la imagen
    result = classifier(image)
    return result
