import coffeescript, flask
app = flask.Flask(__name__)
app.config.update(SERVER_NAME = 'stopiccot.com')

@app.route("/")
def home():
    return flask.render_template('index.html')

@app.route("/", subdomain = "qr")
def qr():
    return flask.render_template('qr_index.html')

@app.route("/", subdomain = "sun")
def sun():
    return flask.render_template('sun_index.html')

@app.route('/js/<file>')
def js(file):
    return coffeescript.compile_file('views/' + file + '.coffee')

app.add_url_rule(app.static_url_path + '/<path:filename>',
                 endpoint = 'static',
                 view_func = app.send_static_file,
                 subdomain = 'qr')

app.add_url_rule(app.static_url_path + '/<path:filename>',
                 endpoint = 'static',
                 view_func = app.send_static_file,
                 subdomain = 'sun')

if __name__ == "__main__":
    app.config.update(SERVER_NAME = 'stopiccot.dev:4568')
    app.run(host = '0.0.0.0', port = 4568, debug = True)