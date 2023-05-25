# TFG_Duna
TFG realizado por Duna de Luis en el curso 2022-2023 en el laboratorio de robótica médica de la Universidad de Málaga

Autora: Duna de Luis Moura (DNI: 78980830A)
Tutora: Dra. Isabel García Morales
Co-tutor: Álvaro Galán Cuenca

## Título:
### Detección de heridas en imágenes RGB-D integrado en un sistema ciberfísico para la asistencia a la sutura laparoscópica.
#### Palabras clave:
cirugía laparoscópica, sutura quirúrgica robotizada, cámara RGB-D, gradiente de profundidad, estimación de puntos de sutura.

## Resumen:
La cirugía laparoscópica robotizada es una técnica quirúrgica avanzada en la que se emplea un sistema robótico para llevar a cabo intervenciones mínimamente invasivas en el abdomen del paciente. Este enfoque combina la laparoscopia, que implica la realización de pequeñas incisiones por las que se introducen instrumentos quirúrgicos miniaturizados, con la tecnología robótica, permitiendo que estos sistemas asistan a los cirujanos en determinadas maniobras quirúrgicas. 
En este contexto, el trabajo desarrollado se ha centrado específicamente en la maniobra de sutura con el objetivo de demostrar el potencial de las cámaras RGB-D en la detección precisa de heridas, sobre las que se calcularán las coordenadas de los puntos de sutura necesarios para llevar a cabo dicha maniobra. Para ello, se ha desarrollado una aplicación que automatiza la detección de heridas empleando datos de profundidad capturados por una cámara RGB-D dentro de la cavidad abdominal del paciente durante la intervención quirúrgica y adapta el cálculo de los puntos de sutura en función de las características de la herida detectada.
Este enfoque innovador ha demostrado su eficacia al detectar los contornos de las heridas en diversas situaciones, abriendo nuevas posibilidades para mejorar la precisión y eficiencia en la sutura autónoma de heridas durante este tipo de procedimientos. La aplicación desarrollada se integra en un dos proyectos en desarrollo por el departamento de investigación en Robótica Médica de la UMA, un sistema robótico y otro ciberfísico, a los que se enviarán las coordenadas de la trayectoria generada.

### Explicación de repositorio
#### DataTrain
Contiene 69 ficheros csv con los dos descriptores utilizados para clasificar cada herida (media de la curvatura Media y Gaussiana). Organizados en tres carpetas: Flat con las heridas planas, Tubular con las heridas tubulares de radio 2.5 cm y Nuevas con heridas tubulares de radios 2 y 3 cm. Cada fichero está nombrado con 3 o 4 letras, seguido de "_img" y un número (por ejemplo "HPF_img1"), la primera letra indica Horizontal o Inclinada, la segunda Plana o Tubular y la tercera y cuarta indica Fina, Mediana y Gruesa. Las heridas nuevas se indican como: N, NN y n. Donde N son heridas de 2cm de radio en un soporte corto (20 cm de longitud), NN de radio 2cm y soporte de 25 cm de longitud y n de radio 3cm. La numeración indica distintas poses y ángulo de inclinación de cada tipo de herida.

####  M1_acquisition_module
Contiene la clase Camera donde se definen todas las funciones necesarias para trabajar con esta, como son establecer sus parámetros, obtener la imagen, calcular la banda de píxeles inválidos, establecer la resolución, etc.

#### M2_processing_module
Contienes las clases Filters y Utilities. En Filters se han definido todos los métodos de procesamiento de imagenes utilizados en el proyecto (por ejemplo interpolación, gradiente, suavizado) y en Utilities las herramientas utilizadas (generador de gráficas 3D y 2D, color bar, rotaciones y transformaciones homogéneas, etc). La función nextNeighbour.py se utiliza en el filtro de interpolación para calcular la media de los vecinos más cercanos NO nulos.

#### M3_wound_detection_module
Se crea la clase Wound donde se definen las herramientas utilizadas para detectar la herida, obtener sus parámetros principales, la ROI, su curvatura, la malla de colisiones, etc.

#### M5_classifier_module
Aparecen una función, 4 ficheros y una clase. La función DataSet_maker.py se encarga de leer todos los descriptores almacenados en el DataTrain y repartirlos de forma aleatoria en el fichero de DataTest_random y DataTrain_random. Se guardan tambien los nombres de los ficheros para poder comprobar los resultados de la clasificación con los reales. La clse KmeanClassifier accede a los ficheros, entrena el clasificador y a partir de los descriptores que se le pasen de la herida realiza la clasificación, devolviendo un valor de 0 o 1 en función de si ha clasificado la herida como plana o como tubular.

#### M6_ros_service_module
Contiene el catkin_ws con los ficheros necesarios para ejecutar el servidor ROS. Para ello, en el paquete camera_pkg se definen dos srv: CameraData y UserReq, el primero publicará datos en el servidor y el segundo los solictará. Para ello, se definen 3 scripts, el nodo camera_client.py que utilizando el sevicio CameraData envia los datos al servidor. El nodo user_client.py solicita dichos datos y el servidor camera_server.py se encarga de almacenarlos y gestionar las peticiones respuesta realizadas. Los datos son el número y coordenadas de los puntos de sutura.

#### main.py
Accede a cada una de las funciones y módulos descritos para cumplir con el propósito de la aplicación: detectar heridas y calcular los puntos de sutura y bias sobre estas.

#### requirements.txt
Se recogen las versiones de cada una de las librerias utilizadas con las que la aplicación funciona actualmente.
