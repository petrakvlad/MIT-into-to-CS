import cv2
from mtcnn import MTCNN
import matplotlib.pyplot as plt
import tensorflow

def get_image_with_boxes(image_path):
    # Load the input image
    image = cv2.imread(image_path)
    
    # Initialize the MTCNN detector
    detector = MTCNN()
    
    # Perform face detection
    faces = detector.detect_faces(image)
    
    # Extract face crops and coordinates
    for face in faces:
        x, y, width, height = face['box']
        # Draw a bounding box around the face
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    
    # Save or display the image with bounding boxes
    cv2.imwrite('output.jpg', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image

def detect_faces(image_path):
    # Load the input image
    image = cv2.imread(image_path)
    
    # Initialize the MTCNN detector
    detector = MTCNN()
    
    # Perform face detection
    faces = detector.detect_faces(image)
    
    # Extract face crops and coordinates
    face_crops = []
    for i, face in enumerate(faces):
    
        x, y, width, height = face['box']
        x1, y1 = x, y
        x2, y2 = x + width, y + height
        face_crop = image[y1:y2, x1:x2]
        face_crops.append(face_crop)

    return face_crops

# Example usage:
input_image_path = "/home/hell/Documents/GitHub/MIT-into-to-CS/seamese/demo_image.jpg"
detected_faces = detect_faces(input_image_path)
new_image = get_image_with_boxes(input_image_path)

#  Display each detected face crop
# for i, face_crop in enumerate(detected_faces):
#     plt.figure()
#     plt.imshow(cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
#     plt.title(f"Face {i+1}")
#     plt.axis("off")
#     plt.show()

