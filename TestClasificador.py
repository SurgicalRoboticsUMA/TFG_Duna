import M5_classifier_module.KmeanClassifier as kmean
import tomli
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib import rcParams

def load_dataset(filepath):
        with open(filepath) as f:
            matrix = f.read()
            matrix = tomli.loads(matrix)['pr']
        return matrix

def labels_binary(labels, param, pos):
        labels_binary = []
        for l in labels:
            if l[pos] == param:
                labels_binary.append(1)
            else:
                labels_binary.append(0)
        return labels_binary

def tester (self, expected_labels, obtained_labels):
        # Comparamos los resultados obtenidos con los esperados [T=1, P=0]
        i = 0
        aciertos = 0
        fallos = []
        for l in obtained_labels:
            if (l - expected_labels[i] == 0):
                aciertos = aciertos + 1
            else:
                fallos.append(expected_labels[0][i])
            i = i + 1
        return aciertos, fallos

dir = "/home/duna/Escritorio/TFG sutura quirurgica/UMA_MallaColisiones/PYTHON/CameraFeature/M5_classifier_module"
#dir = "/home/labrob2022/Desktop/UMA_MallaColisiones/PYTHON/CameraFeature/M5_classifier_module"
   
data_test = [load_dataset(os.path.join(dir, "DataTest_random.csv"))][0]
datatest_labels = [load_dataset(os.path.join(dir, "DataTest_labels_random.csv"))][0]

data_train = [load_dataset(os.path.join(dir, "DataTrain_random.csv"))][0]
datatrain_labels = [load_dataset(os.path.join(dir, "DataTrain_labels_random.csv"))][0]

test_labels_binary = labels_binary(datatest_labels, 'P', 1)
train_labels_binary = labels_binary(datatrain_labels, 'P', 1)

# Especificar centroides iniciales
initial_centroids = np.array([[0.1, 0.1], [-0.001, 0.001]])

# Clasificar entre plano y curvo
kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto")
kmeans.fit(data_train)
labels_train = kmeans.labels_

centroides = kmeans.cluster_centers_

# Comparamos los resultados obtenidos con los esperados [T=0, P=1]
i = 0
aciertos = 0
fallos = []
for l in labels_train:
    if (l - train_labels_binary[i] == 0):
        aciertos = aciertos + 1
    else:
        fallos.append(datatrain_labels[i])
    i = i + 1

#print(f"Cantidad de muestras: {len(data_train)+len(data_test)}")
#print(f"Aciertos data train: {aciertos} / {len(labels_train)}, --> {(aciertos*100/len(labels_train))}%")

""" check = []
for i in range(len(data_test)):
    if abs(data_test[i][0] + 0.00534) < 0.0001:
        check.append([datatest_labels[i], data_test[i]])
print(check) """

# Con el clasificador entrenado clasificamos la herida pasada como test
label_test = kmeans.predict(data_test)

# Comparamos los resultados obtenidos con los esperados [T=0, P=1]
i = 0
aciertos = 0
for l in label_test:
    if (l - test_labels_binary[i] == 0):
        aciertos = aciertos + 1
    else:
        fallos.append(datatest_labels[i])
    i = i + 1

#print(f"Aciertos data test: {aciertos} / {len(label_test)}, --> {(aciertos*100/len(label_test))}%")
#print(f"Fallos -> {fallos}")

# Change the impression parameters globally
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 18

legend_labels = ["Plana", "Tubular mediana", "Tubular grande", "Tubular pequeña", "Centroide"]
#legend_labels = ["Plana", "Tubular", "Centroide"]

# Listas vacías para almacenar puntos de cada tipo
points_train = [[] for _ in range(len(legend_labels))]
points_test = [[] for _ in range(len(legend_labels))]

# Asignar puntos a las listas correspondientes
for i in range(len(data_train)):
    points_train[labels_train[i]].append((data_train[i][0], data_train[i][1]))

for i in range(len(data_test)):
    points_test[label_test[i]].append((data_test[i][0], data_test[i][1]))

# Generar la gráfica de puntos (scatter) para cada tipo
for i in range(len(legend_labels)):
    if len(points_train[i]) > 0:
        plt.scatter(*zip(*points_train[i]), color='blue' if i == 0 else 'green' if i == 1 else 'orange' if i == 2 else 'magenta', label=legend_labels[i])

for i in range(len(legend_labels)):
    if len(points_test[i]) > 0:
        plt.scatter(*zip(*points_test[i]), color='blue' if i == 0 else 'green' if i == 1 else 'orange' if i == 2 else 'magenta', marker='x')

# Scatter de centroides
plt.scatter(centroides[:, 0], centroides[:, 1], color='red', marker='*', label=legend_labels[4])

# Agrega etiquetas de eje y título
plt.xlabel('Media Curvatura Gaussiana')
plt.ylabel('Media Curvatura Media')
plt.title('Gráfico de Dispersión')

# Mostrar leyenda
plt.legend(loc='upper left')
plt.show()