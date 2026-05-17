from django.shortcuts import render

import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

def home(request):

    result = ""

    if request.method == "POST":

        news = request.POST['news']

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        if prediction[0] == 0:
            result = "FAKE NEWS"
        else:
            result = "REAL NEWS"

    return render(request, 'index.html', {'result': result})