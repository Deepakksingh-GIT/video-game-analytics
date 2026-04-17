import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Video Game Analytics", page_icon="🎮", layout="wide")

script_dir = os.path.dirname(__file__)
data_path = os.path.join(script_dir, "..", "..", "data", "processed", "merged_data.csv")
model_path = os.path.join(script_dir, "..", "..", "outputs", "models", "model.pkl")
plots_dir = os.path.join(script_dir, "..", "..", "outputs", "plots")

df = pd.read_csv(data_path)

st.title("🎮 Video Game Analytics Dashboard")

# EDA Section
st.header("Exploratory Data Analysis")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Genres")
    st.image(os.path.join(plots_dir, "top_genres.png"))
with col2:
    st.subheader("Correlation Heatmap")
    st.image(os.path.join(plots_dir, "correlation.png"))

# Filters
st.header("Data Exploration")
genre = st.selectbox("Select Genre", df['Genre'].unique(), key="genre_select")

filtered = df[df['Genre'] == genre]

st.write("Top Games in Selected Genre")
# Format Global_Sales with units
filtered_display = filtered[['Title','Global_Sales']].head(10).copy()
filtered_display['Global_Sales'] = filtered_display['Global_Sales'].apply(lambda x: f"{x:.2f} million units")
st.dataframe(filtered_display)

# Prediction
st.header("Sales Prediction")

rating = st.slider("Rating", 0.0, 5.0, 4.0)
wishlist = st.number_input("Wishlist Count", 0, 100000, 1000)

if st.button("Predict"):
    model = pickle.load(open(model_path,"rb"))
    prediction = model.predict(pd.DataFrame([[rating, wishlist]], columns=['Rating', 'Wishlist']))
    st.success(f"Predicted Global Sales: {prediction[0]:.2f} million units")