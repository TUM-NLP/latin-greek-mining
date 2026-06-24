# Anisotropy

## Isotropy analysis

* To analyze the anisotropy of embeddings, execute following command with two embedding files
`grc-lat.test.grc.vec` and `grc-lat.test.lat.vec` in the directory:


    python isotropy.py


* To apply CBIE or whitening to given embeddings, execute following command:


    python apply_cbie.py --(whitening|cbie) --input_file input_file --output_file output_file


* To visualize the anisotropy of embeddings, tSNE was used.
The file `tSNE.py` stems from Hämmerl et al.,
therefore follow the instructions for usage there: https://github.com/kathyhaem/outliers
