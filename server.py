from flask import Flask, render_template, flash, request, jsonify
from flask_restful import Api, Resource
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from generator import generate_password


# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# API Config
api = Api(app)


# Classes
class PasswordForm(Form):
    seed = TextField('Seed:')
    password = TextField('Password:')
    submit = SubmitField('Generate')


class Password(Resource):
    def get(self):
        password = generate_password(1337)
        return {'password' : password }


# HTTP Routing
@app.route("/")
def index():
    form = PasswordForm()
    return render_template('index.html', form=form)

@app.route('/generator', methods=['GET', 'POST'])
def serve_new_password():
    form = PasswordForm()

    if request.method == 'POST':
        seed = form.seed.data
        form.password.data = generate_password(seed)

    return render_template('index.html', form=form)

# API Routing
api.add_resource(Password, '/api')


# Starting the program, served at 0.0.0.0 on port 1337
if __name__ == '__main__':
   app.run(host='0.0.0.0', port='80')