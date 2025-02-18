from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', title="Accueil")

@app.route('/login')
def login():
    return render_template('login.html', title="Connexion")

if __name__ == '__main__':
    app.run(debug=True)
