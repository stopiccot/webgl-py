import coffeescript, flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('index.html')

@app.route('/js/<file>')
def js(file):
    return coffeescript.compile_file('views/' + file + '.coffee')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)