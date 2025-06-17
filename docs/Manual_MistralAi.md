



# Mistral AI
  
Module to interact with Mistral AI models from Rocketbot.  

*Read this in other languages: [English](Manual_mistralai.md), [Português](Manual_mistralai.pr.md), [Español](Manual_mistralai.es.md)*
  
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

To use this module, we need to obtain the API key from MistralAI. Follow these steps:

- First, create a Mistral account or log in at [console.mistral.ai](https://console.mistral.ai/home).

- Then, navigate to "Workspace" and "Billing" to add your payment information and activate payments on your account.
- After that, go to the "API keys" page and create a new API key by clicking on "Create new key". Make sure to copy the API key, store it securely, and not share it with anyone.
## Description of the commands

### Connect to Mistral
  
Establish connection to Mistral AI
|Parameters|Description|example|
| --- | --- | --- |
|API Key|Your Mistral API key|sk-abc123...|
|Assign to variable|Variable name to store the connection|mistralResult|

### Get Models
  
Retrieve available models from Mistral AI
|Parameters|Description|example|
| --- | --- | --- |
|Assign to variable|Variable name to store the list of models|modelsResult|

### Generate Text
  
Generate text using Mistral AI
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Input text to generate text|What is Rocketbot?|
|Model|ID of the model to use|mistral-tiny|
|Assign to variable|Variable name to store the generated text|textResult|
|Temperature (optional)|Controls the randomness of text generation (0.0 a 0.7)|0.7|
|Maximum tokens (optional)|Maximum number of tokens to generate|100|
|Stop sequence (optional)|Optional sequence to stop text generation|RPA tool|

### OCR to Image/PDF
  
Process an image or PDF with Mistral AI OCR
|Parameters|Description|example|
| --- | --- | --- |
|Model|Name of the OCR model to use|mistral-ocr-latest|
|File or URL|Allows uploading a local file or entering a url to an online file|Path or URL of the file|
|Assign to variable|Variable name to store the OCR result|ocrResult|
