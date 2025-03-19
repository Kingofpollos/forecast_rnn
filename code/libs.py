import numpy as np

#Dividir secuencias de tiempo
def split_sequence(sequence, n_steps_in, n_steps_out):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps_in
		out_end_ix = end_ix + n_steps_out
		# check if we are beyond the sequence
		if out_end_ix > len(sequence):
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return np.array(X), np.array(y)

def split_dates(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        # check if we are beyond the sequence
        if out_end_ix > len(sequence):
            break
        # gather input and output parts of the pattern
        seq = sequence[i:end_ix]
        seq_x = [seq[0], seq[-1]]
        X.append(seq_x)
    return np.array(X)

def vector_normalizer(array):
    return (array - array.min()) / (array.max() - array.min())

def vector_min_max(array):
    return array.min(), array.max()

def apply_normalizer(array, array_min_max):
    array = np.concatenate((array, array_min_max), axis=1)
    return np.apply_along_axis(lambda x: (x - x[-2]) / (x[-1] - x[-2]), 1, array)[:,:-2]