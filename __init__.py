# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path,'modules','filestack_')
sys.path.append(os.path.join(cur_path , 'libs'))
from filestack import Client
from filestack import Filelink

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "upload_":

    try:
        key_ = GetParams('key_')
        path_ = GetParams('path_')
        var_ = GetParams('id_')

        client = Client(key_)

        params = {'mimetype': 'image/png'}
        new_filelink = client.upload(filepath=path_)
        id = os.path.basename(new_filelink.url)
        SetVar(var_,id)

    except Exception as e:
        PrintException()
        raise Exception(e)

if module == "resize":

    id_ = GetParams('id_')
    width_ = GetParams('width_')
    height_ = GetParams('height_')
    check_ = GetParams('check_')
    var_ = GetParams('var_')

    try:
        filelink = Filelink(id_)

        if check_ == True:
            filelink = (
                # filelink.resize(width=width_, height=height_, fit="clip", align="top")
                filelink.resize(width=width_, height=height_, fit="scale").store()
            )

            id = os.path.basename(filelink.url)
            print(id)

        else:
            filelink = (
                filelink.resize(width=width_, height=height_, fit="clip").store()
            )
            id = os.path.basename(filelink.url)

        SetVar(var_,id)

    except Exception as e:
        PrintException()
        raise Exception(e)

if module == "crop":

    id_ = GetParams('id_')
    x_ = GetParams('x_')
    y_ = GetParams('y_')
    width_ = GetParams('width_')
    height_ = GetParams('height_')
    var_ = GetParams('var_')

    try:
        filelink = Filelink(id_)

        filelink = (
            filelink.crop(dim=[x_, y_, width_, height_]).store()
        )

        id = os.path.basename(filelink.url)

        SetVar(var_, id)
    except Exception as e:
        PrintException()
        raise Exception(e)


if module == "download_":

    id_ = GetParams('id_')
    path_ = GetParams('path_')
    path_ = os.path.normpath(path_)
    name_ = GetParams('name_')

    try:
        file_ = os.path.join(path_,name_)
        print(file_)

        filelink = Filelink(id_)
        save_ = filelink.download(file_)

    except Exception as e:
        PrintException()
        raise Exception(e)

