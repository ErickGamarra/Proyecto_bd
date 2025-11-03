--TABLAS
CREATE TABLE CLIENTES (
    Cod_Client NUMBER(5) NOT NULL,
    Nombre VARCHAR2(30) NOT NULL,
    Apellido VARCHAR2(30) NOT NULL,
    DNI NUMBER(8) UNIQUE NOT NULL ,
    Telefono NUMBER(9) NOT NULL,
    Correo VARCHAR2(30) UNIQUE NOT NULL,
    Direccion VARCHAR2(30) NOT NULL,
    CONSTRAINT PK_CLIENTES PRIMARY KEY (Cod_Client)
)
CREATE TABLE PRODUCTOS (
    Cod_Prod NUMBER(8) NOT NULL, 
    Nom_Prod VARCHAR2(100) NOT NULL,
    Precio NUMBER(6, 2) NOT NULL, 
    Stock NUMBER NOT NULL,          

    CONSTRAINT pk_productos PRIMARY KEY (Cod_Prod),
    CONSTRAINT chk_precio_stock CHECK (precio >= 0 AND stock >= 0)
);
CREATE TABLE PEDIDOS (
    Cod_Ped NUMBER(10) NOT NULL,
    Cod_Client NUMBER(5) NOT NULL, 
    fecha_pedido DATE DEFAULT SYSDATE NOT NULL,
    estado VARCHAR2(50) DEFAULT 'Pendiente' NOT NULL,

    CONSTRAINT pk_pedidos PRIMARY KEY (Cod_Ped),
    CONSTRAINT fk_pedidos_cliente FOREIGN KEY (Cod_Client)
        REFERENCES CLIENTES(Cod_Client)
);
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
);

--DATOS DE LA TABLA CLIENTES
INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (1, 'Sofía', 'Ramírez', 25896314, 945123789, 'sofia.r@mailcorp.com', 'Jr. Los Álamos 105');

INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (2, 'Javier', 'Méndez', 14785236, 933567123, 'javi.mendez@soluciones.net', 'Av. El Sol 402');

INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (3, 'Valeria', 'Castro', 36985214, 978456123, 'valeria.c@webmail.com', 'Calle Santa Elena 55');

INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (4, 'Carlos', 'Rojas', 95126347, 960987321, 'carlos.rojas@mail.pe', 'Jr. Los Sauces 88');

INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (5, 'Luisa', 'Herrera', 74125896, 921543876, 'luisa.herrera@techmail.com', 'Pasaje Las Flores 15');

INSERT INTO CLIENTES (Cod_Client, Nombre, Apellido, DNI, Telefono, Correo, Direccion)
VALUES (6, 'Andrés', 'Silva', 85214736, 998765432, 'andres.silva@inbox.com', 'Av. Primavera 777');
--DATOS DE LA TABLA PRODUCTOS
INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (101, 'Leche Fresca Entera 1L', 4.80, 150);

INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (102, 'Gaseosa Cola 2.5L', 8.50, 90);

INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (103, 'Bolsa de Papas Fritas 150g', 3.20, 240);

INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (104, 'Pan de Molde Blanco', 6.90, 80);

INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (105, 'Agua Mineral sin Gas 600ml', 1.50, 350);

INSERT INTO PRODUCTOS (Cod_Prod, Nom_Prod, Precio, Stock)
VALUES (106, 'Barra de Chocolate con Leche', 2.80, 180);

--DATOS DE LA TABLA PEDIDO
INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10001, 1, TO_DATE('2025-11-01', 'YYYY-MM-DD'), 'Entregado'); 

INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10002, 3, TO_DATE('2025-10-30', 'YYYY-MM-DD'), 'Pendiente'); 

INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10003, 5, TO_DATE('2025-10-25', 'YYYY-MM-DD'), 'En Proceso');

INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10004, 2, TO_DATE('2025-11-01', 'YYYY-MM-DD'), 'Entregado');

INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10005, 4, TO_DATE('2025-10-28', 'YYYY-MM-DD'), 'Pendiente');

INSERT INTO PEDIDOS (Cod_Ped, Cod_Client, fecha_pedido, estado)
VALUES (10006, 6, TO_DATE('2025-10-20', 'YYYY-MM-DD'), 'Cancelado');

-- DATOS DE LA TABLA DETALLE PEDIDO
INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10001, 101, 3, 14.40); 

INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10002, 103, 2, 6.40);

INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10003, 102, 1, 8.50);

INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10004, 105, 4, 6.00);

INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10005, 106, 5, 14.00);

INSERT INTO DETALLE_PEDIDO (Cod_Ped, Cod_Prod, Cantidad, Precio_Total)
VALUES (10006, 104, 1, 6.90);

COMMIT;
