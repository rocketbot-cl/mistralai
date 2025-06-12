# mistral_service.py

from typing import Any

try:
    from module import GetVar  # type: ignore # Rocketbot
except:
    def GetVar(var): return None  # Para testing fuera de Rocketbot


def get_mistral_client() -> Any:
    """
    Retorna el cliente Mistral ya conectado. 
    Lanza excepción si no se ejecutó antes el módulo de conexión.
    """
    client = GetVar("mistral_client")
    if not client:
        raise Exception(
            "Debe ejecutar primero el comando 'Conectar con Mistral'.")
    return client
