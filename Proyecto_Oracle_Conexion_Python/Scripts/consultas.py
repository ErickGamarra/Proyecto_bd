# consultas.py
from conexion_oracle import get_connection

conn = get_connection()
cur = conn.cursor()

# Ejemplo 1: Mostrar todos los clientes
print("=== CLIENTES ===")
cur.execute("SELECT * FROM CLIENTES")
for row in cur:
    print(row)

# Ejemplo 2: Mostrar productos con stock mayor a 100
print("\n=== PRODUCTOS CON STOCK > 100 ===")
cur.execute("SELECT Nom_Prod, Stock FROM PRODUCTOS WHERE Stock > 100")
for row in cur:
    print(row)

# Ejemplo 3: Pedidos pendientes
print("\n=== PEDIDOS PENDIENTES ===")
cur.execute("SELECT Cod_Ped, Cod_Client, estado FROM PEDIDOS WHERE estado = 'Pendiente'")
for row in cur:
    print(row)

# Ejemplo 4: Detalle de pedidos con precio total mayor a 10
print("\n=== DETALLE PEDIDO (Precio_Total > 10) ===")
cur.execute("SELECT Cod_Ped, Cod_Prod, Cantidad, Precio_Total FROM DETALLE_PEDIDO WHERE Precio_Total > 10")
for row in cur:
    print(row)

cur.close()
conn.close()
