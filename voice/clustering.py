import os
import argparse
import librosa
import numpy as np
from sklearn.cluster import KMeans
import json

# Define a function for audio preprocessing
def preprocess_audio(audio_path, target_sr=22050):
    # Load the audio file and perform preprocessing (e.g., resampling and noise reduction)
    audio, sr = librosa.load(audio_path, sr=target_sr, res_type='kaiser_fast')
    # You can add noise reduction or other preprocessing steps here if needed

    return audio, sr

def extract_features(audio, sr, max_length=1000):
    # Extract features (e.g., MFCCs) from preprocessed audio
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

    # Pad or truncate the features to a fixed length
    if mfccs.shape[1] < max_length:
        pad_width = max_length - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfccs = mfccs[:, :max_length]

    return mfccs.flatten()

def cluster_audio_files(folder_path, num_clusters):
    # List all audio files in the folder
    audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.wav')]

    # Extract features from each audio file
    features = []
    for file in audio_files:
        audio, sr = preprocess_audio(file)
        feature_vector = extract_features(audio, sr)
        features.append(feature_vector)

    # Perform clustering using K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    cluster_labels = kmeans.fit_predict(features)

    # Create clusters based on labels
    clusters = {}
    for i, label in enumerate(cluster_labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(os.path.basename(audio_files[i]))

    return clusters

def main():
    parser = argparse.ArgumentParser(description='Cluster audio files based on their voices.')
    parser.add_argument('--folder_path', type=str, help='Path to the folder containing audio files.')
    args = parser.parse_args()

    if not args.folder_path:
        print("Please provide the --folder_path argument.")
        return

    num_clusters = 3  # You can change this to the desired number of clusters

    clusters = cluster_audio_files(args.folder_path, num_clusters)

    # Convert cluster keys to strings
    clusters_str_keys = {str(key): value for key, value in clusters.items()}

    # Output the clusters in JSON format
    with open('audio_clusters.json', 'w') as json_file:
        json.dump(clusters_str_keys, json_file, indent=4)

    print("Clusters saved to audio_clusters.json")

if __name__ == '__main__':
    main()



# import os
# import argparse
# import librosa
# import numpy as np
# from sklearn.cluster import KMeans
# import json

# def extract_features(file_path, max_length=1000):
#     # Load the audio file and extract features (e.g., MFCCs)
#     audio, sr = librosa.load(file_path, sr=None)
#     mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

#     # Pad or truncate the features to a fixed length
#     if mfccs.shape[1] < max_length:
#         pad_width = max_length - mfccs.shape[1]
#         mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
#     else:
#         mfccs = mfccs[:, :max_length]

#     return mfccs.flatten()




# def cluster_audio_files(folder_path, num_clusters):
#     # List all audio files in the folder
#     audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.wav')]

#     # Extract features from each audio file
#     features = [extract_features(file) for file in audio_files]

#     # Perform clustering using K-Means
#     kmeans = KMeans(n_clusters=num_clusters, random_state=0)
#     cluster_labels = kmeans.fit_predict(features)

#     # Create clusters based on labels
#     clusters = {}
#     for i, label in enumerate(cluster_labels):
#         if label not in clusters:
#             clusters[label] = []
#         clusters[label].append(os.path.basename(audio_files[i]))

#     return clusters

# def main():
#     parser = argparse.ArgumentParser(description='Cluster audio files based on their voices.')
#     parser.add_argument('--folder_path', type=str, help='Path to the folder containing audio files.')
#     args = parser.parse_args()

#     if not args.folder_path:
#         print("Please provide the --folder_path argument.")
#         return

#     num_clusters = 3  # You can change this to the desired number of clusters

#     clusters = cluster_audio_files(args.folder_path, num_clusters)

#     # Convert cluster keys to strings
#     clusters_str_keys = {str(key): value for key, value in clusters.items()}

#     # Output the clusters in JSON format
#     with open('audio_clusters.json', 'w') as json_file:
#         json.dump(clusters_str_keys, json_file, indent=4)

#     print("Clusters saved to audio_clusters.json")


# if __name__ == '__main__':
#     main()
