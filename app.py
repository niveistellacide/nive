from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/dtl')
def dtl_shit():
    return 'bruh'


if __name__ == '__main__':
    app.run(port=80)
