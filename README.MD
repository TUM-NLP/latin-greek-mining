# Evaluating Latin and Ancient Greek Sentence Alignment through Parallel Sentence Mining

## Content

This project includes the code base used for this paper and additionally publishes its best model DistilSPhilBERTa:
https://huggingface.co/sebastian-reichbauer/DistilSPhilBERTa

For explanations on how to use the files, look into the relevant subdirectories.
Here is an overview over the different directories:
* `corpus_creation` covers the creation of the evaluation corpus. It relies on data (parallel and monolingual),
which is not provided for this Github project. However, the precomputed corpus is available in `data`
* `data` includes the precomputed result of corpus_creation, namely the created corpus data with gold set
* `evaluation_pipeline` is used to calculate embeddings for specific models and evaluate their performance on the metrics Precision, Recall and F1 score
* `post_processing` is used to apply whitening or cbie to the computed embeddings, as well as analyze anisotropy.
Therefore, it handles all stuff related to postprocessing already generated embeddings.
* `training` is used to train models using different methods (parallel sentences or knowledge distillation)

The best performing model from the paper can be found at (INSERT LINK).

## Benchmarks

The updated benchmarks with the opensource version of our dataset can be found here:

### Base Results

| Model name | F1 Score | 
|------------|----------| 
| Ugarit     | 63.8     |
| LaBSE      | 63.0     |
| SPhilBERTa | 43.5     |
| Qwen3      | 36.4     |
| Glot500    | 6.4      |
| XLM-R      | 0.2      |

### Best Model (after knowledge distillation)

DistilSPhilBERTa was trained using knowledge distillation with SPhilBERTa as student model and LaBSE as teacher model, using
English as anchor language.
English-Greek and English-Latin parallel sentences have been used for training.

| Model name       | F1 Score | 
|------------------|----------| 
| LaBSE/SPhilBERTa | 85.4     |

DistilSPhilBERTa can be downloaded at:
https://huggingface.co/sebastian-reichbauer/DistilSPhilBERTa