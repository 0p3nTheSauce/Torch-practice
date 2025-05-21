import numpy as np

signal = np.array([1, 2, 3])
kernel = np.array([4, 5])
convolved_output = np.convolve(signal, kernel) #output [4 13 22 15]

# Print the result
print("Signal:", signal)
print("Kernel:", kernel)
print("Convolved Output:", convolved_output)