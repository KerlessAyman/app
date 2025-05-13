# Step 8: Streamlit App (Bonus 2)
import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load model and vectorizer
model = joblib.load('spam_classifier.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

# Streamlit UI
st.title("Email Spam Detector")
email_text = st.text_area("Enter email text:")

if st.button("Check Spam"):
    if email_text:
        # Preprocess
        text_features = tfidf.transform([email_text])

        # Predict
        prediction = model.predict(text_features)
        # Display result
        if prediction[0] == 1:
            st.error("This email is SPAM!")
        elif prediction[0] == 0:
            st.success("This email is NOT SPAM")
    else:
        st.warning("Please enter some text to analyze")