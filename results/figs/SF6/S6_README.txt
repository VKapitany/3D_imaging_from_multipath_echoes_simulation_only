S4_ground_truth.npy
80x80 depth image, units=metres

S4_reconstructions.npy
80x80 depth image, units=metres

S4_mask.npy
80x80 depth image, units=metres

S4_iou.npy
80x80 depth image, values:
			- 0: background, i.e. complement of union of foregrounds (R tilde = G tilde = 0)
			- 1: only reconstruction foreground (R tilde = 1, G tilde = 0)
			- 2: only ground truth foreground (G tilde = 1, R tilde = 0)
			- 3: intersection of foregrounds (R tilde = G tilde = 1)