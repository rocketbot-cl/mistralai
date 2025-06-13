from mistral_client import get_client  # Importar la función para obtener el cliente
import traceback  # Para capturar trazas de errores


def get_models(result_var, SetVar, PrintException):
    """
    Retrieve the list of models from the global Mistral connection and assign their IDs to the specified variable.

    :param result_var: Name of the variable to store the models' IDs list.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    try:
        # Get the client
        client = get_client()
        if not client:
            raise Exception("Debe conectarse a Mistral AI antes de usar este comando. Ejecute primero el módulo de conexión.")

        # Retrieve the list of models
        response = client.models.list()

        # Extract only the IDs of the models
        model_ids = [model.id for model in response.data]

        # Debug: Print the extracted IDs
        print("DEBUG: Model IDs =", model_ids)

        # Assign the list of model IDs to the specified Rocketbot variable
        SetVar(result_var, model_ids)

    except Exception as e:
        # On failure, set the result variable to None and raise the exception
        SetVar(result_var, None)
        print("Error al obtener la lista de modelos de Mistral AI:")
        print(traceback.format_exc())  # Imprime la traza completa del error
        if PrintException:
            PrintException()
        raise e