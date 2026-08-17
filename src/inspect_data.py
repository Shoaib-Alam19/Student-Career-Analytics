import pandas as pd

df = pd.read_csv("data/train.csv")
df = df.drop_duplicates().reset_index(drop=True)

print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nTarget distribution:")
print(df["PlacementStatus"].value_counts())

X = df.drop("PlacementStatus", axis=1)
y = df["PlacementStatus"]

print("\nFeatures (X):")
print(X.columns)

print("\nTarget (y):")
print(y.name)