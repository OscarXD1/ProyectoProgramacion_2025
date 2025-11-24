import pandas as pd
import mysql.connector

#ESTABLECER CONEXION

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="proyecto"
    )

    cursor = conexion.cursor()

    return cursor, conexion

#LEER ARCHIVO
def leerCSV():
    df = pd.read_csv('farmaciasCompletoLimpio.csv')
    return df

#FUNCION PARA INSERTAR LOS DATOS
def obtenerOInsertar(cursor, conexion, tabla, valor):
    #Buscar si ya existe
    sqlSelect = f"SELECT id FROM {tabla} WHERE descripcion = %s"
    cursor.execute(sqlSelect, (valor,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]

    # Insertar si no existe
    sqlInsert = f"INSERT INTO {tabla} (descripcion) VALUES (%s)"
    cursor.execute(sqlInsert, (valor,))
    conexion.commit()

    return cursor.lastrowid

#TABLA DE LONGITUD Y LATITUD POR QUE SE COMPONE DE DOS COLUMNAS
def obtenerOInsertarLonLat(cursor, conexion, longitud, latitud):

    sqlSelect = "SELECT id FROM LonLat WHERE longitud = %s AND latitud = %s"
    cursor.execute(sqlSelect, (longitud, latitud))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]


    sqlInsert = "INSERT INTO LonLat (longitud, latitud) VALUES (%s, %s)"
    cursor.execute(sqlInsert, (longitud, latitud))
    conexion.commit()

    return cursor.lastrowid



def main():
    cursor, conexion = conectar()

    df=leerCSV()

    for index, fila in df.iterrows():
        descTipoFarmacia = obtenerOInsertar(cursor, conexion, 'tipo_farmacia' ,fila['Tipo'])
        descConsultorio = obtenerOInsertar(cursor, conexion, 'consultorio', fila['Consultorio'])
        descNombreFarmacia = obtenerOInsertar(cursor, conexion, 'nombre_farmacia', fila['Nombre'])
        descClaseActividad = obtenerOInsertar(cursor, conexion, 'clase_actividad', fila['Clase_actividad'])
        descEstrato = obtenerOInsertar(cursor, conexion, 'estrato', fila['Estrato'])
        descCalle = obtenerOInsertar(cursor, conexion, 'calle', fila['Calle'])
        descMunicipio = obtenerOInsertar(cursor, conexion, 'municipio', fila['Ubicacion'])
        descTipoVialidad = obtenerOInsertar(cursor, conexion, 'tipo_vialidad', fila['Tipo_vialidad'])


        # LonLat (longitud y latitud)
        LonLat = obtenerOInsertarLonLat(cursor, conexion, fila["Longitud"], fila["Latitud"])

        # Insertar domicilio
        sqlInsertDomicilio = """
            INSERT INTO domicilio (idCalle, idLonLat, idMunicipio, idTipoVialidad)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sqlInsertDomicilio, (
            descCalle,
            LonLat,
            descMunicipio,
            descTipoVialidad
        ))
        conexion.commit()
        idDomicilio = cursor.lastrowid

        # Insertar farmacia
        sqlInsertFarmacia = """
            INSERT INTO farmacia (
                idNombreFarmacia, idClaseActividad, idEstrato,
                idTipoFarmacia, idConsultorio, idDomicilio
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sqlInsertFarmacia, (
            descNombreFarmacia,
            descClaseActividad,
            descEstrato,
            descTipoFarmacia,
            descConsultorio,
            idDomicilio
        ))
        conexion.commit()

    cursor.close()
    conexion.close()

    print("DATOS INSERTADOS B)")
if __name__ == '__main__':
    main()