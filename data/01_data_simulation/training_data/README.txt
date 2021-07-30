The files in this folder are 

dummy_train_images.npy
- These are a dummy subset of ground truth images used to train the neural networks trained on simulated data.
- Dimensions: 10,100,80,80 <> Max. number of scattering events, object position, rows, columns
- object positions are randomly sampled from the dimensions of the room, constrained by the object being on the floor.
- Along the first dimension, each image is identical <> For various scattering event numbers, I used the same
parent scene
- units: metres

dummy_train_histograms.npy
- These are the corresponding histograms used to train the neural networks trained on simulated data.
- Dimensions: 10,100,200,1 <> Max. number of scattering events, object position, bins, 1
- object positions dimension arranged as before
- units: normalised photon counts
