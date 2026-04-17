import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
plots_dir = os.path.join(script_dir, "..", "outputs", "plots")

df = pd.read_csv(data_path)

# Convert formatted numbers
df['Wishlist'] = df['Wishlist'].apply(parse_number)

# Top Genres
top_genres = df['Genre'].value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top Genres")
plt.savefig(os.path.join(plots_dir, "top_genres.png"))

# Correlation
plt.figure()
sns.heatmap(df[['Global_Sales','Rating','Wishlist']].corr(), annot=True)
plt.savefig(os.path.join(plots_dir, "correlation.png"))

print("EDA completed ✅")