from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # return "<h1>Hello World!</h1>"
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
