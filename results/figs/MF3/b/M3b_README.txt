M3b_mse.npy 
-Dimensions 2,4 > along first dimension (rows):
	0: subset <> the maximum time before cropping the histograms of the subset (milliseconds)
	1: MSE (metres squared)

M3b_ground_truth.npy 
-Dimensions 64,64 <> rows, columns
-Units: metres

M3a_predictions.npy 
-Dimensions 4,64,64 <> subset, rows, columns
-The subset dimension corresponds to the subsets in M3b_mse_iou.npy 
-Units: metres

M3b_histograms.npy 
-Dimensions 4,9600,1 <> subset, bins
-The subset dimension corresponds to the subsets in M3b_mse_iou.npy 
-Units: normalised photon counts

M3b_time_series.npy 
-x axis (time) starting edges for the histograms, units: milliseconds
