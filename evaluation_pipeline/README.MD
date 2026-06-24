# Evaluation Pipeline

These files allow to create embeddings out of specified input data and execute the evaluation pipeline.
The main process of creating embeddings is copied from the PaSeMiLL Github account (https://github.com/shuokabe/PaSeMiLL).

To create sentence embeddings, call:

    python contextual_sentence_embeddings.py -i input_file -o output_file --model_name model_name
as also specified in the PaSeMiLL Github.

After having created embeddings, one can test them using the evaluation pipeline
executed by pipeline.sh:

    ./pipeline.sh input_file1.vec input_file2.vec hyperparameter gold_standard_file

