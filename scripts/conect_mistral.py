from mistralai import Mistral, models  # type: ignore

def connect_to_mistral(api_key, result_var, SetVar, PrintException):
    """
    Connect to Mistral AI using the official SDK and validate the connection.

    :param api_key: API key to authenticate with Mistral AI.
    :param result_var: Name of the variable to store the result.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    # Validate that api_key and result_var are provided
    if not api_key:
        raise Exception("API key is missing. Please provide a valid API key.")
    if not result_var:
        raise Exception("Result variable is not defined. Please define a variable to store the result.")

    try:
        # Create client using the official SDK
        client = Mistral(api_key=api_key)

        # List models as a connection test
        models_list = client.models.list()

        # If we reach here, the connection was successful (status code 200)
        SetVar(result_var, True)

    except models.HTTPValidationError as e:
        # Error 422 - Validation error
        error_msg = "Validation error in the request"
        if hasattr(e, 'data'):
            error_msg += f": {str(e.data)}"
        SetVar(result_var, False)
        raise Exception(error_msg)

    except models.SDKError as e:
        # Handle other HTTP errors (4XX and 5XX)
        status_code = getattr(e, 'status_code', 'unknown')
        error_msg = f"Server error (code {status_code})"

        if status_code in [401, '401']:
            error_msg = "Authentication error: The API key is invalid or unauthorized."
        elif status_code in ['429', 429]:
            error_msg = "Too many requests. Please wait a moment and try again."
        elif str(status_code).startswith('4'):
            error_msg = f"Client error (code {status_code}). Please check your request."
        elif str(status_code).startswith('5'):
            error_msg = "Mistral server error. Please try again later."

        SetVar(result_var, False)
        raise Exception(error_msg)

    except Exception as e:
        # Other unexpected errors
        error_msg = f"Unexpected error: {str(e)}"
        SetVar(result_var, False)
        raise Exception(error_msg)