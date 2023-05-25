## DATA SET MAKER code ##

# Standar library imports
import numpy as np  
import os
import tomli
from sklearn.model_selection import train_test_split

def load_data_set(dir_path):
    files = os.listdir(dir_path)
    data_set = []
    labels = []
    for f in files:
        if f.endswith('.csv'):
            with open(os.path.join(dir_path, f)) as file:
                matrix = tomli.loads(file.read())['pr']
                labels.append(os.path.splitext(os.path.basename(file.name))[0])
                data_set.append(matrix)
    return data_set, labels

def main():
    #flat_dir = "/home/duna/Escritorio/TFG sutura quirurgica/UMA_MallaColisiones/PYTHON/CameraFeature/DataTrain/Flat"
    #tubular_dir = "/home/duna/Escritorio/TFG sutura quirurgica/UMA_MallaColisiones/PYTHON/CameraFeature/DataTrain/Tubular"
    flat_dir = "/home/labrob2022/Desktop/UMA_MallaColisiones/PYTHON/CameraFeature/DataTrain/Flat"
    tubular_dir = "/home/labrob2022/Desktop/UMA_MallaColisiones/PYTHON/CameraFeature/DataTrain/Tubular"

    data_set_flat, labels_flat = load_data_set(flat_dir)
    data_set_tubular, labels_tubular = load_data_set(tubular_dir)
    data_set = data_set_flat + data_set_tubular
    labels_set = labels_flat + labels_tubular

    data_train, data_test, train_labels, test_labels = train_test_split(data_set, labels_set, test_size=0.2)

    with open('M5_classifier_module/DataTrain_random.csv', 'w') as f:
        info = "pr = " + str(data_train)
        f.write(info)
    f.close()

    with open('M5_classifier_module/DataTest_random.csv', 'w') as f:
        info = "pr = " + str(data_test)
        f.write(info)
    f.close()

    with open('M5_classifier_module/DataTrain_labels_random.csv', 'w') as f:
        info = "pr = " + str(train_labels)
        f.write(info)
    f.close()

    with open('M5_classifier_module/DataTest_labels_random.csv', 'w') as f:
        info = "pr = " + str(test_labels)
        f.write(info)
    f.close()

    print("Finish!")

if __name__ == "__main__":
    try:
        main()
    except:
        print('An error has ocurred')
        pass