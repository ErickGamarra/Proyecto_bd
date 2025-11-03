Esta carpeta contiene todos los scripts Python utilizados para conectarse y trabajar con la base de datos Oracle XE del proyecto. Cada script tiene una función específica y juntos permiten crear la estructura de las tablas, insertar los datos iniciales y realizar consultas o pruebas.



Lista de scripts y funciones:



* conexion\_oracle.py



Permite conectarse a la base de datos Oracle de manera reusable.



Inicializa el cliente Oracle (modo thick) y devuelve una conexión que otros scripts pueden usar.



* crear\_tablas.py



Crea la estructura de las tablas según el SQL proporcionado: CLIENTES, PRODUCTOS, PEDIDOS y DETALLE\_PEDIDO.



Solo debe ejecutarse una vez antes de insertar datos.



* insertar\_datos.py



Inserta los registros iniciales en cada tabla según el SQL proporcionado.



Se ejecuta después de crear las tablas para llenar la base con los datos de ejemplo.



* manipular\_tablas.py



Permite hacer consultas de prueba sobre las tablas.



Muestra los nombres de las tablas y puede modificarse para hacer SELECTs, INSERTs o pruebas adicionales de manera controlada.



* consultas.py



Contiene consultas específicas sobre las tablas del proyecto.



Permite extraer información como pedidos de un cliente, productos en stock, total de ventas, etc.



Ideal para probar SQL más avanzados y mostrar resultados de manera organizada.



* proyecto\_oracle.py



Archivo principal que puede combinar funciones de los demás scripts.



Permite ejecutar de manera más completa las operaciones del proyecto, como crear tablas, insertar datos y ejecutar consultas desde un solo lugar.



Sirve como punto de entrada para probar o integrar todo el proyecto en Python.



Orden recomendado de ejecución:



1. conexion\_oracle.py – probar que la conexión funciona.



2\. crear\_tablas.py – crear la estructura de la base.



3\. insertar\_datos.py – llenar las tablas con los registros iniciales.



4\. manipular\_tablas.py – realizar pruebas o consultas básicas.



5\. consultas.py – ejecutar consultas más específicas según las necesidades del proyecto.



6\. proyecto\_oracle.py – probar todo de manera integrada.



Notas:



Todos los scripts usan el usuario SYSTEM y la contraseña ORACLE para conectarse a localhost/XE.



Se requiere que el Oracle Instant Client esté correctamente instalado y el path configurado para que Python pueda usar el cliente.



Se recomienda no ejecutar crear\_tablas.py ni insertar\_datos.py más de una vez, para evitar errores de duplicados.

