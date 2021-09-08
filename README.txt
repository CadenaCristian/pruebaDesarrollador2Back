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
paso 1: pip3 install virtualenv
paso 2: virtualenv <nombre del entorno>
paso 3: cd <nombre del entorno>
paso 4: cd Script
paso 5: source activate

Despues de activar el entorno virtual, se debe dirigir a la ruta del backend y escribir el siguiente comando para activarlo

$ python manage.py runserver 127.0.0.1:8000

- Cabe recalcar que se deben cambiar las variables de conexion a la base de datos, esos datos dependen de que tipo de autenticación credenciales 
use para acceder a sql server


---Compilar el front
Para compilar el front debe ejecutar dos comandos

comando 1: npm i
comando 2: npm run start