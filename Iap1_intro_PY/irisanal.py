import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.groupby("Species")["PetalLengthCm"].mean().round(3))