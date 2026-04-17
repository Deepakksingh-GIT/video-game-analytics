import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

def parse_number(s):
    if isinstance(s, str):
        if 'K' in s:
            return float(s.replace('K', '')) * 1000
        else:
            try:
                return float(s)
            except ValueError:
                return None
    else:
        return s

script_dir = os.path.dirname(__file__)
data_path = os.path.join(script_dir, "..", "data", "processed", "merged_data.csv")
model_path = os.path.join(script_dir, "..", "outputs", "models", "model.pkl")

df = pd.read_csv(data_path)

# Features
df = df[['Global_Sales','Rating','Wishlist']]
df['Wishlist'] = df['Wishlist'].apply(parse_number)
df.dropna(inplace=True)

X = df[['Rating','Wishlist']]
y = df['Global_Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open(model_path,"wb"))

print("Model trained ✅")