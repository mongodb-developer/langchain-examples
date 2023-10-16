from panns_inference import AudioTagging
import numpy as np
import librosa
from pymongo import MongoClient
import os

def get_all_file_paths(directory_path):
    """Get all file paths in a directory."""
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".mp3"):  # To get only '.mp3' or '.wav' files
              print(file)
              file_paths.append(os.path.join(root, file))
    return file_paths


# Main directory holding the input audio files
directory_path = "<DIRECTORY WITH AUDIO FILES>"

model = AudioTagging(checkpoint_path=None, device='cpu') # change device to cpu if a gpu is not available

def normalize(v):
   # np.linalg.norm computes the vector's norm (magnitude).  The norm is the total length of all vectors in a space.
   norm = np.linalg.norm(v)
   if norm == 0: 
        return v
   
   # Return the normalized vector.
   return v / norm


# Function to get an embedding of an audio file. An embedding is a reduced-dimensionality representation of the file.
def get_embedding (audio_file):
  
  # Load the audio file using librosa's load function, which returns an audio time series and its corresponding sample rate.
  a, _ = librosa.load(audio_file, sr=44100)
  
  # Reshape the audio time series to have an extra dimension, which is required by the model's inference function.
  query_audio = a[None, :]
  
  # Perform inference on the reshaped audio using the model. This returns an embedding of the audio. 
  _, emb = model.inference(query_audio)


  # Normalize the embedding. This scales the embedding to have a length (magnitude) of 1, while maintaining its direction.
  normalized_v = normalize(emb[0])


  # Return the normalized embedding required for dot_product elastic similarity dense vector
  return normalized_v


# mongoDB connection
client = MongoClient('mongodb+srv://<cluster>.mongodb.net/?retryWrites=true&w=majority')
db = client['MusicDB']
collection = db['songs']


#Getting all .wav file paths
file_paths = get_all_file_paths(directory_path)

# Getting embeddings for all files
for file_path in file_paths:
    emb = get_embedding(file_path)
    # Store audio file with its embedding
    collection.insert_one({'file' :  file_path,'embeddings': emb.tolist()});
