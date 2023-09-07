import os
import openl3
import numpy as np
from sklearn.cluster import KMeans
import torchaudio
print("bvvvvvvvvvvvvvvvvv")

# Load audio files and extract OpenL3 embeddings
audio_folder = "/home/hell/Documents/GitHub/MIT-into-to-CS/voice/tracks" # Replace with the path to your audio files
audio_files = [os.path.join(audio_folder, file) for file in os.listdir(audio_folder)]
print("bi")
embeddings = []
for audio_file in audio_files:
    waveform, sample_rate = torchaudio.load(audio_file)
    embedding, _ = openl3.get_audio_embedding(waveform.numpy(), sample_rate, content_type="music")
    embeddings.append(embedding)
print("bo")

embeddings = np.array(embeddings)

# Clustering (K-Means)
num_clusters = 3  # Assuming 3 individuals
kmeans = KMeans(n_clusters=num_clusters)
cluster_labels = kmeans.fit_predict(embeddings)
print("bu")

# Output
for i, cluster_label in enumerate(cluster_labels):
    print(f"Audio file {audio_files[i]} belongs to cluster {cluster_label}")


audio_folder = "/home/hell/Documents/GitHub/MIT-into-to-CS/voice/tracks"