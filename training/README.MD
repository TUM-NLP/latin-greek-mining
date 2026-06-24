# Training Models

## Fine-tuning (training.py)

This is for training with parallel sentences (Ancient Greek-Latin).
One needs a training.csv file with the corresponding parallel data in the directory.
It can be created (provided you have the raw data) in `corpus_creation`. Look there for further instructions.
Then the model to be trained can be specified:

    model = SentenceTransformer("bowphs/SPhilBerta", device="cuda")

The output directory can also be specified:

    output_dir="sphilberta_unpr_big"

Additionally, one has to set

    word_level_model=False

to `True`, if a token-level model is used (such as Ugarit and XLM-R)

To start the training process, just execute:

    python training.py


## Knowledge Distillation

To do knowledge distillation, execute the following command with the respecting information:

    python knowledge_distillation.py teacher_model_name student_model_name whiten(True|False) output_directory num_epochs use_grc_lat_dataset(True|False)

as in this example:

    python knowledge_distillation.py bowphs/SPhilberta bowphs/SPhilberta True /directory 1 False

The whiten argument decides if whitening is applied to the teacher embeddings before training.
<br>The use_grc_lat_dataset parameter lets you decide if you want to apply knowledge distillation
with Latin as mediator language (and grc_lat sentences) or with English as mediator language.
However, in both cases, the csv files have to be present in the directory
(`grc_lat_dataset.csv` for grc_lat; `grc_eng_training_big.csv` for grc_eng_lat)<br>
To get grc_eng_training_big.csv, execute corpus_creation.py in `corpus_creation/training_data_processing`
with the repository with the parallel sentences downloaded (read README.MD there for further instructions).
Same applies for `training.csv` (see corpus_creating/data_retrieval).

NOTE:<br>
The file is based on make_multilingual.py, created by Reimers and Gurevych, the authors
of the knowledge distillation paper.

## Post Processing (Whitening/CBIE)

Just call either

    whitening(representations)

or

    cluster_based(representations, n_cluster: int, n_pc: int, hidden_size: int = 768)

with the corresponding parameters.

NOTE:<br>
This file is almost identical with the file Hämmerl et al. used for their paper.