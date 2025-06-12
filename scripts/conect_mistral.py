from mistralai import Mistral  # type: ignore
from mistral_client import set_client  # Importar la función para establecer el cliente

# Variable global para almacenar la conexión
global mod_model_Mistral

try:
    if not mod_model_Mistral:  # type: ignore
        mod_model_Mistral = None
except NameError:
    mod_model_Mistral = None


def connect_to_mistral(api_key, result_var, SetVar, PrintException):
    """
    Connect to Mistral AI using the official SDK and store the connection globally.

    :param api_key: API key to authenticate with Mistral AI.
    :param result_var: Name of the variable to store the result.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    global mod_model_Mistral

    # Validate that api_key and result_var are provided
    if not api_key:
        raise Exception("API key is missing. Please provide a valid API key.")
    if not result_var:
        raise Exception("Result variable is not defined. Please define a variable to store the result.")

    try:
        # Initialize the Mistral client and store it globally
        client = Mistral(api_key=api_key)

        # Test the connection by listing models
        models_list = client.models.list()

        # Validate that the response contains models
        if hasattr(models_list, 'data') and models_list.data:
            print("Se encontraron los modelos.")
        else:
            raise Exception("No se encontraron modelos en la respuesta. Verifica la conexión o el API key.")

        # Store the client globally
        set_client(client)

        # If successful, set the result variable to True
        SetVar(result_var, True)

    except Exception as e:
        # On failure, set the result variable to False and raise the exception
        SetVar(result_var, False)
        PrintException()
        raise e