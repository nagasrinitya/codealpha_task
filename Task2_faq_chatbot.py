import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 FAQ Chatbot")

faq_questions = [
    "What is AI?",
    "What is Python?",
    "What is Machine Learning?",
    "Who developed Python?"
]

faq_answers = [
    "AI means Artificial Intelligence.",
    "Python is a programming language.",
    "Machine Learning is a subset of AI.",
    "Python was developed by Guido van Rossum."
]

user_question = st.text_input("Ask a Question")

if st.button("Get Answer"):

    all_questions = faq_questions + [user_question]

    vectorizer = CountVectorizer().fit_transform(all_questions)

    similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])

    index = similarity.argmax()

    st.success(faq_answers[index])