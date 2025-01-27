import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical # type: ignore
import model as nn
import matplotlib.pyplot as plt

import os
import numpy as np


def load_data_from_npy(data_dir, num_classes):
    print("Load data")
    """
    Carga imágenes desde archivos .npy y genera etiquetas basadas en los nombres de los archivos.

    Args:
        data_dir (str): Ruta a la carpeta de datos (e.g., 'train', 'val', 'test').
        num_classes (int): Número total de clases.

    Returns:
        X (np.array): Array de imágenes cargadas.
        y (np.array): Array de etiquetas codificadas en formato one-hot.
    """
    X = []  # Lista para imágenes
    y = []  # Lista para etiquetas

    # Definir un mapeo de clases a índices
    class_map = {
        "corazon": 0,
        "picas": 1,
        "diamante": 2,
        "trevol": 3
    }

    # Recorrer todos los archivos en el directorio
    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        print(f"Data load from {file_path}")

        if file_name.endswith(".npy"):
            # Cargar la imagen desde el archivo .npy
            image = np.load(file_path)
            X.append(image)

            # Extraer la etiqueta desde el nombre del archivo
            for class_name in class_map.keys():
                if class_name in file_name:
                    y.append(class_map[class_name])
                    break

    # Convertir listas a arrays de NumPy
    X = np.array(X)
    y = np.array(y)

    # Codificar las etiquetas como one-hot
    y = to_categorical(y, num_classes=num_classes)

    print(f"Datos cargados desde {data_dir}: {len(X)} imágenes")
    return X, y




train_dir = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\train"
val_dir = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\val"
test_dir = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\test"

# Número total de clases
num_classes = 4

# Cargar los conjuntos de datos
X_train, y_train = load_data_from_npy(train_dir, num_classes)
X_val, y_val = load_data_from_npy(val_dir, num_classes)
X_test, y_test = load_data_from_npy(test_dir, num_classes)

# Verificar formas
print("Forma de X_train:", X_train.shape)
print("Forma de y_train:", y_train.shape)



# Crear el modelo ajustado para imágenes 128x128
input_shape = (128, 128, 3)  # Dimensiones de las imágenes preprocesadas
num_classes = 4  # Número de clases (As_trebol, As_picas, etc.)
model = nn.create_cnn(input_shape, num_classes)

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Si usas one-hot encoding
              metrics=['accuracy'])

# Mostrar resumen del modelo
model.summary()


# Entrenar el modelo
epochs = 20
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=epochs,
    batch_size=32
)

# Guardar el modelo entrenado
model.save("modelo_cnn_cartas_poker.h5")
print("Modelo guardado como modelo_cnn_cartas_poker.h5")


#Graficas
# Graficar la pérdida y precisión
def plot_training_history(history):
    # Pérdida
    plt.figure()
    plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
    plt.plot(history.history['val_loss'], label='Pérdida de validación')
    plt.title('Pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    plt.show()

    # Precisión
    plt.figure()
    plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
    plt.plot(history.history['val_accuracy'], label='Precisión de validación')
    plt.title('Precisión durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Precisión')
    plt.legend()
    plt.show()

# Graficar los resultados
plot_training_history(history)