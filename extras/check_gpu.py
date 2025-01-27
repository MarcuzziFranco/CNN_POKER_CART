import tensorflow as tf
print(tf.__version__)

print("Dispositivos disponibles:")
for device in tf.config.list_physical_devices():
    print(device)


print(tf.config.list_physical_devices("GPU"))

tf.debugging.set_log_device_placement(True)

