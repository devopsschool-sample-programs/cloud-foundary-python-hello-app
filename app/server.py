import os
from flask import Flask
from flask import current_app as current_app
from flask import redirect, render_template, url_for
import forms

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=("GET", "POST"))
def home():
    return contact()
# def hello():
#     return "Hello World!"

@app.route("/contact", methods=("GET", "POST"))
def contact():
    form = forms.Contact()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template("contact.jinja2", form=form, template="form-template")

@app.route('/success', methods=("GET", "POST"))
def success():
    return render_template("success.jinja2", template="form-template")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)