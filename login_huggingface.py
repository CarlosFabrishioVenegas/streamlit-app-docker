from huggingface_hub import login, HfApi, HfFolder
from huggingface_hub.errors import HFValidationError

token = "Aqui colocar un token de la cuenta"

try:

    login(token)
    
    # Verificamos si el token es válido
    api = HfApi()
    user_info = api.whoami()
    
    # Si no hubo excepciones, el inicio de sesión fue exitoso
    print("Inicio de sesión exitoso en Hugging Face.")
except HFValidationError as e:
    # Si hubo un error con el token, mostramos el mensaje
    print(f"Error: Token no válido. {e}")
except Exception as e:
    # Si ocurrió cualquier otro error, lo mostramos
    print(f"Error: Hubo un problema al intentar iniciar sesión. {e}")