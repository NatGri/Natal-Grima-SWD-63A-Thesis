import numpy as np
import tensorflow as tf
import cv2
import pathlib

# Classes:
classes = np.array(['apple', 'banana', 'beetroot', 'bellpepper', 'cabbage', 'carrot', 'cauliflower', 'chilli pepper',
                    'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'kiwi', 'lemon', 'lettuce',
                    'mango', 'onion', 'orange', 'pear', 'pineapple', 'pomegranate', 'potato', 'radish',
                    'spinach', 'sweet potato', 'tomato', 'turnip', 'watermelon'])


def detect(model_path, image_path):
    # Load Model:
    interpreter = tf.lite.Interpreter(model_path=model_path)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.allocate_tensors()

    # Passing Image:
    for file in pathlib.Path(image_path).iterdir():
        img = cv2.imread(r"{}".format(file.resolve()))

        new_img = cv2.resize(img, (224,224), interpolation=cv2.INTER_CUBIC)
        new_img = new_img.astype(np.float32)
        new_img /= 255.

        # Index That Accepts Input:
        interpreter.set_tensor(input_details[0]['index'], [new_img])

        # Run:
        interpreter.invoke()

        # Output:
        output_data = interpreter.get_tensor(output_details[0]['index'])

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
        print(classes[output_index])

        # Return:
        return classes[output_index]
