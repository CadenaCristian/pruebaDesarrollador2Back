import pyodbc

direccion_servidor = 'LAPTOP-5NJLAGL0\SQLEXPRESS'
nombre_bd = 'DesarrolloPrueba'
nombre_usuario = 'sa'
password = '12345678'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("OK! conexión exitosa")
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
