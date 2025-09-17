import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

grupo_A = np.array([85, 90, 78, 88, 92, 80, 86, 89, 84, 87, 91, 82, 83, 85, 88])
grupo_B = np.array([70, 72, 75, 78, 80, 68, 74, 76, 79, 77, 73, 71, 75, 78, 80])

mean_A, std_A = np.mean(grupo_A), np.std(grupo_A, ddof=1)
mean_B, std_B = np.mean(grupo_B), np.std(grupo_B, ddof=1)

print("Media Grupo A (Tutoría):", mean_A)
print("Desviación Estándar Grupo A:", std_A)
print("Media Grupo B (Control):", mean_B)
print("Desviación Estándar Grupo B:", std_B)

plt.hist(grupo_A, bins=5, alpha=0.6, label="Grupo A (Tutoría)")
plt.hist(grupo_B, bins=5, alpha=0.6, label="Grupo B (Control)")
plt.xlabel("Puntaje")
plt.ylabel("Frecuencia")
plt.title("Histogramas de Rendimiento Académico")
plt.legend()
plt.show()

plt.boxplot([grupo_A, grupo_B], labels=["Grupo A", "Grupo B"])
plt.ylabel("Puntaje")
plt.title("Diagrama de Caja")
plt.show()

t_stat, p_value = stats.ttest_ind(grupo_A, grupo_B, equal_var=False)

print("\nPrueba t:")
print("Estadístico t:", t_stat)
print("Valor p:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Se rechaza H0: El programa de tutoría mejora el rendimiento académico.")
else:
    print("No se rechaza H0: No hay evidencia suficiente de mejora.")

diff_means = mean_A - mean_B

se = np.sqrt(std_A**2/len(grupo_A) + std_B**2/len(grupo_B))

t_crit = stats.t.ppf(1 - alpha/2, df=len(grupo_A)+len(grupo_B)-2)
ci_low = diff_means - t_crit * se
ci_high = diff_means + t_crit * se

print("\nIntervalo de Confianza 95% para la diferencia de medias:")
print(f"({ci_low:.2f}, {ci_high:.2f})")

if ci_low > 0:
    print("Interpretación: El intervalo es positivo, lo que indica que el grupo con tutoría tiene mayor rendimiento.")
else:
    print("Interpretación: El intervalo incluye 0, por lo que no hay evidencia concluyente.")
