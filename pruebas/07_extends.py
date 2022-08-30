from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder="../templates")


@app.route('/')
def index():
    name = "John Doe"
    return render_template('index.html', name=name)


@app.route('/client')
def client():
    list_name = ["John Doe","juan perez","Mario Rosi"]
    return render_template('client.html', list_name=list_name)


if __name__ == '__main__':
    app.run(debug=True, port=8000)