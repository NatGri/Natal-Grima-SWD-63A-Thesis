import numpy as np
import tensorflow as tf

# Load:
interpreter = tf.lite.Interpreter(model_path="model.tflite")

# Input Output Tensors:
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# Print
print(input_details)
print(output_details)
