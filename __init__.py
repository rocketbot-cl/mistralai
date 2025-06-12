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
cur_path = base_path + 'modules' + os.sep + 'mistralai' + os.sep + 'scripts' + os.sep
libs_path = base_path + 'modules' + os.sep + 'mistralai' + os.sep + 'libs' + os.sep
GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type: ignore

if cur_path not in sys.path:
    sys.path.append(cur_path)

# Agregar la carpeta 'libs' al path si no está ya
if libs_path not in sys.path:
    sys.path.append(libs_path)

from conect_mistral import connect_to_mistral  # type: ignore

module = GetParams("module")

try:
    if module == "connect":
        api_key = GetParams("api_key")
        result_var = GetParams("result_var")

        # Delegar la funcionalidad de conexión al archivo conect_mistral.py
        connect_to_mistral(api_key, result_var, SetVar, PrintException)

except Exception as e:
    PrintException()
    raise e
