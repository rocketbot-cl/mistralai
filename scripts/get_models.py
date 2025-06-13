from mistral_client import get_client  # Importar la función para obtener el cliente
import traceback  # Para capturar trazas de errores


def get_models(result_var, SetVar, PrintException):
    """
    Retrieve the list of models from the global Mistral connection and assign it to the specified variable.

    :param result_var: Name of the variable to store the models list.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    try:
        # Get the client
        client = get_client()
        if not client:
            raise Exception("Debe conectarse a Mistral AI antes de usar este comando. Ejecute primero el módulo de conexión.")

        # List models
        models_list = client.models.list()

        # Validate that the response contains models
        if hasattr(models_list, 'data') and models_list.data:
            print("Se encontraron los modelos:")
            # print(models_list.data)  # Imprime los modelos disponibles
        else:
            raise Exception("No se encontraron modelos en la respuesta. Verifica la conexión o el API key.")

        # Assign the models list to the specified Rocketbot variable
        SetVar(result_var, models_list.data)

    except Exception as e:
        # On failure, set the result variable to None and raise the exception
        SetVar(result_var, None)
        print("Error al obtener los modelos de Mistral AI:")
        print(traceback.format_exc())  # Imprime la traza completa del error
        PrintException()
        raise e