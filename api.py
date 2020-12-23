import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Congrats You Create Webpage Using flask in python</h1><p>This site is a prototype API For Flask api</p>"


app.run()
