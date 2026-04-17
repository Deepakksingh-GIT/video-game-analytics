# Video Game Analytics Dashboard

A comprehensive data analytics project for video game sales and ratings, featuring data cleaning, exploratory data analysis (EDA), machine learning prediction, and an interactive web dashboard.

## Features

- **Data Cleaning & Merging**: Processes raw game and sales data, handles missing values, and standardizes formats.
- **Exploratory Data Analysis (EDA)**: Generates visualizations for top genres and correlations.
- **Machine Learning Model**: Trains a RandomForest regressor to predict global sales based on rating and wishlist count.
- **Database Integration**: Stores cleaned data in SQLite for querying.
- **Interactive Dashboard**: Built with Streamlit, includes EDA plots, data exploration, and sales prediction.

## Project Structure

```
video-game-analytics/
├── data/
│   ├── raw/
│   │   ├── games.csv          # Raw game data (titles, ratings, genres)
│   │   └── vgsales.csv        # Raw sales data (names, platforms, sales)
│   └── processed/
│       └── merged_data.csv    # Cleaned and merged dataset
├── src/
│   ├── data_cleaning.py       # Data cleaning and merging script
│   ├── eda.py                 # Exploratory data analysis with plots
│   ├── model.py               # Machine learning model training
│   └── load_db.py             # Database setup and data loading
├── sql/
│   └── schema.sql             # SQLite database schema
├── outputs/
│   ├── plots/                 # EDA visualizations (PNG files)
│   └── models/                # Trained ML model (Pickle file)
├── dashboard/
│   └── app.py/
│       └── apps.py            # Streamlit dashboard app
├── .streamlit/
│   └── config.toml            # Streamlit theme configuration
├── screenshots/               # Dashboard screenshots (optional)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Setup Instructions

1. **Clone or Download the Project**:
   - Ensure you have the project folder on your local machine.

2. **Install Dependencies**:
   - Install Python 3.8+ if not already installed.
   - Run: `pip install -r requirements.txt`

3. **Run Data Pipeline**:
   - Clean and merge data: `python src/data_cleaning.py`
   - Generate EDA plots: `python src/eda.py`
   - Train model: `python src/model.py`
   - Set up database: `python src/load_db.py`

4. **Launch Dashboard**:
   - Run: `streamlit run dashboard/app.py/apps.py`
   - Open the provided local URL (e.g., http://localhost:8501) in your browser.

## Usage

- **Dashboard Sections**:
  - **EDA**: View top genres bar chart and correlation heatmap.
  - **Data Exploration**: Select a genre to see top games with sales figures.
  - **Sales Prediction**: Input rating and wishlist count to predict global sales.

- **Data Insights**:
  - Sales are in millions of units (e.g., 82.74 = 82.74 million units).
  - Model predicts based on user rating (0-5) and wishlist count.

## Screenshots

### Dashboard Overview
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/2381313e-8cec-4dfa-9939-3ee054d5b4e8" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/10e89f2f-11ef-42d1-b1fc-efcc1b11d3c2" />


### EDA Visualizations
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/fe7caf97-4cd0-4bba-a13f-5eaf1db55572" />

### Sales Prediction
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a102bf70-c4f7-43b4-b8f5-f22f1e01dc8e" />

## Technologies Used

- **Python**: Core language
- **Pandas**: Data manipulation
- **Matplotlib/Seaborn**: Data visualization
- **Scikit-learn**: Machine learning
- **Streamlit**: Web dashboard
- **SQLite**: Database storage

## Dataset Sources

- Games data: Hypothetical or sourced from gaming APIs (e.g., IGDB, RAWG).
- Sales data: Based on VGChartz dataset (public domain).

## Contributing

Feel free to fork and contribute improvements!

## License

This project is for educational purposes. Check data sources for licensing.
