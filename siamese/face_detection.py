import cv2
from mtcnn import MTCNN

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
        x1, y1 = x - 12, y - 12
        x2, y2 = x + width + 12, y + height + 12
        face_crop = image[y1:y2, x1:x2]
        face_crops.append(face_crop)

    return face_crops

def detect_faces_and_boxes(image_path):
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
        x1, y1 = x - 12, y - 12
        x2, y2 = x + width + 12, y + height + 12
        face_crop = image[y1:y2, x1:x2]
        face_crops.append(face_crop)

    return face_crops, faces

