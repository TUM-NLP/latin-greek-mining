# Corpus Creation

To create a BUCC style corpus as described in you can call `python corpus_creation.py` after having specified the path of the input files
and the path of the output directory (see top of the file).
It is taken from Okabe et Fraser (2025), Bilingual Sentence Mining for Low-Resource Languages: a Case Study on Upper and Lower Sorbian


If you want to preprocess your corpus data before creating the corpus call
`python preprocess_corpus_data.py`.
It removes any Greek alphabet Latin sentences, replaces j by i and removes excessive whitespaces.
Modify `input_file` and `output_file` at the beginning of the file.