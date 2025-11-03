# insertar_datos.py
from conexion_oracle import get_connection

# Datos a insertar
clientes = [
    (1, 'Sofía', 'Ramírez', 25896314, 945123789, 'sofia.r@mailcorp.com', 'Jr. Los Álamos 105'),
    (2, 'Javier', 'Méndez', 14785236, 933567123, 'javi.mendez@soluciones.net', 'Av. El Sol 402'),
    (3, 'Valeria', 'Castro', 36985214, 978456123, 'valeria.c@webmail.com', 'Calle Santa Elena 55'),
    (4, 'Carlos', 'Rojas', 95126347, 960987321, 'carlos.rojas@mail.pe', 'Jr. Los Sauces 88'),
    (5, 'Luisa', 'Herrera', 74125896, 921543876, 'luisa.herrera@techmail.com', 'Pasaje Las Flores 15'),
    (6, 'Andrés', 'Silva', 85214736, 998765432, 'andres.silva@inbox.com', 'Av. Primavera 777')
]

productos = [
    (101, 'Leche Fresca Entera 1L', 4.80, 150),
    (102, 'Gaseosa Cola 2.5L', 8.50, 90),
    (103, 'Bolsa de Papas Fritas 150g', 3.20, 240),
    (104, 'Pan de Molde Blanco', 6.90, 80),
    (105, 'Agua Mineral sin Gas 600ml', 1.50, 350),
    (106, 'Barra de Chocolate con Leche', 2.80, 180)
]

pedidos = [
    (10001, 1, '2025-11-01', 'Entregado'),
    (10002, 3, '2025-10-30', 'Pendiente'),
    (10003, 5, '2025-10-25', 'En Proceso'),
    (10004, 2, '2025-11-01', 'Entregado'),
    (10005, 4, '2025-10-28', 'Pendiente'),
    (10006, 6, '2025-10-20', 'Cancelado')
]

detalle_pedidos = [
    (10001, 101, 3, 14.40),
    (10002, 103, 2, 6.40),
    (10003, 102, 1, 8.50),
    (10004, 105, 4, 6.00),
    (10005, 106, 5, 14.00),
    (10006, 104, 1, 6.90)
]

# Conexión a la base
conn = get_connection()
cur = conn.cursor()

# Insertar datos
cur.executemany("""
    INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
    VALUES (:1, :2, :3, :4, :5, :6, :7)
""", clientes)

cur.executemany("""
    INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
    VALUES (:1, :2, :3, :4)
""", productos)

cur.executemany("""
    INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
    VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
""", pedidos)

cur.executemany("""
    INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
    VALUES (:1, :2, :3, :4)
""", detalle_pedidos)

conn.commit()
cur.close()
conn.close()

print("Datos insertados correctamente.")
