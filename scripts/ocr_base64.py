from mistral_client import get_client  # Importar la función para obtener el cliente
import base64
import traceback  # Para capturar trazas de errores

def ocr_base64(model, file_path, result_var, SetVar, PrintException):
    """
    Encode an image to base64 and send it to Mistral AI for OCR processing.

    :param model: The OCR model to use.
    :param file_path: The absolute path to the image file to process.
    :param result_var: Name of the variable to store the OCR result.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    try:
        # Get the client
        client = get_client()
        if not client:
            raise Exception("Debe conectarse a Mistral AI antes de usar este comando. Ejecute primero el módulo de conexión.")

        # Validate required parameters
        if not model or not file_path:
            raise Exception("Debe proporcionar un modelo y una ruta de archivo para procesar con OCR.")

        # Read the file and encode it in base64
        with open(file_path, "rb") as file:
            encoded_image = base64.b64encode(file.read()).decode("utf-8")

        # Prepare the document payload
        document = {
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{encoded_image}"
        }

        # Perform OCR using the `process` method
        response = client.ocr.process(
            model=model,
            document=document,
            include_image_base64=True
        )

        # Extract the text from the response
        extracted_text = ""
        if response.pages:
            for page in response.pages:
                if page.markdown:
                    extracted_text += page.markdown + "\n"
        else:
            extracted_text = "No se pudo extraer texto del documento."

        # Print only the markdown content
        print("DEBUG: OCR Markdown =", extracted_text.strip())

        # Assign the extracted text to the specified Rocketbot variable
        SetVar(result_var, extracted_text)

    except Exception as e:
        # On failure, set the result variable to None and raise the exception
        SetVar(result_var, None)
        print("Error al procesar la imagen con OCR de Mistral AI:")
        print(traceback.format_exc())  # Imprime la traza completa del error
        PrintException()
        raise e