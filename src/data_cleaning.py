import pandas as pd
import os

def load_data():
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, "..", "data", "raw")
    games = pd.read_csv(os.path.join(data_dir, "games.csv"))
    sales = pd.read_csv(os.path.join(data_dir, "vgsales.csv"))
    return games, sales

def clean_games(games):
    games.drop_duplicates(inplace=True)

    # Handle missing values
    games['Rating'] = games['Rating'].fillna(games['Rating'].median())

    # Standardize text
    games['Genres'] = games['Genres'].str.lower()

    return games

def clean_sales(sales):
    sales.drop_duplicates(inplace=True)

    sales['Year'] = sales['Year'].fillna(sales['Year'].median())

    return sales

def merge_data(games, sales):
    merged = pd.merge(games, sales, left_on="Title", right_on="Name", how="inner")
    return merged

def save_data(df):
    script_dir = os.path.dirname(__file__)
    processed_dir = os.path.join(script_dir, "..", "data", "processed")
    df.to_csv(os.path.join(processed_dir, "merged_data.csv"), index=False)

if __name__ == "__main__":
    games, sales = load_data()
    games = clean_games(games)
    sales = clean_sales(sales)
    merged = merge_data(games, sales)
    save_data(merged)

    print("Data cleaning completed ✅")