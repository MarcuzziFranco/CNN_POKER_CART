import os
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model # type: ignore

# Cargar el modelo entrenado
model_path = "modelo_cnn_cartas_poker.h5"
print(f"Cargando modelo desde {model_path}...")
model = load_model(model_path)

# Mapeo de clases
class_map = {
    0: "corazon",
    1: "picas",
    2: "diamante",
    3: "trevol"
}

# Procesar cada frame para que sea compatible con el modelo
def preprocess_frame(frame):
    # Redimensionar al tamaño esperado por el modelo
    frame_resized = cv2.resize(frame, (128, 128))
    # Normalizar valores de píxeles
    frame_normalized = frame_resized / 255.0
    # Expandir dimensiones para que sea compatible con el modelo (1, 128, 128, 3)
    frame_expanded = np.expand_dims(frame_normalized, axis=0)
    return frame_expanded

# Detección en tiempo real con la cámara
cap = cv2.VideoCapture(0)  # Usa la cámara por defecto

if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al capturar el frame.")
        break

    # Preprocesar el frame
    processed_frame = preprocess_frame(frame)

    # Realizar la predicción
    predictions = model.predict(processed_frame)
    predicted_class = np.argmax(predictions)
    predicted_class = int(np.argmax(predictions))  # Convertir a int explícitamente
    class_name = class_map[predicted_class]
    confidence = predictions[0][predicted_class]

    # Dibujar un recuadro y mostrar la clase predicha
    height, width, _ = frame.shape
    cv2.rectangle(frame, (50, 50), (width - 50, height - 50), (0, 255, 0), 2)
    cv2.putText(
        frame,
        f"{class_name} ({confidence:.2f})",
        (60, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Mostrar el frame en una ventana
    cv2.imshow('Detección en tiempo real', frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()