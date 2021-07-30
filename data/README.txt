01_data_simulation
>dir "models" contains 10 example models (1 per maximum number of scattering events) trained on simulated training data.
>dir "test_data" contains the temporal histograms and corresponding 3D images used to test the inference of our neural network models.
>dir "training_data" contains dummy training data and histograms; these are a subset of the true training dataset, truncated to contain fewer datapoints to conserve storage space.
>predictions%i contains the i-th model initialisation, pertaining to the 10x100 predictions (10 scattering events, for 100 test histograms)
>time_series.npy
	- The (x-axis) time starting edges of the test histograms bins, unit: nanoseconds

02_cnn_architectures: contains png images of the cnn architectures, for ease of viewing.

-By loading some dummy training data from dir's named 'training_data', and loading the corresponding NN architectures from ../src/nn_architectures.py, we can train a dummy model.
-By loading an NN model from 'models', and loading the test dataset from 'test_data', we can obtain predictions of the test histograms and compare them to corresponding ground truths. These are the same predictions as shown in the article, so they can be used for numerical analysis.