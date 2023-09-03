import cv2
import numpy as np
import torch
import torchvision.transforms as transforms

your_input_width = 100
your_input_height = 100
# Assuming you have a pre-trained Siamese model loaded, and it expects input images in a specific format

def compute_embedding(face_crop, siamese_model):
    # Resize the face crop to the input size expected by the Siamese model
    input_size = (your_input_width, your_input_height)  # Set the desired input size
    transform = transforms.Compose([transforms.ToPILImage(),
                                    transforms.Resize(input_size),
                                    transforms.ToTensor()])
    
    # Preprocess the face crop
    face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    face_crop_tensor = transform(face_crop).unsqueeze(0)  # Add a batch dimension
    
    # Forward pass through the Siamese model to get the embedding
    with torch.no_grad():
        embedding = siamese_model(face_crop_tensor)
    
    # Convert the embedding tensor to a numpy array
    embedding = embedding.squeeze().cpu().numpy()
    
    return embedding

# Example usage:
# - Load your Siamese model and set your desired input size
# - Load a face crop (e.g., from detected_faces) and compute the embedding
# - The 'embedding' variable will contain the embedding vector for that face crop
