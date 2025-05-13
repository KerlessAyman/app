# spam Email
# 📧 Email Spam Detector with Streamlit

A simple machine learning web app to detect whether an email is **Spam** or **Not Spam** using a trained **Random Forest Classifier** and **TF-IDF vectorizer**.

---

## 🚀 Live Demo
You can try the app here: **[Streamlit App Link](https://spam-application.streamlit.app/)**  

---

## 🧠 How It Works

1. **Data Preprocessing**
   - Lowercasing, removing punctuation
   - Tokenization and stopword removal
   - Stemming using NLTK

2. **Vectorization**
   - TF-IDF vectorizer with top 5000 features

3. **Model**
   - Random Forest Classifier trained on spam/ham dataset

4. **Prediction**
   - Text is preprocessed, vectorized, and passed to the model for prediction

---

## 🗂 Project Structure

