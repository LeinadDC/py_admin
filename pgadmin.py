import psycopg2

try:
    conn = psycopg2.connect(host="192.168.0.11", dbname="postgres", user="sysdba", password="kelly123")
    print("Connecting to PostgreSQL")
    cursor = conn.cursor()
except psycopg2.Error as e:
    print(e)

def create_database():
    nombreBD = input("Ingrese el nombre de la base de datos: ")
    createDBQuery = """CREATE DATABASE {}""".format(nombreBD)

    validaCreacion(createDBQuery)

def create_table():
    nombreTabla = input("Ingrese el nombre de la tabla: ")
    atributosTabla = input("Los atributos se deben ingresar de la siguiente manera:\n"
                           "nombre VARCHAR(20), dinero INT(15)\n"
                           "Ingrese los atributos que desea en la tabla:\n")
    createTableQuery = """CREATE TABLE {}({})""".format(nombreTabla,atributosTabla)

    validaCreacion(createTableQuery)

def alter_table():
    nombreTabla = input("Ingrese el nombre de la tabla que desea editar: ")
    argumentoAlteracion = input("El argumento de alteracion se debe ingeresar de la siguiente manera: \n"
                                "ADD COLUMN edad INT NOT NULL\n"
                                "Ingrese el argumento de alteracion que desea ejecutar: \n")
    alterTableQuery = """ALTER TABLE {} {}""".format(nombreTabla, argumentoAlteracion)

    validaCreacion(alterTableQuery)

def validaCreacion(query):
    print("Está a punto de ejecutar el siguiente query: \n"
          "{}\n"
          "¿Está seguro que desea hacerlo?".format(query))
    respuesta = input("Digite 's' o 'n' ")
    respuestaEnMinuscula = respuesta.lower()

    if respuestaEnMinuscula == 's' or respuestaEnMinuscula == 'si':
        try:
            cursor.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print(e)
    elif respuestaEnMinuscula == 'n' or respuestaEnMinuscula =='no':
        print("Query cancelado")
    else:
        print("Escriba una respuesta correcta")
        validaCreacion(query)

if __name__ == '__main__':
    alter_table()

