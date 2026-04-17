import sqlite3
import pandas as pd
import os

# Connect to database
db_path = os.path.join("data", "video_games.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute schema
with open("sql/schema.sql", "r") as f:
    schema = f.read()
cursor.executescript(schema)
conn.commit()

# Load merged data
merged_df = pd.read_csv("data/processed/merged_data.csv")

# Insert into games table
games_data = merged_df[['Title', 'Genre', 'Rating', 'Platform']].drop_duplicates()
games_data.to_sql('games', conn, if_exists='replace', index=False)

# Insert into sales table
sales_data = merged_df[['Name', 'Year', 'Global_Sales']].drop_duplicates()
sales_data.to_sql('sales', conn, if_exists='replace', index=False)

conn.close()

print("Database setup and data loaded ✅")