import os
import librosa
import numpy as np
from sklearn.cluster import KMeans

# Function to extract audio features (MFCCs)
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)  # Take the mean of MFCCs as features

# Define the folder containing audio files and their corresponding labels
audio_folder = "/home/hell/Documents/GitHub/MIT-into-to-CS/voice/tracks"
audio_files = os.listdir(audio_folder)

# Create lists to store audio features and corresponding labels
features = []
labels = []

# Extract features and labels from audio files
for audio_file in audio_files:
    audio_path = os.path.join(audio_folder, audio_file)
    features.append(extract_features(audio_path))
    # Extract the label from the filename (e.g., "person1_audio1.wav" -> "person1")
    label = audio_file.split("_")[0]
    labels.append(label)

# Convert lists to NumPy arrays
X = np.array(features)

# Create a dictionary to map labels to unique integers
label_to_int = {label: idx for idx, label in enumerate(np.unique(labels))}
y = np.array([label_to_int[label] for label in labels])

# Perform K-Means clustering
num_clusters = 3  # You have 3 individuals
kmeans = KMeans(n_clusters=num_clusters)
cluster_labels = kmeans.fit_predict(X)

# Create a dictionary to map cluster labels to individuals
cluster_to_individual = {}
for cluster_id in range(num_clusters):
    cluster_indices = np.where(cluster_labels == cluster_id)[0]
    cluster_samples = y[cluster_indices]
    # Find the most common label in the cluster
    most_common_label = np.bincount(cluster_samples).argmax()
    cluster_to_individual[cluster_id] = most_common_label

# Reverse the label-to-integer mapping to get the individual names
int_to_label = {idx: label for label, idx in label_to_int.items()}


# Print the clustering results with filenames
for cluster_id, individual_int in cluster_to_individual.items():
    cluster_indices = np.where(cluster_labels == cluster_id)[0]
    individual_name = int_to_label[individual_int]
    
    print(f"Cluster {cluster_id + 1} (Individual {individual_name}):")
    for idx in cluster_indices:
        print(f"  - {audio_files[idx]}")

