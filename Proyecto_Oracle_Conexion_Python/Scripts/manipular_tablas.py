import oracledb

# Inicializa el cliente Oracle
oracledb.init_oracle_client(
    lib_dir=r"C:\oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9"
)

def obtener_conexion():
    return oracledb.connect(
        user="SYSTEM",
        password="ORACLE",
        dsn="localhost/xe"
    )

def listar_tablas():
    tablas = ['CLIENTES', 'PRODUCTOS', 'PEDIDOS', 'DETALLE_PEDIDO']
    conn = obtener_conexion()
    cur = conn.cursor()
    query = f"""
        SELECT table_name
        FROM user_tables
        WHERE table_name IN ({','.join("'" + t + "'" for t in tablas)})
        ORDER BY table_name
    """
    cur.execute(query)
    for row in cur:
        print(row[0])
    cur.close()
    conn.close()

if __name__ == "__main__":
    listar_tablas()
