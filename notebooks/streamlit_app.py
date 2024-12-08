import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# st.set_page_config(layout="wide")
st.set_page_config(page_title="Review Analyzer", page_icon=":robot:", layout="wide")

#load the data with csv
data = pd.read_csv("AmazonBP_all_selected_01subset.csv")
data = data[["text", "rating", "sentiment"]] #target variable = sentiment 

# Load the pickled model
with open('text_embedding_logreg.pkl', 'rb') as f:
    model = pickle.load(f)

model_name = 'all-MiniLM-L6-v2' #384 dimensions
embedding_model = SentenceTransformer(model_name)

# Load the embeddings DataFrame
embeddings = pd.read_csv("embedding_X.csv")

def main():
    # Add the image to the top left corner
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("ReviewIcon.png", width=150) 

    # Main title
    with col2:
        # Add some spacing between the picture icon and the title 
        st.write("")  # This adds a blank line
        st.markdown("<h1 style='font-family:sans-serif; color:#6699CC;'>Review Analyzer: Enhancing Customer Satisfaction with Data-Driven  Product Insights</h1>", unsafe_allow_html=True)
        
    #st.title("Leveraging Sentiment Analysis and Similarity Search to Optimize Product offerings and success")

    # Get user input by asking them to enter a new review
    st.markdown("<h3 style='font-size: 20px;'>Enter a new review:</h3>", unsafe_allow_html=True)
    user_review = st.text_input("")

    if user_review: 
        # Encode the user's review using the same model
        user_review_embedding = embedding_model.encode([user_review])

        # Calculate cosine similarity between the user's review and existing reviews
        similarity_scores = cosine_similarity(user_review_embedding, embeddings)
        top_5_most_similar_indices = similarity_scores.argsort()[0][-5:][::-1]

        # Display the top 5 most similar reviews with in a table 
        st.markdown("### Top 5 Most Similar Reviews:")
        st.table(data.iloc[top_5_most_similar_indices])

        st.markdown("### Sentiment Prediction:")
        sentiment_proba = model.predict_proba(user_review_embedding)[0, 1]  # Extract the probability
        predicted_sentiment = "Positive" if sentiment_proba >= 0.5 else "Negative"
        #st.write(f"**Predicted Sentiment:** {predicted_sentiment}")
        #st.write(f"**Sentiment Probability:** {sentiment_proba:.2f}")
        st.write(f"<h4 style='font-size: 20px;'>Predicted Sentiment: {predicted_sentiment}</h4>", unsafe_allow_html=True)
        st.write(f"<h4 style='font-size: 20px;'>Sentiment Probability: {sentiment_proba:.2f}</h4>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()