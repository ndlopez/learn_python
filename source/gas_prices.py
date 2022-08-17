import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('~/Downloads/gas_prices.csv')
plt.plot(data.Year,data.USA)
plt.show()

