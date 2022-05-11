"""
conll_to_spacy.py debug --input_dir ..
conll_to_spacy.py convert --input_dir .. --output_dir ..
"""
with open('data/yoruba.conllu') as f:
    lines = f.readlines()

index = 0
for line in lines:
    index += 1
    if len(line)==0 or line[0]=='#' or line=='\n':
        continue
    tokens_num = len(line.split('\t'))
    if tokens_num != 10:
        print(line.strip('\n'), tokens_num, index)
