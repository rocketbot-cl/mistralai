from mistralai import Mistral  # type: ignore
from mistral_client import set_client  # Import function to set client
from mistralai.models import SDKError  # type: ignore

# Global variable to store connection
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

    try:
        # Initialize the Mistral client and store it globally
        client = Mistral(api_key=api_key)

        try:
            # Test the connection by listing models
            models_list = client.models.list()

            # Validate that the response contains models
            if hasattr(models_list, 'data') and models_list.data:
                print("Models found successfully.")
            else:
                raise Exception("No models found in response. Please verify your connection or API key.")

            # Store the client globally
            set_client(client)

            # If successful, set the result variable to True
            SetVar(result_var, True)

        except SDKError as sdk_error:
            if "Status 401" in str(sdk_error):
                raise Exception("Invalid or expired API key. Please check your credentials and try again.")
            raise Exception(f"Error connecting to Mistral AI: {str(sdk_error)}")

    except Exception as e:
        # On failure, set the result variable to False and raise the exception
        SetVar(result_var, False)
        PrintException()
        raise e