# Este archivo.py se creo ya que es una buena practica tener el codigo separado cuando se deben de realizar consultas a la base de datos,
# ya que se vuelve mucho mas legible e identificable para futuros desarrolladores entender el uso de este archivo

addFavoritosQuery = "INSERT INTO favoritos (imgName,b64,estado) VALUES('{}','{}',{})"
disableFavorito = "UPDATE favoritos SET estado = 0 where imgName = '{}'"
valExistQuery = "select * from favoritos where imgName = '{}'"
listFavoritosQuery = "select * from favoritos where estado = 1"
createDogQuery = "INSERT INTO perros (dogName,race,age,picture,estado) VALUES ('{}','{}',{},'{}',1)"
listDogQuery = "select * from perros"
listDogByIdQuery = "select * from perros where id = {}"
updateDogQuery = "UPDATE perros SET dogName = '{}', race = '{}', age = {}, picture = '{}' where id = {}"
disableDogQuery = "UPDATE perros SET estado = 0 where id = {}"
deleteDogQuery = "DELETE FROM perros where id = {}"
