# Training Data Processing

* With `process_grc_eng.py`, one can convert the data from the Krahne repository (https://github.com/kevinkrahn/ancient-greek-datasets)
(the Greek-English parallel sentences) into a CSV file given the correct file path
* Latin-English parallel sentences are directly retrieved from huggingface
* To generate training.csv with parallel Latin-Greek data, execute the following with the
necessary data in it (this means, DFGH corpus files with correct directory (change in file) and the Thukydides latin and greek xml file from perseus project):


    python preprocess_thukydides.py

    python preprocess_DFGH.py

    python process_training_csv.py

