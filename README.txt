---SQL SERVER (Base de datos)-----
---Para el desarrollo se uso como motor de base de datos SQL SERVER y los siguientes scripst se deben compilar  para el buen funcionamiento del mismo

CREATE DATABASE DesarrolloPrueba;

CREATE TABLE favoritos (
    id int IDENTITY(1,1) PRIMARY KEY,
    imgName varchar(255) NOT NULL,
    b64 varchar(max),
    estado bit not null
);

CREATE TABLE perros (
    id int IDENTITY(1,1) PRIMARY KEY,
    dogName varchar(100) NOT NULL,
	race varchar(100) NOT NULL,
	age int NOT NULL,
    picture varchar(max),
    estado bit not null
);

---Compilacion del back (Python)
Para poder compilar el backend se debe de levantar el entorno virtual los siguientes comando sirven para su creacion,
de igual forma en las carpetas se adjunta el entorno virtual que se uso
paso 1:  python3 -m venv nombreSeleccionado
paso 2: cd <nombre del entorno>
paso 3: cd Script
paso 4: source activate

Despues de activar el entorno virtual, se debe dirigir a la ruta del backend y escribir el siguiente comando para activarlo

$ python manage.py runserver 127.0.0.1:8000

- en caso de que error por alguna libreria, se adjunta el listado de las librerias y dependencias que se usaron, todas se instalan usando
el comando pip install <nombre de la libreria>
asgiref==3.4.1
autopep8==1.5.6
backports.entry-points-selectable==1.1.0
certifi==2021.5.30
charset-normalizer==2.0.4
distlib==0.3.2
Django==3.2.7
django-cors-headers==3.8.0
filelock==3.0.12
idna==3.2
platformdirs==2.2.0
pycodestyle==2.7.0
pyodbc==4.0.32
pytz==2021.1
requests==2.26.0
six==1.16.0
sqlparse==0.4.1
toml==0.10.2
urllib3==1.26.6
virtualenv==20.7.2

- tambien se adjuntan los comando de las 4 librerias que abarcan la mayoria de las anteriores ya mencionadas
pip install django
pip install django-cors-headers
pip install pyodbc
pip install requests

- Cabe recalcar que se deben cambiar las variables de conexion a la base de datos, esos datos dependen de que tipo de autenticación credenciales 
use para acceder a sql server


---Compilar el front
Para compilar el front debe ejecutar dos comandos

comando 1: npm i
comando 2: npm run start
