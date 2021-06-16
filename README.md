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
