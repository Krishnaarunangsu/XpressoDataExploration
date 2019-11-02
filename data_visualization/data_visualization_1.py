import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('classic')
sns.set_style('darkgrid')

# Now we create some random walk data:

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# And do a simple plot:

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.suptitle('First Plot')
plt.show()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], normed=True, alpha=0.5)

plt.show()

for col in 'xy':
    sns.kdeplot(data[col], shade=True)

plt.show()

sns.distplot(data['x'])
sns.distplot(data['y'])
plt.show()

sns.kdeplot(data)
plt.show()

with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde')

plt.show()

with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')

plt.show()