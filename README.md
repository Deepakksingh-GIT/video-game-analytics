# 🎮 Video Game Sales and Engagement Analysis

## 📌 Project Overview

This project focuses on analyzing video game sales and user engagement data to uncover trends in game popularity, platform performance, and user behavior. By combining sales data with engagement metrics such as ratings, wishlist, and play counts, the project provides actionable insights for game developers, publishers, and marketers.

---

## 🎯 Problem Statement

The goal of this project is to analyze and visualize video game sales and engagement data to understand how different factors such as genre, platform, ratings, and user behavior influence game success. The project also aims to support decision-making for marketing strategies, product development, and sales forecasting.

---

## 🛠️ Tech Stack

* **Python** (Pandas, NumPy, Matplotlib, Seaborn)
* **SQL** (Database design and querying)
* **Streamlit / Power BI** (Interactive dashboards)
* **Scikit-learn** (Machine Learning - Sales Prediction)

---

## 📂 Dataset Description

### 1. Games Dataset (games.csv)

* Title – Game name
* Rating – User review score
* Genres – Game categories
* Plays – Number of playthroughs
* Backlogs – Planned plays
* Wishlist – Number of wishlists
* Release Date, Platform, Team

### 2. Sales Dataset (vgsales.csv)

* Name – Game name
* Platform – Console/device
* Year – Release year
* Genre – Category
* Publisher – Game publisher
* Regional Sales – NA, EU, JP, Others
* Global_Sales – Total sales

---

## ⚙️ Project Workflow

### 1. Data Cleaning

* Removed duplicate records
* Handled missing values using statistical methods
* Standardized categorical values (genre, platform, publisher)
* Merged datasets based on game titles

### 2. SQL Database Design

* Created structured tables for games and sales data
* Applied normalization techniques
* Used primary and foreign keys to maintain data integrity

### 3. Exploratory Data Analysis (EDA)

* Analyzed trends in ratings, wishlist, and sales
* Identified popular genres and platforms
* Studied regional sales distribution
* Examined relationships between engagement and sales

### 4. Data Visualization

* Bar charts for genre/platform comparison
* Line charts for sales trends over time
* Heatmaps for correlation analysis
* Scatter plots for rating vs sales

### 5. Machine Learning (Advanced Enhancement)

* Built a regression model to predict global sales
* Used features like rating and wishlist
* Evaluated model performance using standard metrics

---

## 📊 Key Insights

* 🎮 Action and Sports genres generate the highest global sales
* 🌍 North America contributes the largest share of sales
* ⭐ High ratings do not always guarantee high sales
* 📌 Wishlist indicates user interest but does not always convert into revenue
* 🕹️ Platform plays a crucial role in game success

---

## 💡 Business Recommendations

* Focus development on high-performing genres like Action and Sports
* Target North American market for higher revenue potential
* Improve game quality and ratings to boost engagement
* Use wishlist data for demand forecasting
* Optimize platform selection based on genre performance

---

## 🤖 Machine Learning Model

* Model Used: Random Forest Regressor
* Objective: Predict global sales of video games
* Features: Rating, Wishlist
* Outcome: Helps estimate expected sales before game launch

---

## 📈 Dashboard Features

* Interactive filters (Genre, Platform, Year)
* KPI indicators (Total Sales, Avg Rating)
* Trend analysis over time
* Comparison across regions and genres
* Real-time sales prediction (Streamlit)

---

## 🚀 Future Improvements

* Add recommendation system for games
* Integrate real-time data sources
* Improve model accuracy with more features
* Deploy using cloud platforms (AWS/Render)

---

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

---

## 📎 Conclusion

This project demonstrates the complete data analysis pipeline from data cleaning and database design to visualization and predictive modeling. It provides valuable insights into the gaming industry and supports data-driven decision-making.

---

## 👨‍💻 Author

**Deepak Kumar Singh**
Aspiring Data Scientist

---

## License

This project is for educational purposes. Check data sources for licensing.
