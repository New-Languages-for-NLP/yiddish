
"""Load inception conllu data and convert to spaCy binary format (DocBin)"""
import srsly
import typer
import warnings
from pathlib import Path
import subprocess
import shutil

import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans, get_lang_class
from sklearn.model_selection import train_test_split


def convert(export_path: str, n_sents:int, lang:str):

    lang = get_lang_class(lang)
    nlp = lang()

    export_path = Path(export_path)
    assert export_path.exists()
    
    converted_path = Path.cwd() / 'corpus' / 'converted'
    assert converted_path.exists()
    
    conll_path = Path.cwd() / 'corpus' / 'conll'
    assert conll_path.exists()

    conllu_path = Path.cwd() / 'corpus' / 'conllu'
    assert conllu_path.exists()
    
    conllu_files = [f for f in export_path.iterdir() if f.suffix == ".conllu"]
    #convert conllu to .spacy 
    for conllu in conllu_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conllu)}', "./corpus/conllu", f"-n {n_sents}"])
        
    conll_files = [f for f in export_path.iterdir() if f.suffix == ".conll"]
    #convert conll to .spacy 
    for conll in conll_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conll)}', "./corpus/conll", f"-n {n_sents}"])

    conllu_stem = [f.stem for f in conllu_files]
    conll_stem  = [f.stem for f in conll_files]

    matching_stem = list(
        set(conllu_stem) & set(conll_stem)
    )   
    
    converted_conll_files = [f for f in conll_path.iterdir()]
    converted_conllu_files = [f for f in conllu_path.iterdir()]
    all_files = list(
        set(converted_conllu_files)
        | set(converted_conll_files)
    )

    for file_ in all_files:
        if file_.stem in matching_stem:
            conllu_file = conllu_path / (file_.stem + '.spacy')
            conllu_bin = DocBin().from_bytes(conllu_file.read_bytes())
            conllu_docs = [d for d in conllu_bin.get_docs(nlp.vocab)]

            conll_file = conll_path / (file_.stem + '.spacy')
            conll_bin = DocBin().from_bytes(conll_file.read_bytes())
            conll_docs = [d for d in conll_bin.get_docs(nlp.vocab)]

            joined_docs = []
            for ling, ner in zip(conllu_docs, conll_docs):
                ling.ents = ner.ents
                joined_docs.append(ling)
            
            out_bin = DocBin()
            [out_bin.add(doc) for doc in joined_docs]
            out_bin.to_disk(f'./corpus/converted/{file_.stem}.spacy')

        else:
            shutil.copy(str(file_), str(f'./corpus/converted/{file_.stem}.spacy'))
        
if __name__ == "__main__":
    typer.run(convert)
