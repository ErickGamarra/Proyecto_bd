# 1. Crear la carpeta del proyecto
C:\Users\art_r>mkdir Proyecto_Oracle_Conexion_Python
C:\Users\art_r>cd Proyecto_Oracle_Conexion_Python

# 2. Comprobar versión de Python
C:\Users\art_r\Proyecto_Oracle_Conexion_Python>python --version

# 3. Instalación de la librería oracledb
C:\Users\art_r\Proyecto_Oracle_Conexion_Python>pip install oracledb

# 4. Verificar listener de Oracle XE
C:\Users\art_r>lsnrctl status

# 5. Probar conexión a base de datos Oracle XE
C:\Users\art_r>sqlplus system/ORACLE@localhost/XE

# 6. Crear scripts en la carpeta Scripts
# - conexion_oracle.py
# - crear_tablas.py
# - insertar_datos.py
# - manipular_tablas.py
# - proyecto_oracle.py

# 7. Configuración del Oracle Instant Client
# Extraer zip descargado a C:\oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9
# Agregar al PATH:
C:\oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9

# 8. Probar que Oracle Client carga en Python
C:\Users\art_r>python
>>> import oracledb
>>> oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9")
>>> print("Oracle Client cargado correctamente")
Oracle Client cargado correctamente

# 9. Probar conexión desde Python usando el script conexion_oracle.py
C:\Users\art_r\Proyecto_Oracle_Conexion_Python\Scripts>python conexion_oracle.py

# 10. Crear la estructura de tablas
C:\Users\art_r\Proyecto_Oracle_Conexion_Python\Scripts>python crear_tablas.py

# 11. Insertar los datos originales en las tablas
C:\Users\art_r\Proyecto_Oracle_Conexion_Python\Scripts>python insertar_datos.py

# 12. Probar consultas básicas
C:\Users\art_r\Proyecto_Oracle_Conexion_Python\Scripts>python manipular_tablas.py

# 13. Comprobar tablas y datos desde SQL*Plus
C:\Users\art_r>sqlplus system/ORACLE@localhost/XE
SQL> SELECT table_name FROM user_tables;
SQL> SELECT * FROM CLIENTES;
SQL> SELECT * FROM PRODUCTOS;
SQL> SELECT * FROM PEDIDOS;
SQL> SELECT * FROM DETALLE_PEDIDO;

# 14. Otros comandos útiles en SQL*Plus
SQL> DESC CLIENTES;
SQL> COMMIT;
SQL> EXIT;

# 15. Cierre de sesión y pruebas finales
C:\Users\art_r\Proyecto_Oracle_Conexion_Python\Scripts>exit


NOTAS: art_r : Fue el nombre del usuario del equipo en donde se trabajó, puede variar según en donde se desarrolle el trabajo.
Se realizó en un entorno con win11 HOME, así que si es usuario de Linux requerirá utilizar otro tipo de comandos en bash.