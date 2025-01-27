import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization # type: ignore

def create_cnn(input_shape=(128, 128, 3), num_classes=4):
    """
    Crea una arquitectura básica de CNN ajustada para imágenes de 128x128.

    Args:
        input_shape (tuple): Dimensiones de entrada de las imágenes (128, 128, 3).
        num_classes (int): Número de clases a predecir (e.g., 4 para los palos de póker).

    Returns:
        model: Modelo de Keras listo para compilar y entrenar.
    """
    model = Sequential()

    # Primera capa de convolución + MaxPooling
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())

    # Segunda capa de convolución + MaxPooling
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())

    # Tercera capa de convolución + MaxPooling
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())

    # Cuarta capa de convolución (opcional, dado el tamaño mayor)
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(BatchNormalization())

    # Aplanamiento y capas densas
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))  # Regularización para evitar overfitting
    model.add(Dense(num_classes, activation='softmax'))  # Salida con 'softmax' para clasificación

    return model



