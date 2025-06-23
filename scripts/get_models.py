from mistral_client import get_client  # Import function to get client
import traceback  # For capturing error traces


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
            raise Exception("You must connect to Mistral AI before using this command. Please run the connection module first.")

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
        print("Error getting model list from Mistral AI:")
        print(traceback.format_exc())  # Print full error trace
        if PrintException:
            PrintException()
        raise e