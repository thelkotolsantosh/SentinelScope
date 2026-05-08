import pandas as pd
from sklearn.ensemble import IsolationForest

# Load logs
logs = pd.read_csv("data/sample_logs.csv")

# Feature engineering
logs['failed'] = logs['status'].apply(lambda x: 1 if x == 'failed' else 0)

# Model
model = IsolationForest(contamination=0.2, random_state=42)
logs['anomaly'] = model.fit_predict(logs[['failed']])

print(logs)
