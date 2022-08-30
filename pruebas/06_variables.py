from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='../templates')


@app.route('/user/<name>')
@app.route('/user/')
def index(name="John doe"):
    age = 17
    my_list = [1,2,3,4]
    return render_template('user.html', name=name, age=age, my_list=my_list)#Almacena en el template la variable name con el nombre name


if __name__=='__main__':
    app.run(debug=True, port=8000)