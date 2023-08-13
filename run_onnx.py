#region imports
import os
import cv2
import onnx
import json
import time
import pathlib
import warnings
import numpy as np
import onnxruntime
warnings.filterwarnings("ignore")
#endregion
#--------------------------------------------------



#region Load Model
# Load ONXX Model
onnx_model_path = "/home/docker_transfer/onnx_models/onnx_mobilenet_fine.onnx"

session = onnxruntime.InferenceSession(onnx_model_path, None)
loaded_model = session
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
#endregion
#--------------------------------------------------



#region model inference
# To run the model on test folder and make the predictions
def model_inference_on_test_images(folder_path, loaded_model):
    img_height, img_width = (160,160)
    class_labels = []


    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Loop through each file in the list
    for file_name in file_list:
        if file_name.endswith(".jpg"):
            # Construct the full path of the image
            image_path = os.path.join(folder_path, file_name)

            # Read the image using OpenCV
            img = cv2.imread(image_path)

            img.resize( 1,img_height, img_width,3)
            data = img

            data = json.dumps({'data': img.tolist()})
            data = np.array(json.loads(data)['data']).astype('float32')

            data = data / 255.0

            result = session.run([output_name], {input_name: data})
            prediction=int(np.argmax(np.array(result).squeeze(), axis=0))
            
            class_labels.append(prediction)
#endregion



#region test image folders
totaltime = 0
start = time.time()

test_images_folder0 = "/home/docker_transfer/DATA/testing/Acne/"
model_inference_on_test_images(test_images_folder0,loaded_model)

test_images_folder1 = "/home/docker_transfer/DATA/testing/Actinic Keratosis/"
model_inference_on_test_images(test_images_folder1,loaded_model)

test_images_folder2 = "/home/docker_transfer/DATA/testing/Basal Cell Carcinoma/"
model_inference_on_test_images(test_images_folder2,loaded_model)

test_images_folder3 = "/home/docker_transfer/DATA/testing/Eczemaa/"
model_inference_on_test_images(test_images_folder3,loaded_model)

test_images_folder4 = "/home/docker_transfer/DATA/testing/Rosacea/"
model_inference_on_test_images(test_images_folder4,loaded_model)

end = time.time()

totaltime = end - start
#endregion
#--------------------------------------------------


print("##### Training was completed in ",totaltime," seconds. #####")
print("##### 1 Image is analyzed in ",totaltime/185.0," seconds. #####")

