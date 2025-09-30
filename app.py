import nltk
#nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('model.h5')
import json
import random
intents = json.loads(open('data.json').read())
words = pickle.load(open('texts.pkl','rb'))
classes = pickle.load(open('labels.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rambla")
def rambla():
    return render_template("menu-la.html")

@app.route("/latium")
def latium():
    return render_template("latium.html")


@app.route("/addik")
def addik():
    return render_template("addik.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)




from flask import Flask, render_template, request
import pymysql

@app.route("/reserver", methods=['POST'])
def res():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="restauration"
    )
    rest = request.form.get('rest')
    nom = request.form.get('name')
    num = request.form.get('num')
    date = request.form.get('date')
    time = request.form.get('time')
    nbr = request.form.get('nbr')
    cursor = connection.cursor()
    query = "INSERT INTO {} (nom, num, date, time,nbr) VALUES (%s, %s, %s, %s,%s)".format(rest)
    cursor.execute(query, (nom, num, date, time,nbr))
    connection.commit()
    sql = "SELECT id FROM {} WHERE num = %s AND nom = %s".format(rest)
    cursor.execute(sql, (num, nom))
    rows = cursor.fetchall()
    reservation_id = None
    for row in rows:
        reservation_id = row[0]
    cursor.close()
    connection.close()
    return str(reservation_id)

@app.route("/annu", methods=['POST'])
def annule():
    print("num")
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="restauration"
        )

        restaurant = request.form.get('rest')
        num = request.form.get('num')
        print(restaurant)
        print(num)
        cursor = connection.cursor()
        query = "DELETE FROM {} WHERE id=%s".format(restaurant)
        cursor.execute(query, (num,))
        connection.commit()

        if cursor.rowcount == 1:
            msg = "Réservation annulée"
        else:
            msg = "La réservation n'a pas été trouvée."

        cursor.close()
        connection.close()

        return str(msg)

    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
    
    
    
if __name__ == "__main__":
    app.run()