create data base consesionario;
use consesionario;
create table cliente(
    id int primary key,
    nombre varchar(30) not null,
    direccion varchar(20) not null,
    ciudad varchar(20) not null,
    telefono varchar(20) not null
    );
create table autos(
    matricula int primary key not null,
    marca varchar(20) not null,
    modelo varchar(20) not null,
    color varchar(20) not null,
);
create table promotor(
    id int primary key not null,
    nombre varchar(30) not null,
    turno varchar(20) not null,
    telefono varchar(20) not null unique

);

create table venta(
    id_venta int primary key not null,
    id_cliente int not null,
    matricula int not null,
    id_promotor int not null,
    fecha date not null,
    precio decimal(10,2) not null,
    foreign key (id_cliente) references cliente(id),
    foreign key (matricula) references autos(matricula),
    foreign key (id_promotor) references promotor(id)
);


create table compra(
    fecha_compra int primary key not null,
    fecha_compra datetime,
    id_cliente int,
    mat_auto int,
    foreign key (id_cliente) references cliente(id),
)


insert into cliente  values (1,'Juan Perez','Calle 123','Ciudad A','555-1234');

