import torch
from SNN import SiameseNetwork
import os
from face_detection import detect_faces
from face_detection import detect_faces_and_boxes
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.functional as F
from helper import imshow
import cv2

# Takes picture, extract faces, compares with the labled faces through SNN and writes name or Undefined

# Specify project folder as base_folder
# Python environment with the required libraries installed (e.g., PyTorch, OpenCV, Pillow).
# Pre-trained Siamese Network model weights saved as 'siamese_model_weights.pth' in the 'base_folder'.
# Images of known people in the 'instances' folder within the 'base_folder'.
# An input image ('demo_image.jpg') in the 'base_folder' for face recognition.

base_folder = '/home/hell/Documents/GitHub/MIT-into-to-CS/siamese'

# Load the model
model = SiameseNetwork()
# if torch.cuda.is_available():
#     model.cuda()
model.load_state_dict(torch.load(os.path.join(base_folder, 'siamese_model_weights.pth')))
model.eval()

# Save output image for processing
changed_img = cv2.imread(os.path.join(base_folder, 'demo_image.jpg'))
output_folder = base_folder
output_file = os.path.join(output_folder, 'output_image.jpg')
cv2.imwrite(output_file, changed_img)

# Preprocessing
preprocess = transforms.Compose([
    transforms.Resize((100, 100)),
    transforms.ToTensor()
])

# path to the folder containing the images of known people
folder_path = os.path.join(base_folder, 'instances')
# List all files in the folder
pictures_known_people = os.listdir(folder_path)

# get face crops and boxes from analyzed picture
faces_from_analyzed_picture, boxes_from_pic = detect_faces_and_boxes(os.path.join(base_folder, 'demo_image.jpg'))

# Compare each face crop from analyzed picture with the known people
for each_face, each_box in zip(faces_from_analyzed_picture, boxes_from_pic):

    imagetoprocess0 = Image.fromarray(each_face)
    imagetoprocess0 = imagetoprocess0.convert("L")
    normalized_image0 = preprocess(imagetoprocess0)
    normalized_image0 = normalized_image0.unsqueeze(0)

    for file_name in pictures_known_people:

        image_path = os.path.join(folder_path, file_name)
        face_known_person = detect_faces(image_path)
        imagetoprocess1 = Image.fromarray(face_known_person[0])
        imagetoprocess1 = imagetoprocess1.convert("L")

        # preprocessing to the image
        normalized_image1 = preprocess(imagetoprocess1)

        # unsqueeze the tensors
        normalized_image1 = normalized_image1.unsqueeze(0)

        # Move the tensors to the GPU if available
        # if torch.cuda.is_available():
        #     normalized_image0 = normalized_image0.cuda()
        #     normalized_image1 = normalized_image1.cuda()

        # Pass the images through the Siamese network
        output1, output2 = model(normalized_image1, normalized_image0)

        # Calculate the Euclidean distance between the two output feature vectors
        euclidean_distance = F.pairwise_distance(output1, output2)

        # Identify or Undefined
        if euclidean_distance.item() < 1:
          
          x, y, width, height = each_box['box']
          changed_img = cv2.imread(os.path.join(base_folder, 'output_image.jpg'))
          cv2.rectangle(changed_img, (x, y), (x + width, y + height), (0, 255, 0), 2)
          # Calculate the position for the text
          text_x = x
          text_y = y - 10
          cv2.putText(changed_img, file_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
          output_file = os.path.join(output_folder, 'output_image.jpg')
          cv2.imwrite(output_file, changed_img)
          break

        else:

          x, y, width, height = each_box['box']
          changed_img = cv2.imread(os.path.join(base_folder, 'output_image.jpg'))
          cv2.rectangle(changed_img, (x, y), (x + width, y + height), (0, 255, 0), 2)
          # Calculate the position for the text
          text_x = x
          text_y = y - 10
          cv2.putText(changed_img, "Undefined", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
          output_file = os.path.join(output_folder, 'output_image.jpg')
          cv2.imwrite(output_file, changed_img)
