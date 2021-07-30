This repository holds material for:

Alex Turpin, Valentin Kapitany, Jack Radford, Davide Rovelli, Kevin Mitchell, Ashley Lyons, Ilya Starshynov & Daniele Faccio 
## "3D imaging from multipath temporal echoes" 

This repository is published under a CC BY-NC 4.0 License. The corresponding authors are 
Dr. Alex Turpin (alex.turpin@glasgow.ac.uk) and Prof. Daniele Faccio (daniele.faccio@glasgow.uk)

Contents:

LICENSE_CC_BY-NC_4.0.txt
>license

requirements.txt
>requirements list for python installations

data
>dir 01_data_simulation contains simulated data and models.
>dir 02_cnn_architectures contains png images of the cnn architectures, for ease of viewing.

notebooks
>simulation_MC_ray_gun.ipynb can be run to generate simulated data
results
>dir 'figs' contains the figures used in the article and in the supplementary text, in svg/pdf formats as well as numpy arrays, for access to the raw datapoints
>dir 'videos' contains the supplementary videos

src
>utils.py contains some methods shared among multiple IPython notebook
>nn_architectures.py contains the convolutional neural network architectures for the various data types, as shown in ..data/04_cnn_architectures



