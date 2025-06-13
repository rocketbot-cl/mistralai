from mistral_client import get_client  # Importar la función para obtener el cliente
import traceback  # Para capturar trazas de errores


def ocr_document(model, document_url, document_type, result_var, SetVar, PrintException):
    """
    Send a document or image URL to Mistral AI for OCR processing and extract the text.

    :param model: The OCR model to use.
    :param document_url: The URL of the document or image to process.
    :param document_type: The type of the document ("image" for images, "pdf" for PDFs).
    :param result_var: Name of the variable to store the extracted text.
    :param SetVar: Function to set variables in Rocketbot.
    :param PrintException: Function to print exceptions in Rocketbot.
    """
    try:
        # Get the client
        client = get_client()
        if not client:
            raise Exception("Debe conectarse a Mistral AI antes de usar este comando. Ejecute primero el módulo de conexión.")

        # Validate required parameters
        if not model or not document_url or not document_type:
            raise Exception("Debe proporcionar un modelo, una URL de documento o imagen, y el tipo de documento para procesar con OCR.")

        # Prepare the document payload based on the type
        if document_type == "image":
            document = {"type": "image_url", "image_url": document_url}
        elif document_type == "pdf":
            document = {"type": "document_url", "document_url": document_url}
        else:
            raise Exception("Tipo de documento no soportado. Use 'image' para imágenes o 'pdf' para documentos PDF.")

        # Perform OCR using the `process` method
        response = client.ocr.process(
            model=model,
            document=document
        )

        # Debug: Print the full response
        print("DEBUG: OCR response =", response)

        # Extract the text from the response
        extracted_text = ""
        if response.pages:
            for page in response.pages:
                if page.markdown:
                    extracted_text += page.markdown + "\n"
        else:
            extracted_text = "No se pudo extraer texto del documento."

        # Assign the extracted text to the specified Rocketbot variable
        SetVar(result_var, extracted_text)

    except Exception as e:
        # On failure, set the result variable to None and raise the exception
        SetVar(result_var, None)
        print("Error al procesar el documento con OCR de Mistral AI:")
        print(traceback.format_exc())  # Imprime la traza completa del error
        PrintException()
        raise e