import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de validación o testeo
def load_data_from_npy(data_dir, num_classes):
    print("Cargando datos para evaluación...")
    X = []
    y = []

    class_map = {
        "corazon": 0,
        "picas": 1,
        "diamante": 2,
        "trevol": 3
    }

    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        print(file_path)
        if file_name.endswith(".npy"):
            image = np.load(file_path)
            X.append(image)

            for class_name in class_map.keys():
                if class_name in file_name:
                    y.append(class_map[class_name])
                    break

    X = np.array(X)
    y = np.array(y)
    y = tf.keras.utils.to_categorical(y, num_classes=num_classes)

    print(f"Datos cargados desde {data_dir}: {len(X)} imágenes")
    return X, y

# Ruta del conjunto de validación o testeo
val_dir = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\val"
test_dir = "C:\\Users\\Franco\\Desktop\\CNN_POKER_CART\\data\\test"
num_classes = 4

# Cargar los datos de validación o testeo
X_val, y_val = load_data_from_npy(val_dir, num_classes)
X_test, y_test = load_data_from_npy(test_dir, num_classes)

# Cargar el modelo entrenado
model_path = "modelo_cnn_cartas_poker.h5"
print(f"Cargando modelo desde {model_path}...")
model = load_model(model_path)

# Evaluar en el conjunto de validación
print("\nEvaluando en el conjunto de validación:")
val_loss, val_accuracy = model.evaluate(X_val, y_val, batch_size=32)
print(f"Pérdida en validación: {val_loss:.4f}")
print(f"Precisión en validación: {val_accuracy:.4f}")

# Evaluar en el conjunto de testeo
print("\nEvaluando en el conjunto de testeo:")
test_loss, test_accuracy = model.evaluate(X_test, y_test, batch_size=32)
print(f"Pérdida en testeo: {test_loss:.4f}")
print(f"Precisión en testeo: {test_accuracy:.4f}")

# Predicciones en el conjunto de testeo
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Matriz de confusión y reporte de clasificación
print("\nMatriz de confusión:")
print(confusion_matrix(y_true, y_pred_classes))

print("\nReporte de clasificación:")
print(classification_report(y_true, y_pred_classes, target_names=["corazon", "picas", "diamante", "trevol"]))

# Visualización de algunas predicciones incorrectas
def plot_incorrect_predictions(X, y_true, y_pred_classes, class_names):
    incorrect = np.where(y_true != y_pred_classes)[0]
    print(f"Mostrando {len(incorrect)} predicciones incorrectas...")

    plt.figure(figsize=(12, 8))
    for i, idx in enumerate(incorrect[:9]):  # Mostrar hasta 9 imágenes
        plt.subplot(3, 3, i + 1)
        plt.imshow(X[idx])
        plt.title(f"Verdadero: {class_names[y_true[idx]]}\nPredicho: {class_names[y_pred_classes[idx]]}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Visualizar predicciones incorrectas
plot_incorrect_predictions(X_test, y_true, y_pred_classes, ["corazon", "picas", "diamante", "trevol"])