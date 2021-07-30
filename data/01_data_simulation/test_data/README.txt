The files in this folder are 

test_images.npy
- These are the ground truth images used to test the neural networks trained on simulated data.
- Dimensions: 10,100,80,80 <> Max. number of scattering events, object position, rows, columns
- object positions arranged as: 10x+y (e.g. to get position x=2,y=5, one wants examples=25) [see code]
- Along the first dimension, each image is identical <> For various scattering event numbers, I used the same
parent scene
- units: metres

test_histograms.npy
- These are the histograms used to test the neural networks trained on simulated data.
- Dimensions: 10,100,200,1 <> Max. number of scattering events, object position, bins, 1
- object positions dimension arranged as before
- units: normalised photon counts

background_mask.npy
- background image used to binarise predictions to calculate IOU (see Supplementary)
