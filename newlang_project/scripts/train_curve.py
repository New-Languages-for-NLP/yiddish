# Ines' train-curve uses factors, split data into quarters, compare results of models trained with various portions of the data
# just test for improvement in the last 25% of the data,
# would the model benefit from more data? 

# https://code.ihub.org.cn/projects/1112/repository/commit_diff?changeset=c2a961dd551350a3e2d7d985f2b53990142c02e7
# https://prodi.gy/docs/recipes#train-curve

import typer
from pathlib import Path
import random

import spacy
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split

def train_curve(model_path:Path, train_file:Path, test_file:Path):
    """TODO: Write docstring."""
   
    nlp = spacy.load(model_path)

    train_bin = DocBin().from_bytes(train_file.read_bytes())
    train_docs = [d for d in train_bin.get_docs(nlp.vocab)]




if __name__ == "__main__":
    typer.run(train_curve)
