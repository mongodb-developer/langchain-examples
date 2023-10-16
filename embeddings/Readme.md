# audioEmbedding

This script uses [`panns_inference`](https://github.com/qiuqiangkong/panns_inference) library and `librosa` to take audio Wav or mp3 files and create 2048 dimensional embeddings.

This data can be used as an embedding array for MongoDB Atlas Vector search for advanced search capabilities:

- Similariity search based on audio
- Ranking and scoring similarity of audio

  

## Setup and install

### Atlas Cluster

Build [vector search](https://www.mongodb.com/products/platform/atlas-vector-search) on MusicDB and songs with 2048 dimensions
```
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embeddings": {
        "dimensions": 2048,
        "similarity": "dotProduct",
        "type": "knnVector"
      }
    }
  }
}
```

### Local machine
Install numpy, librosa and panns_inference:

```
pip install panns-inference
pip install numpy
pip install librosa
pip install pymongo
```

Download the  file `Cnn14_mAP=0.431.pth` from [here](https://huggingface.co/thelou1s/panns-inference/blob/main/Cnn14_mAP%3D0.431.pth), and place under `<YOUR_HOME_DIR>/panns_data/Cnn14_mAP=0.431.pth` (eg. `/Users/pavel.duchovny/panns_data/Cnn14_mAP=0.431.pth`)

First run might take time as the `panns_inference` model is a locally hosted model that is being downloaded.

Place files in a temporary directory with your audio files for analysis. Point the directory in the main script `audioEmbeddings.py` replacing `<DIRECTORY WITH AUDIO FILES>` to the full path.

Replace your cluster or database URI in `audioEmbeddings.py` script :
```
client = MongoClient('mongodb+srv://<cluster>.mongodb.net/?retryWrites=true&w=majority')
```

## Run 

```
python ./audioEmbeddings.py
```

### Example of output
```
> ls /audiofiles/
audio1.mp3
audio2.mp3

> python ./audioEmbeddings.py
Checkpoint path: /Users/pavel.duchovny/panns_data/Cnn14_mAP=0.431.pth
Using CPU.
audio1.mp3
audio2.mp3
```


# DISCLAIMER

---

**This repository/software is provided "AS IS", without warranty of any kind.** It is intended for educational and experimental purposes only and should not be considered as a product of MongoDB or associated with MongoDB in any official capacity.

**Use of this repository/software is at your own risk.** The author/maintainer/contributors are not responsible for any damage, data loss, or any adverse effects that may occur as a result of using or relying on this repository/software.

It is important to understand and acknowledge that this is **not a MongoDB product**, and MongoDB, Inc. has not reviewed, approved, or endorsed this repository/software.

Always ensure to take necessary precautions, including backups and thorough testing, before using any software in a production environment.

---

