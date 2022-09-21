#Part 3: creating a histogram (Gaussian Distribution)
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

np.random.seed(30)
x = np.random.normal(size=1000)

plt.hist(x, density=True, bins=20)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data');
plt.title('Gaussian Distribution')

# Save the histogram
plt.savefig('hist.png')
