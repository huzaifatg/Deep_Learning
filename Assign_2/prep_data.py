import os
import pandas as pd

# Path to face_classification folder
src_dir = "data/images/face_classification"

data = []

# Loop over happy and sad folders
for label in ["happy_person_face", "sad_person_face"]:
    folder = os.path.join(src_dir, label)
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        continue

    for fname in os.listdir(folder):
        # Store relative path to the image
        filepath = os.path.join("face_classification", label, fname)
        data.append([filepath, "Happy" if "happy" in label else "Sad"])

# Create labels.csv inside data/images/
df = pd.DataFrame(data, columns=["filename", "label"])
df.to_csv("data/images/labels.csv", index=False)

print(f"✅ labels.csv created with {len(df)} entries at data/images/labels.csv")
