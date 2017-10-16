import psycopg2, menu

class DatabaseConn():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host="192.168.0.12", dbname="postgres", user="sysdba", password="kelly123")
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            print(e)

db = DatabaseConn()

class DatabaseAction():

    '''CREAR BASE DE DATOS'''
    def create_database(self):
        nombreBD = input("Ingrese el nombre de la base de datos: ")
        createDBQuery = """CREATE DATABASE {}""".format(nombreBD)

        self.validaCreacion(createDBQuery)

    """AQUI INICIAN LAS FUNCIONES DDL"""
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

    '''METODO PARA VALIDAR TODAS LAS ACCIONES'''
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
                print("Tabla creada\n")
                input("Presione cualquier tecla para continuar.")
            except psycopg2.Error as e:
                print("Error encontrado en la ejecución del query: {}\n ".format(e))
                input("¿Desea intentarlo de nuevo?\n"
                      "Digite 's' o 'n' ")
        elif respuestaEnMinuscula == 'n' or respuestaEnMinuscula =='no':
            print("Query cancelado")
        else:
            print("Escriba una respuesta correcta")
            self.validaCreacion(query)
        print(db.cursor.statusmessage)

    """AQUI INICIAN LAS FUNCIONES DDL"""

    def insert_data(self):
        nombreTabla = input("Ingrese el nombre de la tabla a la que desea insertar datos: ")
        nombreColumnas = input("Ingrese el nombre de las columnas: ")
        valores = input("Ingrese los valores: ")

        insertQuery = """INSERT INTO {} ({}) VALUES ({})""".format(nombreTabla, nombreColumnas,valores)

        self.validaCreacion(insertQuery)

    def delete_data(self):
        nombreTabla = input("Ingrese el nombre de la tabla de la cual desea borrar datos: ")
        condicion = input("Ingrese la condición que desea evaluar para borrar los datos: ")

        deleteQuery = """DELETE FROM {} WHERE {}""".format(nombreTabla,condicion)

        self.validaCreacion(deleteQuery)

    def update_data_where(self):
        nombreTabla = input("Ingrese el nombre de la tabla de la cual desea actualizar los datos: ")
        columna = input("Ingrese la columna que desea actualizar: ")
        condicion =  input("Ingrese la condición que sea evaluar para actualizar los datos: ")

        updateWhereQuery = """UPDATE {} SET {} WHERE {}""".format(nombreTabla,columna,condicion)

        self.validaCreacion(updateWhereQuery)

    def update_data_general(self):
        nombreTabla = input("Ingrese el nombre de la tabla de la cual desea actualizar los datos: ")
        condicion = input("Ingrese la condicion que desea ejecutar para la actualización: \n"
                          "Ejemplo de condición: SET price = price * 1.10 \n")

        updateGeneralQuery = """UPDATE {} SET {}""".format(nombreTabla,condicion)

        self.validaCreacion(updateGeneralQuery)

    def create_index(self):
        nombreIndex = input("Ingrese el nombre del indice: ")
        nombreTabla = input("Ingrese el nombre de la tabla: ")
        nombreColumna = input("Ingrese el nombre de la tabla en la cual desea aplicar este indice:")

        indexQuery = """CREATE INDEX {} ON {} ({})""".format(nombreIndex,nombreTabla,nombreColumna)

        self.validaCreacion(indexQuery)
    def create_index_unique(self):
        nombreIndex = input("Ingrese el nombre del indice: ")
        nombreTabla = input("Ingrese el nombre de la tabla: ")
        nombreColumna = input("Ingrese el nombre de la tabla en la cual desea aplicar este indice:")

        uniqueIndexQuery = """CREATE UNIQUE INDEX {} ON {} ({})""".format(nombreIndex,nombreTabla,nombreColumna)

        self.validaCreacion(uniqueIndexQuery)

    def alter_index(self):
        nombreIndex = input("Ingrese el nombre del indice: ")
        accion = input("¿Qué desea hacer?\n"
                       "Ingrese alguna de las siguientes opciones: \n"
                       "'r' - Renombrar \n"
                       "'t' - Definir tablespace \n"
                       "'s' - Definir condición \n"
                       "'rs' - Reinciar condicón\n"
                       "'e' - Volver al menú")

        condicion = ""
        if accion == 'r':
            condicion = input("Ingrese el nuevo nombre: ")
            alterIndexQuery = """ALTER INDEX IF EXISTS {} RENAME TO {}""".format(nombreIndex,condicion)

        elif accion == 't':
            condicion = input("Ingrese el nombre del tablespace: ")
            alterIndexQuery = """ALTER INDEX IF EXISTS {} SET TABLESPACE{}""".format(nombreIndex,condicion)

        elif accion == 's':
            condicion = input("Ingrese el nombre del tablespace: ")
            alterIndexQuery = """ALTER INDEX IF EXISTS {} SET {}""".format(nombreIndex,condicion)

        elif accion == 'rs':
            condicion = input("Ingrese el nombre del tablespace: ")
            alterIndexQuery = """ALTER INDEX IF EXISTS {} RESET {}""".format(nombreIndex,condicion)
        elif accion == 'e':
            ddlMenu.close()
            mainMenu.open()
        else:
            print("Ingrese una respuesta válida. ")
            self.alter_table()

        self.validaCreacion(alterIndexQuery)


    def delete_index(self):
        nombreIndice = input("Ingrese el nombre del indice que desea eliminar: ")

        dropIndexQuery = """DROP INDEX IF EXISTS {}""".format(nombreIndice)

        self.validaCreacion(dropIndexQuery)


dbaction = DatabaseAction()

mainMenu = menu.Menu()
ddlMenu = menu.Menu()
updateMenu = menu.Menu()

updateMenu.set_title("Menu Update")
updateMenu.set_options([
    ("Update con where", dbaction.update_data_where),
    ("Update con una condición",dbaction.update_data_general),
    ("Volver al menú DDL",updateMenu.close)])

ddlMenu.set_title("Menu DDL")
ddlMenu.set_options([
    ("Crear una nueva tabla",dbaction.create_table),
    ("Eliminar una tabla existente",dbaction.delete_table),
    ("Alterar una tabla existente",updateMenu.open),
    ("Alterar un indice",dbaction.alter_index),
    ("Volver al menú principal",ddlMenu.close)])

dmlMenu = menu.Menu()
dmlMenu.set_title("Menu DML")
dmlMenu.set_options([
    ("Insertar datos",dbaction.insert_data),
    ("Borrar datos",dbaction.delete_data),
    ("Actualizar datos",dbaction.update_data_where),
    ("Volver al menú principal",dmlMenu.close)])


mainMenu.set_title("Bienvenido a Py Admin")
mainMenu.set_options([
    ("Crear una base de datos", dbaction.create_database),
    ("Menu DDL", ddlMenu.open),
    ("Menu DML",dmlMenu.open)])


if __name__ == '__main__':
    mainMenu.open()


