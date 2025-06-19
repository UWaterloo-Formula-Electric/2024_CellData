import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('computed_ir.csv')

# scatter chart of cell ir histogram distribution
df = 1000 * df[df['Internal Resistance'] > 0]  # Filter outliers if necessary
std = df['Internal Resistance'].std()
mean = df['Internal Resistance'].mean()

plt.hist(df['Internal Resistance'], bins=50)
plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
plt.axvline(mean + std, color='r', linestyle='dashed', linewidth=2)
plt.axvline(mean - std, color='r', linestyle='dashed', linewidth=2)
# print mean and std near the plot
plt.title(f'Cell IR Histogram Distribution - Mean: {mean:.2f}, Std: {std:.2f}')
plt.xlabel('Cell IR (mOhms)')
plt.ylabel('Frequency')
plt.grid()
plt.show()