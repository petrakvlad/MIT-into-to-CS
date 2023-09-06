import torch
from SNN import SiameseNetwork
import os
from face_detection import detect_faces
from face_detection import detect_faces_and_boxes
import torchvision.transforms as transforms
from PIL import Image
import torchvision.utils
import torch.nn.functional as F
from helper import imshow
import cv2


# Load the model
model = SiameseNetwork().cuda()
model.load_state_dict(torch.load('/home/hell/Documents/GitHub/MIT-into-to-CS/siamese/siamese_model_weights.pth'))

model.eval()  # Set the network to evaluation mode


# folder containing the images of known people
folder_path = '/home/hell/Documents/GitHub/MIT-into-to-CS/siamese/instances'

# List all files in the folder of known people
pictures_known_people = os.listdir(folder_path)


# Get face crops from target picture
faces_from_analyzed_picture, boxes_from_pic = detect_faces_and_boxes("/home/hell/Documents/GitHub/MIT-into-to-CS/siamese/demo_image.jpg")


# Save output image which will be changed in the process as faces will be recognized
final_image_with_boxes = cv2.imread('/home/hell/Documents/GitHub/MIT-into-to-CS/siamese/demo_image.jpg')
output_folder = '/home/hell/Documents/GitHub/MIT-into-to-CS/siamese'
output_file = os.path.join(output_folder, 'output_image.jpg')
cv2.imwrite(output_file, final_image_with_boxes)

# Convert the image to a tensor and normalize it
preprocess = transforms.Compose([
    transforms.Resize((100, 100)),
    transforms.ToTensor()
])

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

        # Apply the preprocessing to the image
        normalized_image1 = preprocess(imagetoprocess1)

        # You need to unsqueeze the tensors to add a batch dimension
        normalized_image1 = normalized_image1.unsqueeze(0)

        # Move the tensors to the GPU if available
        if torch.cuda.is_available():
            normalized_image0 = normalized_image0.cuda()
            normalized_image1 = normalized_image1.cuda()

        # Pass the images through the Siamese network
        output1, output2 = model(normalized_image1, normalized_image0)

        # Calculate the Euclidean distance between the two output feature vectors
        euclidean_distance = F.pairwise_distance(output1, output2)

        if euclidean_distance.item() < 1.0:
          x, y, width, height = each_box['box']
          changed_img = cv2.imread('/content/drive/MyDrive/Colab Notebooks/snn network/output_image.jpg')
          cv2.rectangle(changed_img, (x, y), (x + width, y + height), (0, 255, 0), 2)
          # Calculate the position for the text
          text_x = x
          text_y = y - 10
          cv2.putText(changed_img, file_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
          output_folder = '/content/drive/MyDrive/Colab Notebooks/snn network'
          output_file = os.path.join(output_folder, 'output_image.jpg')
          cv2.imwrite(output_file, changed_img)

        # Display the concatenated images with the dissimilarity score
        concatenated = torch.cat((normalized_image1, normalized_image0), 3)
        imshow(torchvision.utils.make_grid(concatenated), f'Dissimilarity: {euclidean_distance.item():.2f}')



