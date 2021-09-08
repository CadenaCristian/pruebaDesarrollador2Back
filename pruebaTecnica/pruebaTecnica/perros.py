from django.http import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .mydb import conexion
from .query import createDogQuery, listDogQuery, listDogByIdQuery, updateDogQuery, disableDogQuery, deleteDogQuery
import json
# import requests
# import base64

# Este service es el encragado de añadir un perro nuevo en la base de datos, con los datos ingresados por
# el usuario desde el front


@csrf_exempt
def createDog(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            with conexion.cursor() as db:
                sql = createDogQuery.format(
                    body["dogName"], body["race"], body["age"], body["picture"])
                db.execute(sql)
                retorna = db.rowcount
            respuesta = {
                "error": False,
                "message": "Se inserta el perro con exito",
                "data": retorna
            }
            return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al añadir al canino",
                "data": error
            }

# Este service es el encargado de listar los perros que se hyan creado


@csrf_exempt
def listDog(request):
    if request.method == 'GET':
        try:
            array = []
            with conexion.cursor() as db:
                sql = listDogQuery
                db.execute(sql)
                retorna = db.fetchall()
                for x in retorna:
                    obj = {
                        "id": x[0],
                        "dogName": x[1],
                        "race": x[2],
                        "age": x[3],
                        "picture": x[4],
                        "estado": x[5]
                    }
                    array.append(obj)
                respuesta = {
                    "error": False,
                    "message": "Se retorna una lista con los perros que se han creado",
                    "data": array
                }
                return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al listar los caninos",
                "data": error
            }

# Este service se encarga de retornar la información para un perro en especifico


@csrf_exempt
def listDogById(request, id):
    if request.method == 'GET':
        try:
            array = []
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            with conexion.cursor() as db:
                sql = listDogByIdQuery.format(id)
                db.execute(sql)
                retorna = db.fetchone()
                obj = {
                    "id": retorna[0],
                    "dogName": retorna[1],
                    "race": retorna[2],
                    "age": retorna[3],
                    "picture": retorna[4],
                    "estado": retorna[5]
                }
                array.append(obj)
                respuesta = {
                    "error": False,
                    "message": "Se retorna el dato segun su id",
                    "data": array
                }
                return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al mostrar la imagen del canino",
                "data": error
            }

# Este service es el encargado de actualizar los datos del perro


@csrf_exempt
def updateDog(request):
    if request.method == 'PUT':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            with conexion.cursor() as db:
                sql = updateDogQuery.format(
                    body["dogName"], body["race"], body["age"], body["picture"], body["id"])
                db.execute(sql)
                retorna = db.rowcount
                respuesta = {
                    "error": False,
                    "message": "Se actualizan los datos",
                    "data": retorna
                }
                return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al actualizar al canino",
                "data": error
            }
        print("error: ", error)

# Este service se creo pero no se uso, se creo ya que es una buena practica deshabilitar los datos en lugar de eliminarlos


@csrf_exempt
def disableDog(request, id):
    if request.method == 'PATCH':
        try:
            with conexion.cursor() as db:
                sql = disableDogQuery.format(id)
                db.execute(sql)
                retorna = db.rowcount
                respuesta = {
                    "error": False,
                    "message": "Se deshabilita la imagen del canino",
                    "data": retorna
                }
                return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al deshabilitar al canino",
                "data": error
            }

# Este service es el encargado de eliminar un perro en especifico


@csrf_exempt
def deleteDog(request, id):
    if request.method == 'DELETE':
        try:
            with conexion.cursor() as db:
                sql = deleteDogQuery.format(id)
                db.execute(sql)
                retorna = db.rowcount
                respuesta = {
                    "error": False,
                    "message": "Se elimina la imagen del canino",
                    "data": retorna
                }
                return JsonResponse(respuesta, safe=False)
        except Exception as error:
            respuesta = {
                "error": False,
                "message": "Error al eliminar al canino",
                "data": error
            }
