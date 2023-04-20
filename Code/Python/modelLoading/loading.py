import numpy as np
import tensorflow as tf
import cv2
import pathlib

classes2 = np.array(['apple', 'banana', 'carrot', 'kiwi', 'lettuce', 'orange'])

# Load:
interpreter = tf.lite.Interpreter(model_path="/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Code/Python/modelLoading/modelV3.tflite")

# Input Output Tensors:
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# Print
print(input_details)
print(output_details)

img = cv2.imread("/Users/natalgrima/School/Natal-Grima-SWD-63A-Thesis/Code/Python/modelLoading/Banana_36.jpg")

new_img = cv2.resize(img, (224,224), interpolation=cv2.INTER_CUBIC)
new_img = new_img.astype(np.float32)
new_img /= 255.

# Index That Accepts Input:
interpreter.set_tensor(input_details[0]['index'], [new_img])

# Run:
interpreter.invoke()

# Output:
output_data = interpreter.get_tensor(output_details[0]['index'])

print('output:')
print(output_data)

#
output_max = output_data.max()
output_index = output_data.argmax()

# Prints for Testing:
print('input')
print(input_details)
print('output')
print(output_details)
print('index')
print(output_index)
print('class')
print(classes2[output_index])