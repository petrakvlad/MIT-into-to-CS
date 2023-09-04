import torch
import matplotlib.pyplot as plt
from SNN import SiameseNetwork
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from dataset import SiameseNetworkDataset
from torch.utils.data import DataLoader, Dataset
from PIL import Image
from face_detection import detect_faces
import torch.nn.functional as F
from dataset import imshow
import torchvision
import cv2
from mtcnn import MTCNN
import tensorflow

# Initialize the model
model = SiameseNetwork()
model.load_state_dict(torch.load('siamese_model_weights.pth'))
model.eval()  # Put the model in evaluation mode


# Load the image
imaget = Image.open("/home/hell/Documents/GitHub/MIT-into-to-CS/seamese/people/instances/0_michael_scott.jpg")

# Define the desired image size (e.g., 224x224)
desired_size = (100, 100)

# Resize the image
imaget = imaget.resize(desired_size)

# Convert the image to a tensor and normalize it
preprocess = transforms.Compose([transforms.Resize((100,100)),
                                     transforms.ToTensor()
                                    ])

# Apply the preprocessing to the image
normalized_image = preprocess(imaget)

# Extract the embedding for the image
with torch.no_grad():
    embedding = model.twin_1(normalized_image.unsqueeze(0))  # Unsqueezing to add a batch dimension



input_image_path = "/home/hell/Documents/GitHub/MIT-into-to-CS/seamese/demo_image.jpg"
detected_faces_1 = detect_faces(input_image_path)

for fac in detected_faces_1:

    # Concatenate the two images together
    concatenated = torch.cat((imaget, fac), 0)
    
    output1, output2 = model(imaget, fac)
    euclidean_distance = F.pairwise_distance(output1, output2)
    imshow(torchvision.utils.make_grid(concatenated), f'Dissimilarity: {euclidean_distance.item():.2f}')