import tensorflow as tf
import numpy as np
import os

# Load your pre-trained TensorFlow model
current_directory = os.getcwd()
model_path = os.path.join(current_directory, "vedavision_densenetv3.h5")

model = tf.keras.models.load_model(model_path)

# Define the image preprocessing function



def getPlant(preprocessed_image):
    predictions = model.predict(preprocessed_image)

    file_path = "./PlantsNameSeq1.txt"

    # Open the file in read mode
    plant_list = []
    with open(file_path, 'r') as file:
        # Read and print each line in the file
        for line in file:
            # print(line.strip())
            # strip() removes leading and trailing whitespace characters
            plant_list.append(line.strip())

    # class_names = sorted(os.listdir(directory_path))
    # Print the predicted class label
    plant_list.sort()

    max_index = np.argmax(predictions.flatten())

    # Get the maximum value
    max_value = predictions.flatten()

    sorted_flatten = sorted(max_value, reverse=True)

    indieces = []
    max_value = max_value.tolist()
    # print(type(max_value))
    indieces.append(max_value.index(sorted_flatten[0]))
    indieces.append(max_value.index(sorted_flatten[1]))
    indieces.append(max_value.index(sorted_flatten[2]))

    for index in indieces:
        print(plant_list[index])
    
    return indieces