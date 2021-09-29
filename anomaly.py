import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use a predefined style set
plt.style.use('ggplot')


# Import Faker
from faker import Faker
fake = Faker()

# Creates a list of array called names list to hold the random names
names_list = []

# Creates a for loop with a range of 100
fake = Faker()
for _ in range(100):
    names_list.append(fake.name())

# Created another list called bit speed with the range of 100
bitspeed= []
for _ in range(100):
    mbps = np.random.randint(25,100)
    bitspeed.append(mbps)

# Creation of pandas DataFrame
mbps_df = pd.DataFrame(
    {'Person': names_list,
        'Internet speed(In mbps)': bitspeed
    })

# Print a subsection of the DataFrame
print(mbps_df.head())
print(format('Risk Detection', '*^82'))
if mbps > 25:
    print("No risk")
elif mbps < 25:
    print("Low risk")
elif mbps < 15:
    print("Medium")
else:
    print("High Risk")

print(format('Anomaly', '*^82'))
mbps_df.at[16, 'Internet speed(In mbps)'] = 23
mbps_df.at[65, 'Internet speed(In mbps)'] = 20


# To verify if the Internet speed were changed
print(mbps_df.loc[16])
print(mbps_df.loc[65])


# Generate a Histogram plot
mbps_df['Internet speed(In mbps)'].plot(kind='hist')
plt.show()

# The Minimum and maximum mbps
print('The lowest mbps that a customer got ' + str(mbps_df['Internet speed(In mbps)'].min()))
print('The highest mbps that a customer got  ' + str(mbps_df['Internet speed(In mbps)'].max()))

# cannot link this anomaly detection to current code
print(format('Anomaly Detection', '*^82'))
if str(mbps_df > 25):
    print("No risk")
elif str(mbps_df < 25):
    print("Low risk")
elif str(mbps_df < 15):
    print("Medium")
else:
    print("High Risk")