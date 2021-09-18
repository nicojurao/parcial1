import mysql.connector
import re


db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_parcial',
    port=3306
)


def crearUsuario(nombre,email,contraseña):
    cursor=db.cursor()
    cursor.execute('''insert into users(nombre, email, contraseña) values (%s,%s,%s)''',(
    nombre,
    email,
    contraseña
    ))
    db.commit()
    cursor.close

def ingresoSistema(email,contraseña):
    cursor=db.cursor()
    cursor.execute('''select count(*) from users where email=%s and contraseña=%s''',(
    email,
    contraseña
    ))
    data = cursor.fetchall()
    dataval=data[0][0]
    cursor.close()

opcion = 0

while opcion!=3:
    creada=0
    print("1.CREAR USUARIO")
    print("2.INGRESAR AL SISTEMA")
    print("3.SALIR")
    opcion = int(input())

    if opcion==1:
       nombre=input("INGRESE SU NOMBRE: ")

       while creada!=4:
        email=input("INGRESE SU EMAIL: ")
        if "@"and "." in email:
            contraseña=input("INGRESE SU CONTRASEÑA: ")
            crearUsuario(nombre,email,contraseña)
            print("USUARIO CREADO CON EXITO")
            creada=4
        else:
            print("SU CORREO ELECTRONICO NO ES VALIDO, INTENTE NUEVAMENTE CON UNA DIRECCION DE CORREO VALIDA")

    elif opcion==2:
        email=input("INGRESE SU CORREO ELECTRONICO: ")
        contraseña=input("INGRESE SU CONTRASEÑA: ")

        cursor=db.cursor()
        cursor.execute('''select count(*) from users where email=%s and contraseña=%s''',(
        email,
        contraseña
        ))
        data = cursor.fetchall()
        dataval=data[0][0]
        cursor.close()


        if dataval==1:
             print("bienvenido al sistema")
             opcion=3
        else:
            print("nombre usuario o contraseña incorrecta")

    else:
        print("SELECCIONE UNA OPCION VALIDA")
