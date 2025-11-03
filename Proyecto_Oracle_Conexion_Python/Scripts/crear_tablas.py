# crear_tablas.py
import oracledb
from conexion_oracle import get_connection  # Reutiliza la conexión

conn = get_connection()
cur = conn.cursor()

# Crear las tablas según la estructura proporcionada
cur.execute("""
CREATE TABLE CLIENTES (
    Cod_Client NUMBER(5) NOT NULL,
    Nombre VARCHAR2(30) NOT NULL,
    Apellido VARCHAR2(30) NOT NULL,
    DNI NUMBER(8) UNIQUE NOT NULL,
    Telefono NUMBER(9) NOT NULL,
    Correo VARCHAR2(30) UNIQUE NOT NULL,
    Direccion VARCHAR2(30) NOT NULL,
    CONSTRAINT PK_CLIENTES PRIMARY KEY (Cod_Client)
)
""")

cur.execute("""
CREATE TABLE PRODUCTOS (
    Cod_Prod NUMBER(8) NOT NULL, 
    Nom_Prod VARCHAR2(100) NOT NULL,
    Precio NUMBER(6, 2) NOT NULL, 
    Stock NUMBER NOT NULL,
    CONSTRAINT pk_productos PRIMARY KEY (Cod_Prod),
    CONSTRAINT chk_precio_stock CHECK (precio >= 0 AND stock >= 0)
)
""")

cur.execute("""
CREATE TABLE PEDIDOS (
    Cod_Ped NUMBER(10) NOT NULL,
    Cod_Client NUMBER(5) NOT NULL, 
    fecha_pedido DATE DEFAULT SYSDATE NOT NULL,
    estado VARCHAR2(50) DEFAULT 'Pendiente' NOT NULL,
    CONSTRAINT pk_pedidos PRIMARY KEY (Cod_Ped),
    CONSTRAINT fk_pedidos_cliente FOREIGN KEY (Cod_Client)
        REFERENCES CLIENTES(Cod_Client)
)
""")

cur.execute("""
CREATE TABLE DETALLE_PEDIDO (
    Cod_ped NUMBER NOT NULL,      
    Cod_Prod NUMBER NOT NULL,    
    Cantidad NUMBER NOT NULL,
    Precio_Total NUMBER(8, 2) NOT NULL, 
    CONSTRAINT pk_detalle_pedido PRIMARY KEY (Cod_Ped, Cod_prod),
    CONSTRAINT fk_detalle_pedido_ped FOREIGN KEY (Cod_Ped)
        REFERENCES PEDIDOS(Cod_Ped),
    CONSTRAINT fk_detalle_pedido_prod FOREIGN KEY (Cod_Prod)
        REFERENCES PRODUCTOS(Cod_Prod),      
    CONSTRAINT chk_cantidad CHECK (cantidad > 0)
)
""")

conn.commit()
cur.close()
conn.close()
print("Tablas creadas correctamente")
