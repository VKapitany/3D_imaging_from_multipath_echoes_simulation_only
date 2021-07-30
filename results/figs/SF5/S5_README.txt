S5_ground_truths.npy 
- 3*48x64 <> rows,columns
- units: metres

S5_histograms.npy 
- Dimensions: 3x256x1 <> bins,1
- units: normalised photon counts

S5_predictions.npy 
- CNN reconstructions of the ground truths
- 3*48x64 <> rows,columns
- units: metres

S5_time_series.npy
- x axis values (time) for histograms
- Dimensions: 256
- units: nanoseconds
