<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Train new language model from cadet and inception data

This project template lets you train a part-of-speech tagger, morphologizer and dependency parser from your cadet and inception data.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install the new language object from Cadet |
| `convert` | Convert the data to spaCy's format |
| `split` | Split the data into train, validation, and test |
| `debug` | Assess data for training using spaCy's debug data |
| `train` | Train urban-giggle |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `document` | Generate project documentation |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `install` &rarr; `convert` &rarr; `split` &rarr; `debug` &rarr; `train` &rarr; `evaluate` &rarr; `package` &rarr; `document` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/urban-giggle` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
