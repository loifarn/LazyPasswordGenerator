from flask import Flask, render_template, flash, request
from flask_restful import Api, Resource
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from generator import generate_password


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# API Config
api = Api(app)


# Classes
class PasswordForm(Form):
    password = TextField('Password:')


class Password(Resource):
    def get(self):
        password = generate_password(1337)
        return {'password' : password }


# HTTP Routing
@app.route("/", methods=['GET', 'POST'])
def serve():
    form = PasswordForm(request.form)
    print(form.errors)

    if request.method == 'POST':
        seed = request.form['password']
        form.password.data = generate_password(seed)
        #flash(generate_password(seed))
        
    return render_template('index.html', title="Password", form=form)


# API Routing
api.add_resource(Password, '/pw')


# Starting the program, served at 0.0.0.0 on port 1337
if __name__ == '__main__':
    app.run('0.0.0.0', '1337')

