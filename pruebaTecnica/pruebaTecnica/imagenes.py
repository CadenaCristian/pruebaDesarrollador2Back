from django.http import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .mydb import conexion
from .query import addFavoritosQuery, valExistQuery, listFavoritosQuery, disableFavorito
import json
import requests
import base64
import os

# Este service se encarga de listar las imagenes desde una api publica


@csrf_exempt
def listImage(request):
    if request.method == 'GET':
        try:
            arrayImg = []
            count = 0
            while count < 12:
                imgObject = {
                    "name": '',
                    "url": '',
                    "favorito": False
                }
                count = count + 1
                response = requests.get(
                    'https://dog.ceo/api/breeds/image/random')
                response = response.json()
                sp = response['message']
                partido = sp.split('/')
                nombreImagen = partido[5]
                # imagen = requests.get(sp).content
                # with open(nombreImagen, 'wb') as handler:
                #     handler.write(imagen)
                # with open(nombreImagen, "rb") as bimg:
                #     encoded = base64.b64encode(bimg.read())
                # encoded = str(encoded, 'utf-8')
                imgObject["name"] = nombreImagen
                imgObject["url"] = sp
                arrayImg.append(imgObject)
                # os.remove(os.path.expanduser(nombreImagen))
            respuesta = {
                "error": False,
                "message": "Se retorna la imagen en base64",
                "data": arrayImg
            }
            return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al retornar la imagen en base64",
                "data": error
            }

# Este service es el encargado de añadir una imagen que se haya seleccionado desde la api publica,
# la convierte ne base64 y la almacena en la base de datos


@csrf_exempt
def addFavoritos(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            with conexion.cursor() as db:
                valExist = valExistQuery.format(
                    body["imgName"])
                db.execute(valExist)
                exist = db.rowcount
                if exist == 0:
                    bs64Split = body["b64"].split('base64,')
                    sql = addFavoritosQuery.format(
                        body["imgName"], bs64Split[1], 1)
                else:
                    sql = disableFavorito.format(body["imgName"])
                db.execute(sql)
            respuesta = {
                "error": False,
                "message": "Se añade a favoritos con exito"
            }
            return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al añadir a favoritos",
                "data": error
            }
            print("error: ", error)

# Este service es el encargado de listar las imagenes que hayan sido almacenasdas como favoritas


def listFavoritos(request):
    if request.method == 'GET':
        try:
            array = []
            with conexion.cursor() as db:
                sql = listFavoritosQuery
                db.execute(sql)
                result = db.fetchall()
                for res in result:
                    obj = {
                        'id': res[0],
                        'imgName': res[1],
                        'b64': res[2],
                        'estado': res[3]
                    }
                    array.append(obj)
            respuesta = {
                "error": False,
                "message": "Se retorna las imagenes en favoritos",
                "data": array
            }
            return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al listar favoritos",
                "data": error
            }
