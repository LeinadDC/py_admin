import psycopg2, menu, getpass
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DatabaseConn():
    def __init__(self):
        try:
            host = input("Ingrese el host: ")
            dbname = input("Ingrese la base de datos a la que desea conectarse: ")
            user = input("Ingrese su usuario: ")
            password = getpass.getpass("Ingrese su contraseña: ")
            self.cursor = None
            self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
            self.cursor = self.conn.cursor()
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except psycopg2.Error as e:
            print(e)

class DatabaseAction():

    '''CREAR BASE DE DATOS'''
    def create_database(self):
        nombreBD = input("Ingrese el nombre de la base de datos: ")
        createDBQuery = """CREATE DATABASE {}""".format(nombreBD)

        self.validaCreacion(createDBQuery)

    def show_all_databases(self):
        showDBQuery = """SELECT * FROM pg_database"""
        db.cursor.execute(showDBQuery)
        resultado = db.cursor.fetchall()
        try:
            for row in resultado:
                print(row)
        except psycopg2.DatabaseError as e:
            print(e)
        input("Presione cualquier tecla para continuar.")

    def show_current_database(self):
        currentDBQuery = """SELECT current_database()"""
        db.cursor.execute(currentDBQuery)
        resultado = db.cursor.fetchall()
        try:
            for row in resultado:
                print(row)
        except psycopg2.DatabaseError as e:
            print(e)
        input("Presione cualquier tecla para continuar.")

    """AQUI INICIAN LAS FUNCIONES DDL DE TABLA"""
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
                print("Accion = \n"
                      "{}\n"
                      "Ejecutada")
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

    """AQUI INICIAN LAS FUNCIONES DML"""

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

    """AQUI INICIAN LAS FUNCIONES DDL DE INDICES"""

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

    """AQUI INICIA EL SELECT"""
    def select(self):
        columnas = input("Ingrese las columnas que desea para su selección: ")
        nombreTabla = input("Ingrese el nombre de la tabla: ")

        respuestaJoin = input("¿Desea agregarle algún tipo de JOIN a este query?")
        respuestaJoinEnMinuscula = respuestaJoin.lower()
        selectQuery = """SELECT {} FROM {}""".format(columnas, nombreTabla)

        if respuestaJoinEnMinuscula == 's' or respuestaJoinEnMinuscula == 'si':
            join = self.agregueJoin(selectQuery)
            self.join_builder(selectQuery, join)
        elif respuestaJoinEnMinuscula == 'n' or respuestaJoinEnMinuscula == 'no':
            self.agregueClausula(selectQuery)
        else:
            print("Escriba una respuesta correcta")



    def agregueJoin(self,selectQuery):
        respuesta = input("¿Qué tipo de JOIN desea agregar?\n"
                          "'j' - JOIN\n"
                          "'ij' - INNER JOIN\n"
                          "'lo' - LEFT OUTER JOIN\n"
                          "'ro' - RIGHT OUTER JOIN\n"
                          "'fo' - FULL OUTER JOIN\n"
                          "'cj' - CROSS JOIN\n"
                          "'n' - No agregar un JOIN\n"
                          "Opción = ")
        return respuesta

    def join_builder(self,query, join):
        if join == 'j':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        elif join == 'ij':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ INNER JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        elif join == 'lo':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ LEFT OUTER JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        elif join == 'ro':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ RIGHT OUTER JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        elif join == 'fo':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ FULL OUTER JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        elif join == 'cj':
            condicion, tablaJoin = self.genereArgumentosJoin()
            query += """ CROSS JOIN {} ON {}""".format(tablaJoin, condicion)
            print(query)
            self.agregueClausula(query)
        else:
            print("Else")

        return query

    def genereArgumentosJoin(self):
        tablaJoin = input("Ingrese la tabla con al cual desea realizar el JOIN: ")
        condicion = input("Ingrese la condición que desea evaluar en el JOIN: ")
        return condicion, tablaJoin

    def agregueClausula(self,selectQuery):
        respuesta = input("¿Desea agregar una clausula al query?\n"
                          "Digite 's' o 'n' ")
        respuestaEnMinuscula = respuesta.lower()
        if respuestaEnMinuscula == 's' or respuestaEnMinuscula == 'si':
            clausula = self.genereClausula()
            self.query_builder(selectQuery, clausula)
        elif respuestaEnMinuscula == 'n' or respuestaEnMinuscula == 'no':
            self.validacionSelect(selectQuery)
        else:
            print("Escriba una respuesta correcta")
        return selectQuery

    def genereClausula(self):
        clausula = input("¿Desea agregar una clausula al query?\n"
                         "'w' - Where\n"
                         "'g' - Group by\n"
                         "'h' - Having\n"
                         "'o' - Order By\n"
                         "'n' - No agregar una clausula\n"
                         "Opción = ")
        return clausula

    def query_builder(self,query, clausula):
        if clausula == 'w':
            condicion = input("Ingrese la condición para la clausula WHERE : ")
            query += """ WHERE {}""".format(condicion)
            print(query)
            self.agregueClausula(query)
        elif clausula == 'g':
            condicion = input("Ingrese la condición para la clausula GROUP BY : ")
            query += """ GROUP BY {}""".format(condicion)
            print(query)
            self.agregueClausula(query)
        elif clausula == 'h':
            condicion = input("Ingrese la condición para la clausula HAVING : ")
            query += """ HAVING {}""".format(condicion)
            print(query)
            self.agregueClausula(query)
        elif clausula == 'o':
            condicion = input("Ingrese la condición para la clausula ORDER BY : ")
            query += """ ORDER BY {}""".format(condicion)
            print(query)
            self.agregueClausula(query)
        elif clausula == 'n':
            pass
        else:
            print("Else")

        return query

    def validacionSelect(self,query):
        print("Está a punto de ejecutar el siguiente query: \n"
              "{}\n"
              "¿Está seguro que desea hacerlo?".format(query))
        respuesta = input("Digite 's' o 'n' ")
        respuestaEnMinuscula = respuesta.lower()

        if respuestaEnMinuscula == 's' or respuestaEnMinuscula == 'si':
            try:
                db.cursor.execute(query)
                resultado = db.cursor.fetchall()
                try:
                    for row in resultado:
                        print(row)
                except psycopg2.DatabaseError as e:
                    print(e)

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

    """CREATE FUNCTION - FUNCIONA PERO LE FALTA TRABAJO"""
    def create_Function(self):
        nombreFuncion = input("Ingrese el nombre de la función: ")
        parametros = input("Ingrese los parámetros que acepta la función: ")
        returnFuncion = input("Defina el RETURN de la función: ")
        comoReturnFuncion = input("Defina como debe retornar esta función los datos: ")
        declareVariable = input("Declare las variables que van dentro del segmento DECLARE: ")
        estructuraBegin = input("Escriba la estructura de la función: ")

        funcionQuery = """CREATE OR REPLACE FUNCTION {}({}) RETURNS {} AS {}\n DECLARE {};\n BEGIN \n{} END; LANGUAGE plpgsql""". \
            format(nombreFuncion, parametros, returnFuncion, comoReturnFuncion, declareVariable, estructuraBegin)

        self.validaCreacion(funcionQuery)


dbaction = DatabaseAction()

mainMenu = menu.Menu()
ddlMenu = menu.Menu()
updateMenu = menu.Menu()

dmlMenu = menu.Menu()
dmlMenu.set_title("Menu DML")
dmlMenu.set_options([
    ("Insertar datos",dbaction.insert_data),
    ("Borrar datos",dbaction.delete_data),
    ("Actualizar datos",updateMenu.open),
    ("Volver al menú principal",dmlMenu.close)])

updateMenu.set_title("Menu Update")
updateMenu.set_options([
    ("Update con where", dbaction.update_data_where),
    ("Update con una condición",dbaction.update_data_general),
    ("Volver al menú DDL",updateMenu.close)])

ddlMenu.set_title("Menu DDL")
ddlMenu.set_options([
    ("Crear una nueva tabla",dbaction.create_table),
    ("Eliminar una tabla existente",dbaction.delete_table),
    ("Alterar una tabla existente",dbaction.alter_table),
    ("Crear un nuevo indice",dbaction.create_index),
    ("Crear un nuevo indice único",dbaction.create_index_unique),
    ("Eliminar un indice existente",dbaction.delete_index),
    ("Alterar un indice existente",dbaction.alter_index),
    ("Crear una nueva función", dbaction.create_Function),
    ("Volver al menú principal",ddlMenu.close)])

"""MENU PRINCPIAL"""
mainMenu.set_title("Bienvenido a Py Admin")
mainMenu.set_options([
    ("Ver lista de bases de datos", dbaction.show_all_databases),
    ("Ver base de datos actual", dbaction.show_current_database),
    ("Crear una base de datos", dbaction.create_database),
    ("Menu DDL", ddlMenu.open),
    ("Menu DML",dmlMenu.open),
    ("Select",dbaction.select),
    ("Salir", mainMenu.close)])


if __name__ == '__main__':
    db = DatabaseConn()
    while db.cursor is None:
        db = DatabaseConn()

    mainMenu.open()


