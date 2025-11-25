import pandas as pd

#aqui estoy leyendo el df ya limpio para poder hacer las agrpaciones
farmaciasCompletoLimpio=pd.read_csv("farmaciasCompletoLimpio.csv")

#¿Cuántas farmacias hay por municipio?
# aqui voy a agrupar por los municiopios y contar las farmacias .
def farmaciasMunicipio(farmaciasCompletoLimpio ):
    farmaciasXmunicipio=(farmaciasCompletoLimpio.groupby("Ubicacion")["Id"].count()
                     .reset_index(name="Numero_farmacias")
                     .sort_values("Numero_farmacias", ascending=False))
    return farmaciasXmunicipio


#¿Cuáles son las colonias con más farmacias en el estado en general?
#aqui agrupare por colonia y contare las farmacias
def farmaciasColonia(farmaciasCompletoLimpio):
    farmaciasXcolonias=(farmaciasCompletoLimpio.groupby("Colonia")["Id"].count()
                    .reset_index(name="Numero_farmacias")
                    .sort_values("Numero_farmacias", ascending=False))
    return farmaciasXcolonias


#¿Cómo se distribuyen las farmacias en el estado? hay distribucion por municipio y de ahi por colonia
def distribucionEstado(farmaciasCompletoLimpio):
    distribucionFarmaciasEstado=(farmaciasCompletoLimpio.groupby(["Ubicacion", "Colonia"])["Id"].count()
                       .reset_index(name="Numero_farmacias")
                       .sort_values(["Ubicacion", "Numero_farmacias"], ascending=[True,False]))
    return distribucionFarmaciasEstado


if __name__=="__main__":
    print(farmaciasMunicipio(farmaciasCompletoLimpio))
    print("==============================================")
    print(farmaciasColonia(farmaciasCompletoLimpio).head(10))
    print("===============================================")
    print(distribucionEstado(farmaciasCompletoLimpio).head(20))