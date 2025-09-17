import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/xime/Desktop/Portafolio/M4/olimpicos.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")

print("Primeras 5 filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nTipo de variables por columna:")
print(df.dtypes)

print("\nMedia de edad:", df["edad"].mean())
print("Media de entrenamientos semanales:", df["entrenamientos_semanales"].mean())
print("Media de medallas totales:", df["medallas_totales"].mean())

sns.histplot(df["entrenamientos_semanales"], bins=10, kde=True)
plt.title("Distribución de Entrenamientos Semanales")
plt.xlabel("Entrenamientos Semanales")
plt.ylabel("Frecuencia")
plt.show()

sns.histplot(df["medallas_totales"], bins=10, kde=True)
plt.title("Distribución de Medallas Totales")
plt.xlabel("Medallas Totales")
plt.ylabel("Frecuencia")
plt.show()