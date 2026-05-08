import matplotlib.pyplot as plt
import pandas as pd

logs = pd.read_csv("data/sample_logs.csv")

logs['status'].value_counts().plot(kind='bar')
plt.title("Login Status Count")
plt.show()
