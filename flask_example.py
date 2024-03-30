from flask import Flask, request,jsonify
from wtforms import Form, StringField, validators

app = Flask(__name__)

class RegistrationForm(Form):
    name = StringField('Name', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35), validators.Email()])

    @app.route('/register', methods=['POST'])
    def register():
        form = RegistrationForm(request.form)
        if form.validate():
            return jsonify(success=True)
        else:
            return jsonify(success=False,error=form.errors)
        
if __name__ == '__main__':
    app.run(debug=True)