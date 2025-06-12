# Variable global para almacenar la conexión
mod_model_Mistral = None

def set_client(client):
    """
    Establece el cliente global de Mistral.
    """
    global mod_model_Mistral
    mod_model_Mistral = client

def get_client():
    """
    Obtiene el cliente global de Mistral.
    """
    global mod_model_Mistral
    return mod_model_Mistral