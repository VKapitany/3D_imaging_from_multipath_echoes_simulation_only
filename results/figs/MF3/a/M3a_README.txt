M3a_mse.npy 
-Dimensions 2,4 > along first dimension (rows):
	0: subset <> the maximum time before cropping the histograms of the subset (nanoseconds)
	1: MSE (metres squared)

M3a_ground_truth.npy 
-Dimensions 60,80 <> rows, columns
-Units: metres

M3a_predictions.npy 
-Dimensions 4,60,80 <> subset, rows, columns
-The subset dimension corresponds to the subsets in M3a_mse_iou.npy 
-Units: metres

M3a_histograms.npy 
-Dimensions 4,256,1 <> subset, bins
-The subset dimension corresponds to the subsets in M3a_mse_iou.npy 
-Units: normalised photon counts

M3a_time_series.npy 
-x axis (time) starting edges for the histograms, units: nanoseconds
