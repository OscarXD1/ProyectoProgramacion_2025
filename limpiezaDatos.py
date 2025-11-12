import pandas as pd

ruta="farmaciasEstadoCompleto.csv"
dfOriginal=pd.read_csv(ruta)
dfLimpio= dfOriginal.copy()


#checar la estructura que tienen los datos
def estructura(dfLimpio:pd.DataFrame):
    print(dfLimpio.head())
    print(dfLimpio.shape)
    print(dfLimpio.info())
    print(dfLimpio.columns)
    print(dfLimpio.dtypes)
    print(dfLimpio.index)


#checar nulos
def revisarNulos(dfLimpio: pd.DataFrame):
    print(dfLimpio.isnull().sum())
#porcentaje de nulos de cada columna
    print(dfLimpio.isnull().sum() / len(dfLimpio))

""""
despues d esto de los nulos voy a borrar
telefono,correo,corredor industrial,nom corredor industrial,numero local,num exterior, num interior,  duda razon social,
"""

#los duplicados
def verDuplicados(dfLimpio: pd.DataFrame):
    print(dfLimpio.duplicated())
    print(dfLimpio[dfLimpio.duplicated(keep=False)]) #en la salida dio que no tiene duplis
    print(dfLimpio.drop_duplicates().shape[0]) #aqui solo confirme

#revisar duplis por columnas q pueden estar relacionadas
    print(dfLimpio[dfLimpio.duplicated(subset=["Nombre","Colonia"],keep=False)])
    print(dfLimpio[dfLimpio.duplicated(subset=["Latitud", "Longitud"], keep=False)])
    print(dfLimpio[dfLimpio.duplicated(subset=["Nombre", "Colonia", "Latitud", "Longitud"], keep=False)]) #814 duplicados
    print(dfLimpio[dfLimpio.duplicated(subset=["Nombre", "Colonia", "Latitud", "Longitud"], keep=False)].groupby(["Nombre", "Colonia", "Latitud", "Longitud"]).size()) #cuantas veces se repite cada combi
#las xonbinaciones que salen igual en nombre, colonia, latitud y longitud aparecen dos veces

#AQUI BORRARE LOS DUPLIS
def eliminarDuplicados(dfLimpio:pd.DataFrame):
    dfLimpio = dfLimpio.drop_duplicates(subset=["Nombre", "Colonia", "Latitud", "Longitud"])
    print(dfLimpio.duplicated(subset=["Nombre", "Colonia", "Latitud", "Longitud"]).sum())
    print(dfLimpio.shape[0])
    return dfLimpio

#BORRAR COLUMNAS
#estas columnas se borraran por que tienen mas de un 60% de datos
def eliminarColumnas(dfLimpio: pd.DataFrame):
    dfLimpio=dfLimpio.drop(columns=["Num_Interior","Telefono","Sitio_internet","tipo_corredor_industrial", "nom_corredor_industrial","numero_local",
                                "Num_Exterior", "Correo_e","Razon_social","CP"])
    return dfLimpio

def revision(dfLimpio: pd.DataFrame):
    print(dfLimpio.columns)
    print(dfLimpio.isnull().sum())
    print(dfLimpio.isnull().sum() / len(dfLimpio))


if __name__=="__main__":
    estructura(dfLimpio)
    print("=====================================================")
    revisarNulos(dfLimpio)
    print("=====================================================")
    verDuplicados(dfLimpio)
    print("=====================================================")
    dfLimpio=eliminarDuplicados(dfLimpio)
    print("=====================================================")
    dfLimpio=eliminarColumnas(dfLimpio)
    print("=====================================================")
    revision(dfLimpio)

    dfLimpio.to_csv("farmaciasCompletoLimpio.csv", index=False)

