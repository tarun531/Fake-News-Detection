# 📰 Fake News Detection System using Machine Learning & NLP

## 📌 Project Overview

This project demonstrates an AI-powered Fake News Detection System that identifies whether a news article is real or fake using Natural Language Processing (NLP) and Machine Learning techniques.

The system analyzes news text, processes the content using TF-IDF Vectorization, and predicts the authenticity of the news article using a trained machine learning model.

Unlike traditional ML projects that only focus on training models, this project includes:

* Data preprocessing
* Text cleaning
* NLP techniques
* Machine learning classification
* Real-time prediction system
* Interactive web interface

This project simulates a real-world misinformation detection system used in modern media platforms.

---

# 🎯 Key Features

✅ Fake News Detection using Machine Learning
🧠 Natural Language Processing (NLP)
📊 TF-IDF Text Vectorization
🌐 Flask Web Application
🚀 Real-time News Prediction
📁 Dataset-based Model Training
🎨 Responsive User Interface
🔍 Text Cleaning & Preprocessing

---

# 🧠 Architecture / Workflow

```text id="1mjlwm"
User Enters News Article
            ↓
Text Preprocessing
(Remove Stopwords, Symbols, Lowercasing)
            ↓
TF-IDF Vectorization
            ↓
Machine Learning Model Prediction
            ↓
Classifies News as:
REAL or FAKE
            ↓
Displays Result on Web Dashboard
```

---

# ⚙️ Tech Stack

| Category        | Tools                         |
| --------------- | ----------------------------- |
| Programming     | Python                        |
| ML Framework    | Scikit-learn                  |
| NLP             | NLTK                          |
| Backend         | Flask                         |
| Frontend        | HTML, CSS, Bootstrap          |
| Data Processing | Pandas, NumPy                 |
| Model           | Passive Aggressive Classifier |
| Deployment      | Render / GitHub               |

---

# 📂 Project Structure

```text id="ztjlwm"
Fake-News-Detection/
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── fake_news.csv
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# 🔄 How It Works (Step-by-Step)

## 1️⃣ Dataset Collection

The system uses a Fake News dataset containing:

* Real News Articles
* Fake News Articles

---

## 2️⃣ Text Preprocessing

The text is cleaned using NLP techniques:

* Lowercasing
* Removing punctuation
* Removing stopwords
* Tokenization

Example:

```text id="wjlwm0"
Breaking News!!! → breaking news
```

---

## 3️⃣ TF-IDF Vectorization

Text data is converted into numerical vectors using:

```python id="4u3h4r"
TfidfVectorizer()
```

This helps the machine learning model understand textual patterns.

---

## 4️⃣ Model Training

The model is trained using:

```python id="4jlwm1"
PassiveAggressiveClassifier
```

The algorithm learns patterns from fake and real news articles.

---

## 5️⃣ Real-Time Prediction

The user enters a news article through the web application.

The system predicts:

✅ REAL NEWS
❌ FAKE NEWS

---

# 🚀 How to Run This Project

## 🔹 Prerequisites

* Python 3.x
* VS Code
* Git
* pip

---

## 🔹 Step 1: Clone Repository

```bash id="jlwm2"
git clone https://github.com/tarun531/Fake-News-Detection.git

cd Fake-News-Detection
```

---

## 🔹 Step 2: Create Virtual Environment

```bash id="jlwm3"
python -m venv venv
```

Activate environment:

### Windows

```bash id="jlwm4"
venv\Scripts\activate
```

---

## 🔹 Step 3: Install Dependencies

```bash id="jlwm5"
pip install -r requirements.txt
```

---

## 🔹 Step 4: Train Machine Learning Model

```bash id="jlwm6"
python train_model.py
```

This generates:

```text id="jlwm7"
model.pkl
vectorizer.pkl
```

---

## 🔹 Step 5: Run Flask Application

```bash id="jlwm8"
python app.py
```

---

## 🔹 Step 6: Open Browser

```text id="jlwm9"
http://127.0.0.1:5000
```

---

# 📊 Machine Learning Workflow

## Input

* News Article Text

## Processing

* NLP Cleaning
* TF-IDF Vectorization

## Output

* REAL
* FAKE

---

# 📸 Expected Output

## Fake News Example

### Input:

```text id="jlwm10"
Aliens landed in New York yesterday and took control of the city.
```

### Output:

```text id="jlwm11"
FAKE NEWS
```

---

## Real News Example

### Input:

```text id="jlwm12"
The government announced new economic reforms during the budget session.
```

### Output:

```text id="jlwm13"
REAL NEWS
```

---

# 🏆 Key Learning Outcomes

* Natural Language Processing (NLP)
* Text preprocessing techniques
* TF-IDF vectorization
* Machine learning model training
* Flask web development
* Real-time prediction systems
* Dataset handling and preprocessing

---

# 🔥 Why This Project is Important

Fake news spreads rapidly through social media and online platforms.

This project demonstrates how AI and NLP can help:

* Detect misinformation
* Improve news credibility
* Automate content verification
* Build intelligent media systems

It simulates real-world AI-powered misinformation detection platforms.

---

# 👨‍💻 Author

## Tarun Sunkam

GitHub:
https://github.com/tarun531

---

# ⭐ Future Improvements

* Deep Learning Models (LSTM/BERT)
* News API Integration
* Multi-language Detection
* User Authentication
* News Credibility Score
* Admin Dashboard
* Cloud Deployment
* Real-time News Monitoring

---

# 💡 Final Note

This project represents a real-world AI-powered Fake News Detection System that combines Machine Learning, NLP, and Web Development technologies to identify misinformation and classify news articles with high accuracy.
