import os
import re
from nltk.corpus import stopwords

def preprocess(file_paths, output_dir):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:  # Specify the encoding as UTF-8
            data = f.readlines()

        data = [re.sub(r'[^\w\s@.]', ' ', line) for line in data]
        data = [re.sub(r'\n', '', line) for line in data]
        data = [re.sub(r'\s+', ' ', line) for line in data]
        data = [line.lower() for line in data]
        data = [word for line in data for word in line.split() if word not in stopwords.words('english')]

        # if the length of a word is 1, remove it
        data = [word for word in data if len(word) > 1]
        # remove space in the text
        data = [word.strip() for word in data]

        # Construct output file path
        output_filename = os.path.basename(file_path)  # Keep the same filename
        output_path = os.path.join(output_dir, output_filename)

        # Write preprocessed text to the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:  # Specify the encoding as UTF-8
            output_file.write(" ".join(data))

if __name__ == '__main__':
    dataset_dir = r"C:\Users\kiran\Project\resumetext"
    output_dir = r"C:\Users\kiran\Project\preprocessed"
    os.makedirs(output_dir, exist_ok=True)

    file_paths = []

    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.endswith(".txt"):  # Change to the appropriate file extension if needed
                file_paths.append(os.path.join(root, file))

    preprocess(file_paths, output_dir)
    print("Preprocessing complete.")

