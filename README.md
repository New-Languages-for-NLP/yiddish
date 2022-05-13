# 🌱 Project Language 

This repository is the central point for documentation and data for your project. You will find several folders where you can store the data and code used as you create data and train models for a new language. 

`0_original_texts`: This folder contains the original text files for the project. This is a record of the original state of the texts before any pre-processing and annotation.

`1_lookups_data`: This folder contains the json lookups files for unambiguous lemmata, pos, and feats. This data is used to document the bulk annotation process and is superseded by the manually annotated data from INCEpTION.

`2_new_language_object`: This folder contains the nlp object folder from either Cadet or the Cadet notebook. This folder is fetched during training to load the new language object.

`3_inception_export`: This folder contains the CoNLL-U data that is exported from INCEpTION once annotation work is completed. If versioning of exports is required, you can place each version is its own subfolder. During training, this folder provides the main source of training data and should be split between training and validation sets.

`4_trained_models`: This folder contains packaged models and model cards for your new language models.

## Dataset Summary 
- Short description of your language and your research goals.

## Language(s) 
- Name of the language or languages in the corpus.


## Curation Rationale
- See the sections on Mission Statement and Collection Development Policy in Jo and Gebru, ["Lessons from Archives"](https://arxiv.org/abs/1912.10389)
- In brief, why were these particular materials included in the dataset? Why were other materials excluded or left out?  
  
## Source Data
- Preferably a list with an entry for each text in the corpus, including:
  - Source and how obtained
  - Processing and sampling 
  - in-copyright?

## Personal and Sensitive Information, Potential for Human Harm 
- Assess the potential for the information in your dataset to cause human harm. Does the dataset contain historical texts with period biases and harmful language? Do your texts contain personal information?  

## Licensing Information
- relevant copyright and licensing of materials used in your dataset

## Dataset Curators
- names of project members

## Citation Information
- How to cite this project. 

### References
0. https://docs.google.com/document/d/1rqNMMNmr6nKJacA-alwQp0fEVfi6ynEB-r5E3oglSo0/edit#
1. https://github.com/ephraimberkovitch/PrincetonNLPYiddish
2. https://newnlp.princeton.edu/Workshop-I/
3. https://docs.google.com/document/d/1CD0tFz3gsIqz5vFh37ELoLAYrWK4L8ukR2qFT0TgjIQ/edit
4. https://www.zotero.org/groups/3839060/new_languages_for_nlp
5. https://github.com/Princeton-CDH/geniza
6. http://galabra.mypressonline.com/Protea/
7. https://github.com/explosion/spacy-models/releases/
8. https://spacy.io/api/data-formats#json-input
9. https://www.cs.uky.edu/~raphael/yiddish.html
10.https://huggingface.co/
11.https://inception.slovo.world/login.html: ephraim.berkovitch+NewNLP
12.https://github.com/New-Languages-for-NLP/files/blob/main/Different_no_lookups.conllu
13.https://universaldependencies.org/u/pos/index.html
14.https://github.com/New-Languages-for-NLP/cadet/blob/80786f1b59242f1bcc8be324a960b68d3e34f2ea/app/routers/export_texts.py#L193
15.http://www.cs.uky.edu/~raphael/yiddish/sholemAleykhem/contents.html
16.https://course.spacy.io/en
17.https://explosion.ai/demos/matcher
18.https://www.youtube.com/watch?v=WnGPv6HnBok&t=7s
19.https://new-languages-for-nlp.github.io/course-materials/w1/cadet.html: cadet+NewNLP
20.https://new-languages-for-nlp.github.io/course-materials/w1/cadet-notebook.html
21.pymorphy2
22.https://github.com/OnlpLab/NEMO-Corpus/tree/main/guidelines
23.https://programminghistorian.org/en/lessons/jupyter-notebooks
24.https://github.com/inception-project/inception-external-recommender
25.https://gitter.im/inception-project/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
26.https://yi.wikipedia.org/wiki/%D7%9C%D7%99%D7%A1%D7%98%D7%A2_%D7%A4%D7%95%D7%9F_%D7%9C%D7%A9%D7%95%D7%9F-%D7%A7%D7%95%D7%93%D7%A9_%D7%95%D7%95%D7%A2%D7%A8%D7%98%D7%A2%D7%A8_%D7%90%D7%99%D7%9F_%D7%99%D7%99%D7%93%D7%99%D7%A9
27. https://github.com/booknlp/booknlp
28. https://www.wikiwand.com/yi/%D7%9C%D7%99%D7%A1%D7%98%D7%A2_%D7%A4%D7%95%D7%9F_%D7%9C%D7%A9%D7%95%D7%9F-%D7%A7%D7%95%D7%93%D7%A9_%D7%95%D7%95%D7%A2%D7%A8%D7%98%D7%A2%D7%A8_%D7%90%D7%99%D7%9F_%D7%99%D7%99%D7%93%D7%99%D7%A9
29. https://yi.wikipedia.org/wiki/%D7%9C%D7%99%D7%A1%D7%98%D7%A2_%D7%A4%D7%95%D7%9F_%D7%9C%D7%A9%D7%95%D7%9F-%D7%A7%D7%95%D7%93%D7%A9_%D7%95%D7%95%D7%A2%D7%A8%D7%98%D7%A2%D7%A8_%D7%90%D7%99%D7%9F_%D7%99%D7%99%D7%93%D7%99%D7%A9