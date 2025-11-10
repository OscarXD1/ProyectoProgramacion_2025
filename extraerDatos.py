import requests
import pandas as pd


def extraerDatos():
    #Token para usar la api de inegi
    token = "b97caaa8-e3c2-40f3-afd6-e5b300217c60"
    #Codigo que representa las farmacias
    codigo = "466330"
    palabra = "farmacias"
    #localidad
    ciudad = "005"
    estado = "02"
    inicio = "1"
    fin = "1500"


    url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/{palabra}/{estado}/{inicio}/{fin}/{token}"

    #Convertir a json lo que extraemos
    response = requests.get(url)
    data = response.json()
    #DATAFRAME DE TODAS LAS FARMACIAS DEL ESTADO
    df = pd.DataFrame(data)
    df.to_csv("farmaciasEstado.csv",index=False)


    #FILTRAR POR LA COLUMNA UBICACION SOLAMENTE A FARMACIAS DE TIJUANA
    #dfTijuana = df[df['Ubicacion'] == "TIJUANA, Tijuana, BAJA CALIFORNIA"]
    #dfTijuana.to_csv("farmaciasTijuana.csv",index=False)


    #print(len(df))
    print("LISTO :)")
if __name__ == "__main__":
    extraerDatos()
