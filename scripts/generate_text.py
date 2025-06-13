from mistral_client import get_client  # Importar la función para obtener el cliente
import traceback  # Para capturar trazas de errores


def generate_text(prompt, model, result_var, temperature, max_tokens, stop_sequence, SetVar, PrintException):
    """
    Generate text using the Mistral AI client and assign it to the specified variable.

    :param prompt: The input prompt for text generation.
    :param model: The model to use for text generation.
    :param result_var: Name of the variable to store the generated text.
    :param temperature: Sampling temperature for text generation.
    :param max_tokens: Maximum number of tokens to generate.
    :param stop_sequence: Optional stop sequence to end text generation.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    try:
        # Get the client
        client = get_client()
        if not client:
            raise Exception("Debe conectarse a Mistral AI antes de usar este comando. Ejecute primero el módulo de conexión.")

        # Validate required parameters
        if not prompt or not model:
            raise Exception("Debe proporcionar un prompt y un modelo para generar texto.")

        # Create the user message
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        # Generate text using the `chat.complete` method
        response = client.chat.complete(
            model=model,
            messages=messages,
            temperature=float(temperature or 0.7),
            max_tokens=int(max_tokens or 100),
            stop=[stop_sequence] if stop_sequence else None
        )

        # Debug: Print the full response and the generated message content
        print("DEBUG: response =", response)
        print("DEBUG: response.choices[0].message.content =", response.choices[0].message.content)

        # Access the generated message content
        generated_text = response.choices[0].message.content

        # Assign the result to the specified Rocketbot variable
        SetVar(result_var, generated_text)

    except Exception as e:
        # On failure, set the result variable to None and raise the exception
        SetVar(result_var, None)
        print("Error al generar texto con Mistral AI:")
        print(traceback.format_exc())  # Imprime la traza completa del error
        PrintException()
        raise e