import pandas as pd
import re
import pickle
import nltk

from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import PassiveAggressiveClassifier

nltk.download('stopwords')

fake = pd.read_csv("dataset/Fake.csv")

true = pd.read_csv("dataset/True.csv")

fake["label"] = 0

true["label"] = 1

data = pd.concat([fake, true])

data = data[['text', 'label']]

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [
        word for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

data["text"] = data["text"].apply(clean_text)

X = data["text"]

y = data["label"]

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = PassiveAggressiveClassifier()

model.fit(X_train, y_train)

pickle.dump(model, open("model/model.pkl", "wb"))

pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model Trained Successfully")