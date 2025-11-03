# conexion_oracle.py
import oracledb

# Inicializa el cliente Oracle (modo thick)
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9")

def get_connection():
    """Retorna una conexión a la base de datos Oracle."""
    return oracledb.connect(
        user="SYSTEM",
        password="ORACLE",
        dsn="localhost/XE"
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Conexión exitosa")
        conn.close()
    except Exception as e:
        print("Error al conectar:", e)
print("Conexión exitosa")