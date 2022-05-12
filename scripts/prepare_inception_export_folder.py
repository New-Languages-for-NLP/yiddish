# 1. original version + "-1" - normalized version
# 2. move it 1 level up and rename to the name of the folder
import os
import preprocess_texts


BASE_FOLDER = 'data/input/annotation'
ANNOTATOR = 'sinai.rusinek'
OUTPUT_FOLDER = 'data/output'

conllu_2002_folders = os.listdir(BASE_FOLDER)
for folder in conllu_2002_folders:
    conllu_2002_folder = os.path.join(BASE_FOLDER, folder)
    print(conllu_2002_folder)
    file_name = os.path.join(conllu_2002_folder, ANNOTATOR+".conll")
    with open(file_name) as f:
        conll = f.read()
    normalized_conll = preprocess_texts.normalize(conll)
    output_file_name = os.path.join(OUTPUT_FOLDER, folder.replace(".conllu", ".conll"))
    with open(output_file_name, "w") as f:
        f.write(normalized_conll)
