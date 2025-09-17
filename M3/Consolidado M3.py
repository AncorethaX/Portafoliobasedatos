import pandas as pd
import numpy as np

df = pd.read_csv("/Users/xime/Desktop/Portafolio/M3/migracion.csv")
print(df.head())

print("Valores nulos por columna:\n", df.isnull().sum())

for col in df.select_dtypes(include=[np.number]).columns:
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include=[object]).columns:
    df[col].fillna("Desconocido", inplace=True)

for col in ["Cantidad_Migrantes"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    filtro = (df[col] >= (Q1 - 1.5*IQR)) & (df[col] <= (Q3 + 1.5*IQR))
    df = df[filtro]

mapa_razones = {
    "Económica": "Trabajo",
    "Conflicto": "Guerra",
    "Educación": "Estudio",
    "Climática": "Desastre Natural"
}
df["Razon_Migracion"] = df["Razon_Migracion"].replace(mapa_razones)


print("\nPrimeras 5 filas:\n", df.head())
print("\nInformación general:\n")
df.info()
print("\nDescripción estadística:\n", df.describe())

media_migrantes = df["Cantidad_Migrantes"].mean()
mediana_migrantes = df["Cantidad_Migrantes"].median()
print("\nMedia migrantes:", media_migrantes)
print("Mediana migrantes:", mediana_migrantes)

print("\nPIB Promedio País Origen:", df["PIB_Origen"].mean())
print("PIB Promedio País Destino:", df["PIB_Destino"].mean())

print("\nConteo por razón de migración:\n", df["Razon_Migracion"].value_counts())

print("\nMigrantes por razón:\n", df.groupby("Razon_Migracion")["Cantidad_Migrantes"].sum())

print("\nMedia IDH Origen por razón:\n", df.groupby("Razon_Migracion")["IDH_Origen"].mean())

df = df.sort_values(by="Cantidad_Migrantes", ascending=False)

conflicto = df[df["Razon_Migracion"] == "Guerra"]
print("\nMigraciones por conflicto:\n", conflicto)

alto_idh = df[df["IDH_Destino"] > 0.90]
print("\nMigraciones con IDH destino > 0.90:\n", alto_idh)

df["Diferencia_IDH"] = df["IDH_Origen"] - df["IDH_Destino"]

df.to_csv("Migracion_Limpio.csv", index=False)
print("\nArchivo final exportado como 'Migracion_Limpio.csv'")