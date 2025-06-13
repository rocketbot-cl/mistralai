# coding: utf-8
"""
Módulo Rocketbot para conectarse con Mistral AI usando su SDK oficial.

Para obtener el módulo/función que se está llamando:
    GetParams("module")

Para obtener variables desde Rocketbot:
    var = GetParams("nombre_variable")

Para modificar variables en Rocketbot:
    SetVar("nombre_variable", valor)

Para instalar el SDK:
    pip install mistralai -t libs
"""

import os
import sys

base_path = tmp_global_obj["basepath"]  # type: ignore
cur_path = base_path + 'modules' + os.sep + \
    'mistralai' + os.sep + 'scripts' + os.sep
libs_path = base_path + 'modules' + os.sep + \
    'mistralai' + os.sep + 'libs' + os.sep
GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type: ignore

if cur_path not in sys.path:
    sys.path.append(cur_path)

# Agregar la carpeta 'libs' al path si no está ya
if libs_path not in sys.path:
    sys.path.append(libs_path)


module = GetParams("module")

from generate_text import generate_text  # type: ignore
from get_models import get_models  # type: ignore
from conect_mistral import connect_to_mistral  # type: ignore

try:
    if module == "connect":
        api_key = GetParams("api_key")
        result_var = GetParams("result_var")
        connect_to_mistral(api_key, result_var, SetVar, PrintException)

    elif module == "get_models":
        result_var = GetParams("result_var")
        get_models(result_var, SetVar, PrintException)

    elif module == "generate_text":
        prompt = GetParams("prompt")
        model = GetParams("model")
        result_var = GetParams("result_var")
        temperature = GetParams("temperature")
        max_tokens = GetParams("max_tokens")
        stop_sequence = GetParams("stop_sequence")
        generate_text(prompt, model, result_var, temperature, max_tokens, stop_sequence, SetVar, PrintException)

    else:
        raise Exception(f"El módulo '{module}' no está implementado.")
except Exception as e:
    PrintException()
    raise e
