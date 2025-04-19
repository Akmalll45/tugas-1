from flask import Flask, render_template

app = Flask(__name__)

nama ="my name is akmal"

@app.route("/")
def home():
    return f"<p>hallo everyone {nama}</P>"

@app.route("/bostrapp")
def bostrapp():
    return render_template("index.html")

@app.route("/name/<name>")
def name(namm):
    return f"hello ,{namm}"

@app.route('/user/<int:user_id>')
def user_id(user_id):
    return f"User ID: {user_id}"

@app.route('/profil/<yoii>')  
def profil(naam):
    return render_template("profil.html", user = naam)

app_name = "My Flask App"  # Variabel global

@app.route('/nama')
def nama():
    return f"Welcome to {app_name}!"

@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('index.html', user=user)

if __name__=="__main__":
    app.run(debug=True)
