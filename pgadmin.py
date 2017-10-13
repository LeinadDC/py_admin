import psycopg2, menu

class DatabaseConn():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host="192.168.0.11", dbname="postgres", user="sysdba", password="kelly123")
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(e)

db = DatabaseConn()

class DatabaseAction():

    def create_database(self):
        nombreBD = input("Ingrese el nombre de la base de datos: ")
        createDBQuery = """CREATE DATABASE {}""".format(nombreBD)

        self.validaCreacion(createDBQuery)

    def create_table(self):
        nombreTabla = input("Ingrese el nombre de la tabla: ")
        atributosTabla = input("Los atributos se deben ingresar de la siguiente manera:\n"
                               "nombre VARCHAR(20), dinero INT(15)\n"
                               "Ingrese los atributos que desea en la tabla:\n")
        createTableQuery = """CREATE TABLE {}({})""".format(nombreTabla,atributosTabla)

        self.validaCreacion(createTableQuery)

    def alter_table(self):
        nombreTabla = input("Ingrese el nombre de la tabla que desea editar: ")
        argumentoAlteracion = input("El argumento de alteracion se debe ingeresar de la siguiente manera: \n"
                                    "ADD COLUMN edad INT NOT NULL\n"
                                    "Ingrese el argumento de alteracion que desea ejecutar: \n")
        alterTableQuery = """ALTER TABLE {} {}""".format(nombreTabla, argumentoAlteracion)

        self.validaCreacion(alterTableQuery)

    def delete_table(self):
        nombreTabla = input("Ingrese el nombre de la tabla que desea eliminar: ")

        dropTableQuery = """DROP TABLE {}""".format(nombreTabla)

        self.validaCreacion(dropTableQuery)

    def validaCreacion(self,query):
        print("Está a punto de ejecutar el siguiente query: \n"
              "{}\n"
              "¿Está seguro que desea hacerlo?".format(query))
        respuesta = input("Digite 's' o 'n' ")
        respuestaEnMinuscula = respuesta.lower()

        if respuestaEnMinuscula == 's' or respuestaEnMinuscula == 'si':
            try:
                db.cursor.execute(query)
                db.conn.commit()
            except psycopg2.Error as e:
                print(e)
        elif respuestaEnMinuscula == 'n' or respuestaEnMinuscula =='no':
            print("Query cancelado")
        else:
            print("Escriba una respuesta correcta")
            self.validaCreacion(query)

mainMenu = menu.Menu()

mainMenu.set_options([
("Conectarse a una base de datos", db.conn)])


if __name__ == '__main__':
    mainMenu.open()

