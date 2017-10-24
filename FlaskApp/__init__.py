from flask import Flask, render_template
from dbconnect import connection
import json

def extract_tweets(topic):
    try:
        cursor, conn = connection()
    except Exception as e:
        return(str(e))
    query = ('SELECT * FROM '+ topic + ';')
    cursor.execute(query)
    tup_data = cursor.fetchall()
    data_list = []
    for tup in tup_data:
        text = tup[3].decode('latin-1')
        city = tup[4].decode('latin-1')
        datarow = [tup[0], tup[1], tup[2], text, city, tup[5]]
        data_list.append(datarow)
    return data_list

def convert_to_json(data):
    data_out = []
    for element in data:
        user = element[0].decode('latin-1').encode('utf-8')
        count = str(int(element[1]))
        data_out.append({"user":user, "count":count})
    return data_out

def top_users(topic):
    try:
        cursor, conn = connection()
    except Exception as e:
        return(str(e))
    query = ('SELECT user, COUNT(*) FROM '+ topic + ' GROUP BY user ORDER BY COUNT(*) DESC LIMIT 10;')
    cursor.execute(query)
    tup_data = cursor.fetchall()
    data_out = convert_to_json(tup_data)
    return data_out

def top_cities(topic):
    try:
        cursor, conn = connection()
    except Exception as e:
        return(str(e))
    query = ('SELECT city, COUNT(*) FROM '+ topic + ' GROUP BY city ORDER BY COUNT(*) DESC LIMIT 10;')
    cursor.execute(query)
    tup_data = cursor.fetchall()
    data_out = convert_to_json(tup_data)
    return data_out

app = Flask(__name__)

#  Main page

@app.route('/')
def homepage():
    data = top_users('construction')
    return render_template("construction/users.html", data=data)

#  TOPIC: Oil

@app.route('/oil/users/')
def oil_users():
    data = top_users('oil')
    return render_template("oil/users.html", data=data)
@app.route('/oil/cities/')
def oil_cities():
    data = top_cities('oil')
    return render_template("oil/cities.html", data=data)
@app.route('/oil/tweets/')
def oil_tweets():
    data = extract_tweets('oil')
    return render_template("oil/tweets.html", data=data)
@app.route('/oil/')
def oil():
    data = top_users('oil')
    return render_template("oil/users.html", data=data)

#  TOPIC: Construction

@app.route('/construction/')
def construction():
    data = top_users('construction')
    return render_template("construction/users.html", data=data)
@app.route('/construction/users/')
def construction_users():
    data = top_users('construction')
    return render_template("construction/users.html", data=data)
@app.route('/construction/cities/')
def construction_cities():
    data = top_cities('construction')
    return render_template("construction/cities.html", data=data)
@app.route('/construction/tweets/')
def construction_tweets():
    data = extract_tweets('construction')
    return render_template("construction/tweets.html", data=data)

#  TOPIC: Energy

@app.route('/energy/')
def energy():
    data = top_users('energy')
    return render_template("energy/users.html", data=data)
@app.route('/energy/users/')
def energy_users():
    data = top_users('energy')
    return render_template("energy/users.html", data=data)
@app.route('/energy/cities/')
def energy_cities():
    data = top_cities('energy')
    return render_template("energy/cities.html", data=data)
@app.route('/energy/tweets/')
def energy_tweets():
    data = extract_tweets('energy')
    return render_template("energy/tweets.html", data=data)

if __name__ == "__main__":
    app.run()
