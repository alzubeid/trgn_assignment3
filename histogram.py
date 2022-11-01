#Part 3: creating a histogram (Patient Blood Glucose Level)
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df =pd.read_csv(patient_blood_glucose.csv)
data = df[Glucose]
bins=np.arnage(min(data), max(data) +1, 1)
plt.hist(df['Glucose'], bins)

plt.title('Blood Glucose Level')
plt.xlabel('Patients')
Plt.ylabel('blood_glc_level')
plt.show()

# Save the histogram
plt.savefig('hist.png')
