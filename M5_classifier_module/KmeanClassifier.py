from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import tomli
import os
import matplotlib.pyplot as plt

class KmeanClassifier:

    """ Init classifier parameters """
    def __init__(self, dir):
        self.dir = dir
        self.data_set_train = [self.load_dataset(os.path.join(self.dir, "DataTrain_random.csv"))][0]
        self.datatrain_labels = [self.load_dataset(os.path.join(self.dir, "DataTrain_labels_random.csv"))][0]
        self.train_labels_binary = self.labels_binary(self.datatrain_labels, 'P', 0)

    """ Load dataset from the folder """
    def load_dataset(self, filepath):
        with open(filepath) as f:
            matrix = f.read()
            matrix = tomli.loads(matrix)['pr']
        return matrix

    """ Binarice the labels """
    def labels_binary(self, labels, param, pos):
        labels_binary = []
        for l in labels:
            if l[pos] == param:
                labels_binary.append(1)
            else:
                labels_binary.append(0)
        return labels_binary
    
    """ Check the results of the classification """
    def tester (self, expected_labels, obtained_labels):
        # Compare the results obtained with those expected [T=0, P=1].
        i = 0
        aciertos = 0
        fallos = []
        for l in obtained_labels:
            if (l - expected_labels[i] == 0):
                aciertos = aciertos + 1
            else:
                fallos.append(expected_labels[i])
            i = i + 1
        return aciertos, fallos
    
    """ For finding an especific data """
    def check (self, data, labels, x):
        check = []
        for i in range(len(data)):
            if abs(data[i][0] + x) < 0.0001:
                check.append([labels[i], data[i]])
        return check

    """ Launch and plot the classifier """
    def fit_predict(self, data_test):
        # Classify between flat and tubular
        kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto")
        kmeans.fit(self.data_set_train)
        labels_train = kmeans.labels_

        centroides = kmeans.cluster_centers_

        aciertos, fallos = self.tester(self.train_labels_binary, labels_train)
        print(f"Aciertos data train: {aciertos} / {len(labels_train)}, --> {(aciertos*100/len(labels_train))}%")

        # With the trained classifier we classify the last wound as a test.
        data_test = np.array(data_test).reshape(1, -1)
        label_test = kmeans.predict(data_test)

        for i in range(len(self.data_set_train)):
            if (self.train_labels_binary[i] == 0):
                plt.scatter(self.data_set_train[i][0], self.data_set_train[i][1], color='blue')
            else:
                plt.scatter(self.data_set_train[i][0], self.data_set_train[i][1], color='green')
        
        # Creates a scatter plot
        # Tubular in green and flat in blue
        
        # Labels for the legend
        legend_labels = ["Plana", "Tubular", "Centroide"]

        # Empty lists for storing points of each type
        points_train = [[] for _ in range(len(legend_labels))]
        points_test = [[] for _ in range(len(legend_labels))]

        # Assign points to the corresponding lists
        for i in range(len(self.data_set_train)):
            points_train[labels_train[i]].append((self.data_set_train[i][0], self.data_set_train[i][1]))

        for i in range(len(data_test)):
            points_test[label_test[i]].append((data_test[i][0], data_test[i][1]))

        # Generate the scatter plot for each type of scatter plot
        for i in range(len(legend_labels)):
            if len(points_train[i]) > 0:
                plt.scatter(*zip(*points_train[i]), color='blue' if i == 0 else 'green', label=legend_labels[i])

        for i in range(len(legend_labels)):
            if len(points_test[i]) > 0:
                plt.scatter(*zip(*points_test[i]), color='blue' if i == 0 else 'green', marker='x')

        # Scatter de centroids
        plt.scatter(centroides[:, 0], centroides[:, 1], color='red', marker='*', label=legend_labels[2])

        # Add axis and title labels
        plt.xlabel('Media Curvatura Gaussiana')
        plt.ylabel('Media Curvatura Media')
        plt.title('Gráfico de Dispersión')

        # Show legend
        plt.legend(loc='upper left')
        plt.show()

        return label_test       
      
        

    